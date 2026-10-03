from __future__ import annotations
from pathlib import Path
import re
from .filesystem import iter_owned_files
from .common import balanced_block, line_of
from ..model import FactGraph, Node, Edge, Evidence
from ..source_roles import classify_source

TS_EXTS = {".ts",".tsx",".js",".jsx"}
IMPORT_RE = re.compile(r'import\s+(?:type\s+)?(?:[^"\']+\s+from\s+)?["\']([^"\']+)["\']|require\(\s*["\']([^"\']+)["\']\s*\)')
CLASS_RE = re.compile(r'(?P<decs>(?:@\w+(?:\([^)]*\))?\s*)*)(?:export\s+)?(?:default\s+)?class\s+(?P<name>[A-Za-z_]\w*)(?:\s+extends\s+(?P<extends>[A-Za-z_]\w*))?(?:\s+implements\s+(?P<implements>[^{]+))?')
INTERFACE_RE = re.compile(r'(?:export\s+)?interface\s+(?P<name>[A-Za-z_]\w*)')
METHOD_RE = re.compile(r'(?P<decs>(?:@\w+(?:\([^)]*\))?\s*)*)(?:(?:public|private|protected|static|async|readonly)\s+)*(?P<name>[A-Za-z_]\w*)\s*\((?P<params>[^)]*)\)\s*(?::\s*(?P<ret>[^{=>\n]+))?')
DEC_RE = re.compile(r'@([A-Za-z_]\w*)\s*(?:\(([^)]*)\))?')
EXPRESS_RE = re.compile(r'(?P<obj>app|router|server|[A-Za-z_]\w*Router)\.(?P<method>get|post|put|patch|delete|options|head|all)\s*\(\s*["\'](?P<path>[^"\']+)["\']',re.I)
TEST_RE = re.compile(r'\b(?:it|test)\s*\(\s*["\']([^"\']+)["\']')
PRISMA_RE = re.compile(r'\bprisma\.([A-Za-z_]\w*)\.([A-Za-z_]\w*)\s*\(')
MONGOOSE_RE = re.compile(r'\bmongoose\.model\s*\(\s*["\']([^"\']+)["\']')
THIS_CALL_RE = re.compile(r'\bthis\.([A-Za-z_]\w*)\.([A-Za-z_]\w*)\s*\(')

NEST_CLASS={"Controller":"controller","Injectable":"service","Module":"module"}
NEST_HTTP={"Get":"GET","Post":"POST","Put":"PUT","Patch":"PATCH","Delete":"DELETE","Options":"OPTIONS","Head":"HEAD","All":"ANY"}

def _decs(s): return [(m.group(1),m.group(2) or "") for m in DEC_RE.finditer(s or "")]
def _str(raw):
    m=re.search(r'["\']([^"\']+)["\']',raw or "")
    return m.group(1) if m else ""
def _join(a,b):
    parts=[x.strip("/") for x in (a,b) if x and x.strip("/")]
    return "/"+"/".join(parts) if parts else "/"


def _is_test_path(rel: str) -> bool:
    low = rel.lower()
    return any(x in low for x in (".test.", ".spec.", "/test/", "/tests/", "__tests__"))

def _classify_class(name: str, rel: str, dec_names: list[str], default_kind: str) -> str:
    if _is_test_path(rel):
        return "test_class"
    lname=name.lower()
    if lname.endswith("dto") or "/dto/" in rel.lower():
        return "dto"
    if lname.endswith("factory"):
        return "factory"
    return default_kind

