from __future__ import annotations
from pathlib import Path
import ast
from .filesystem import iter_owned_files
from ..model import FactGraph, Node, Edge, Evidence

ROUTE_DECORATORS = {"get":"GET","post":"POST","put":"PUT","patch":"PATCH","delete":"DELETE","options":"OPTIONS","head":"HEAD"}
CONTROL_HINTS = {
    "login_required":"authentication",
    "permission_required":"authorization",
    "requires_auth":"authentication",
    "authorize":"authorization",
    "authenticated":"authentication",
    "validator":"validation",
    "validate":"validation",
}

def _name(node):
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        left = _name(node.value)
        return f"{left}.{node.attr}" if left else node.attr
    if isinstance(node, ast.Call):
        return _name(node.func)
    return ""

def _str_arg(call):
    if not isinstance(call, ast.Call) or not call.args:
        return ""
    a = call.args[0]
    return a.value if isinstance(a, ast.Constant) and isinstance(a.value, str) else ""

def scan_python(root: Path) -> FactGraph:
    graph = FactGraph()
    module_nodes = {}
    symbol_nodes = {}
    parsed = {}

    py_files = [p for p in iter_owned_files(root) if p.suffix == ".py"]
    for p in py_files:
        rel = p.relative_to(root).as_posix()
        try:
            tree = ast.parse(p.read_text(encoding="utf-8", errors="ignore"), filename=rel)
        except SyntaxError:
            continue
        parsed[rel] = tree
        module_name = ".".join(Path(rel).with_suffix("").parts)
        mid = f"module:{module_name}"
        module_nodes[rel] = mid
        graph.add_node(Node(mid, "module", module_name, rel, {"language":"Python"}, Evidence(evidence=[rel])))

        for node in tree.body:
            if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                if isinstance(node, ast.ClassDef):
                    kind = "class"
                    decorators = [_name(d) for d in node.decorator_list]
                    bases = [_name(b) for b in node.bases]
                    nid = f"type:{module_name}:{node.name}"
                    graph.add_node(Node(
                        nid, kind, node.name, rel,
                        {"decorators":decorators,"bases":bases,"language":"Python"},
                        Evidence(evidence=[f"{rel}:{node.lineno}"])
                    ))
                    symbol_nodes[(rel,node.name)] = nid
                    graph.add_edge(Edge(mid,nid,"declares",[f"{rel}:{node.lineno}"]))

                    for child in node.body:
                        if isinstance(child,(ast.FunctionDef,ast.AsyncFunctionDef)):
                            fid = f"method:{module_name}:{node.name}#{child.name}"
                            decs = [_name(d) for d in child.decorator_list]
                            graph.add_node(Node(
                                fid,"method",child.name,rel,
                                {"owner":nid,"decorators":decs,"async":isinstance(child,ast.AsyncFunctionDef)},
                                Evidence(evidence=[f"{rel}:{child.lineno}"])
                            ))
                            graph.add_edge(Edge(nid,fid,"declares",[f"{rel}:{child.lineno}"]))
                            _decorator_semantics(graph, fid, child.decorator_list, rel, child.lineno)
                else:
                    fid = f"function:{module_name}:{node.name}"
                    decs = [_name(d) for d in node.decorator_list]
                    graph.add_node(Node(
                        fid,"function",node.name,rel,
                        {"decorators":decs,"async":isinstance(node,ast.AsyncFunctionDef)},
                        Evidence(evidence=[f"{rel}:{node.lineno}"])
                    ))
                    symbol_nodes[(rel,node.name)] = fid
                    graph.add_edge(Edge(mid,fid,"declares",[f"{rel}:{node.lineno}"]))
                    _decorator_semantics(graph, fid, node.decorator_list, rel, node.lineno)

        # ORM-ish entities: SQLAlchemy/Django model inheritance
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                bases = [_name(b) for b in node.bases]
                if any("Model" in b or "Base" == b.split(".")[-1] for b in bases):
                    nid = symbol_nodes.get((rel,node.name))
                    if nid:
                        for n in graph.nodes:
                            if n.id == nid:
                                n.kind = "entity"
                                n.metadata["orm_hint"] = bases
                                break

        # Pytest/unittest-style tests
        low = rel.lower()
        for node in ast.walk(tree):
            if isinstance(node,(ast.FunctionDef,ast.AsyncFunctionDef)) and (
                node.name.startswith("test_") or "/test" in low or "/tests/" in low
            ):
                tid = f"test:{module_name}:{node.name}:{node.lineno}"
                graph.add_node(Node(
                    tid,"test",node.name,rel,{"framework":"pytest/unittest-like"},
                    Evidence(evidence=[f"{rel}:{node.lineno}"])
                ))

    # imports + calls
    name_to_node = {}
    nodes_by_id = {}
    for n in graph.nodes:
        if n.kind in {"class","entity","function","method","module"}:
            name_to_node.setdefault(n.name, []).append(n.id)
        nodes_by_id[n.id] = n

    for rel, tree in parsed.items():
        mid = module_nodes[rel]
        imports = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports[alias.asname or alias.name.split(".")[0]] = alias.name
            elif isinstance(node, ast.ImportFrom):
                mod = node.module or ""
                for alias in node.names:
                    imports[alias.asname or alias.name] = f"{mod}.{alias.name}".strip(".")
        # Full dotted import targets, including third-party ones that resolve to nothing in
        # this repo (the `imports` dict below only uses these to wire in-repo edges and drops
        # the rest) — kept here, same shape as the Java/TS scanners' node.metadata["imports"],
        # so a later pass (external systems) can allowlist-match without a new parser.
        nodes_by_id[mid].metadata["imports"] = sorted(set(imports.values()))
        for local, full in imports.items():
            simple = full.split(".")[-1]
            for target in name_to_node.get(simple, []):
                graph.add_edge(Edge(mid,target,"imports",[rel]))

        # Calls are attributed to nearest enclosing function/method when possible.
        class Visitor(ast.NodeVisitor):
            def __init__(self):
                self.scope = [mid]
            def visit_ClassDef(self, node):
                nid = next((x.id for x in graph.nodes if x.path==rel and x.name==node.name and x.kind in {"class","entity"}), mid)
                self.scope.append(nid)
                for ch in node.body: self.visit(ch)
                self.scope.pop()
            def visit_FunctionDef(self, node):
                candidates = [x.id for x in graph.nodes if x.path==rel and x.name==node.name and x.kind in {"function","method"}]
                sid = candidates[0] if candidates else self.scope[-1]
                self.scope.append(sid)
                for ch in node.body: self.visit(ch)
                self.scope.pop()
            visit_AsyncFunctionDef = visit_FunctionDef
            def visit_Call(self, node):
                called = _name(node.func)
                simple = called.split(".")[-1]
                for target in name_to_node.get(simple, []):
                    if target != self.scope[-1]:
                        graph.add_edge(Edge(self.scope[-1],target,"calls",[f"{rel}:{getattr(node,'lineno',0)}"]))
                self.generic_visit(node)
        Visitor().visit(tree)

    return graph

def _decorator_semantics(graph, owner_id, decorators, rel, lineno):
    for d in decorators:
        name = _name(d)
        low = name.lower().split(".")[-1]
        # FastAPI/Flask-like route decorators: app.get("/x"), router.post("/x")
        method = low
        if method in ROUTE_DECORATORS:
            path = _str_arg(d)
            route_id = f"route:{ROUTE_DECORATORS[method]}:{path}:{rel}:{lineno}"
            graph.add_node(Node(
                route_id,"route",f"{ROUTE_DECORATORS[method]} {path or '/'}",rel,
                {"http_method":ROUTE_DECORATORS[method],"path":path or "/","handler":owner_id,"framework":"Python web framework-like"},
                Evidence(evidence=[f"{rel}:{lineno}"])
            ))
            graph.add_edge(Edge(route_id,owner_id,"handled_by",[f"{rel}:{lineno}"]))
        for hint, control in CONTROL_HINTS.items():
            if hint in low:
                cid = f"control:{control}:{owner_id}:{low}"
                graph.add_node(Node(
                    cid,"control",low,rel,
                    {"control_type":control,"target":owner_id},
                    Evidence(evidence=[f"{rel}:{lineno}"])
                ))
                graph.add_edge(Edge(cid,owner_id,"protects",[f"{rel}:{lineno}"]))