def scan_typescript(root: Path) -> FactGraph:
    graph=FactGraph()
    classes={}
    file_imports={}
    texts={}
    class_records=[]

    for p in [p for p in iter_owned_files(root) if p.suffix.lower() in TS_EXTS]:
        rel=p.relative_to(root).as_posix()
        text=p.read_text(encoding="utf-8",errors="ignore")
        if _is_test_path(rel):
            for tm in TEST_RE.finditer(text):
                graph.add_node(Node(f"test:{rel}:{line_of(text,tm.start())}","test",tm.group(1),rel,{"framework":"Jest/Vitest/Mocha-like"},Evidence(evidence=[f"{rel}:{line_of(text,tm.start())}"])))
            continue
        if classify_source(rel, root)["scope"] == "frontend":
            continue
        texts[rel]=text
        imports=[m.group(1) or m.group(2) for m in IMPORT_RE.finditer(text)]
        file_imports[rel]=imports

        for cm in CLASS_RE.finditer(text):
            block=balanced_block(text,cm.end())
            if not block: continue
            bstart,bend=block
            decs=_decs(cm.group("decs"))
            names=[a for a,_ in decs]
            kind=next((NEST_CLASS[a] for a in names if a in NEST_CLASS),"class")
            kind=_classify_class(cm.group("name"), rel, names, kind)
            nid=f"type:{rel}:{cm.group('name')}"
            ev=[f"{rel}:{line_of(text,cm.start())}"]
            graph.add_node(Node(nid,kind,cm.group("name"),rel,{
                "language":"TypeScript/JavaScript","annotations":names,"imports":imports,
                "extends":cm.group("extends"),"implements":(cm.group("implements") or "").strip(), "is_test_code": _is_test_path(rel)
            },Evidence(evidence=ev)))
            classes[cm.group("name")]=nid
            class_records.append((nid,cm.group("name"),rel,text,bstart,bend,decs))

        for im in INTERFACE_RE.finditer(text):
            name=im.group("name"); nid=f"interface:{rel}:{name}"
            graph.add_node(Node(nid,"interface",name,rel,{"language":"TypeScript"},Evidence(evidence=[f"{rel}:{line_of(text,im.start())}"])))
            classes[name]=nid

        for rm in EXPRESS_RE.finditer(text):
            method=rm.group("method").upper(); path=rm.group("path")
            rid=f"route:{method}:{path}:{rel}:{line_of(text,rm.start())}"
            graph.add_node(Node(rid,"route",f"{method} {path}",rel,{
                "http_method":method,"path":path,"framework":"Express/Fastify-like"
            },Evidence(evidence=[f"{rel}:{line_of(text,rm.start())}"])))

        for pm in PRISMA_RE.finditer(text):
            model,op=pm.group(1),pm.group(2)
            eid=f"datastore:prisma:{model}"
            graph.add_node(Node(eid,"entity",model,rel,{"orm":"Prisma","observed_operation":op},Evidence(evidence=[f"{rel}:{line_of(text,pm.start())}"])))
        for mm in MONGOOSE_RE.finditer(text):
            name=mm.group(1)
            graph.add_node(Node(f"datastore:mongoose:{name}","entity",name,rel,{"orm":"Mongoose"},Evidence(evidence=[f"{rel}:{line_of(text,mm.start())}"])))

    for nid,name,rel,text,bstart,bend,decs in class_records:
        body=text[bstart:bend]
        base=""
        for d,raw in decs:
            if d=="Controller": base=_str(raw)

        # constructor param-properties approximate DI variable->type mapping
        vars_to_type={}
        ctor=re.search(r'constructor\s*\(([^)]*)\)',body,re.S)
        if ctor:
            params=ctor.group(1)
            for m in re.finditer(r'(?:private|public|protected)?\s*(?:readonly\s+)?([A-Za-z_]\w*)\s*:\s*([A-Za-z_]\w*)',params):
                vars_to_type[m.group(1)]=m.group(2)
                if m.group(2) in classes:
                    graph.add_edge(Edge(nid,classes[m.group(2)],"depends_on",[rel]))

        for mm in METHOD_RE.finditer(body):
            meth=mm.group("name")
            if meth in {"if","for","while","switch","catch","constructor"}: continue
            abspos=bstart+mm.start()
            mid=f"method:{rel}:{name}#{meth}:{line_of(text,abspos)}"
            anns=_decs(mm.group("decs"))
            ev=[f"{rel}:{line_of(text,abspos)}"]
            graph.add_node(Node(mid,"method",meth,rel,{
                "owner":nid,"params":" ".join((mm.group("params") or "").split()),
                "return_type":" ".join((mm.group("ret") or "").split()),
                "annotations":[a for a,_ in anns]
            },Evidence(evidence=ev)))
            graph.add_edge(Edge(nid,mid,"declares",ev))
            mblock=balanced_block(body,mm.end())
            if mblock:
                ms,me=mblock; mbody=body[ms:me]
                for cm in THIS_CALL_RE.finditer(mbody):
                    var,called=cm.group(1),cm.group(2)
                    typ=vars_to_type.get(var)
                    if typ and typ in classes:
                        graph.add_edge(Edge(mid,classes[typ],"calls_dependency",ev))
                        graph.add_edge(Edge(mid,f"method-name:{typ}#{called}","calls_method_name",ev))
            for a,raw in anns:
                if a in NEST_HTTP:
                    path=_join(base,_str(raw))
                    rid=f"route:{NEST_HTTP[a]}:{path}:{rel}:{name}#{meth}"
                    graph.add_node(Node(rid,"route",f"{NEST_HTTP[a]} {path}",rel,{
                        "http_method":NEST_HTTP[a],"path":path,"handler":mid,"framework":"NestJS"
                    },Evidence(evidence=ev)))
                    graph.add_edge(Edge(rid,mid,"handled_by",ev))

        impl = next((n.metadata.get("implements") for n in graph.nodes if n.id==nid), "")
        if impl:
            for token in impl.split(","):
                simple=re.split(r'[<\s]',token.strip())[0]
                if simple in classes: graph.add_edge(Edge(nid,classes[simple],"implements",[rel]))
        ext = next((n.metadata.get("extends") for n in graph.nodes if n.id==nid), "")
        if ext and ext in classes: graph.add_edge(Edge(nid,classes[ext],"extends",[rel]))

    return graph
