from __future__ import annotations
from pathlib import Path
import json, shutil, yaml
from .model import FactGraph
from .scanners.filesystem import scan_filesystem
from .scanners.java import scan_java
from .scanners.typescript import scan_typescript
from .scanners.python import scan_python
from .scanners.frontend import scan_frontend
from .recovery.controls import recover_controls
from .recovery.traceability import enrich_traceability
from .recovery.semantic import build_semantic_model
from .renderers.markdown import system_overview, recovered_rad, recovered_sdd, recovered_odd, testing_baseline, quality_report, doc_signature
from .validation import validate_model
from .manifest import build_manifest
from .export import generic_context
from .scanner_output import scanner_findings

OUTPUT_MARKER = ".ases-output"

def clean_output(path: Path) -> bool:
    path = path.resolve()
    if not path.exists():
        return False
    if not path.is_dir():
        raise ValueError(f"Not a directory: {path}")
    if path.name != ".ases" and not path.name.endswith(".ases") and not (path / OUTPUT_MARKER).exists():
        raise ValueError(f"Refusing to remove unrecognized ASES output directory: {path}")
    shutil.rmtree(path)
    return True

def scan_project(root: Path, out: Path | None = None, source_uri: str | None = None) -> dict:
    root = root.resolve()
    out = (out or root / ".ases").resolve()
    if out.exists() and (out.name == ".ases" or out.name.endswith(".ases") or (out / OUTPUT_MARKER).exists()):
        clean_output(out)
    docs = out / "docs"
    docs.mkdir(parents=True, exist_ok=True)
    (out / OUTPUT_MARKER).write_text("ASES generated output. Safe to remove.\n", encoding="utf-8")

    inventory = scan_filesystem(root)
    graph = FactGraph()
    for scanner in (scan_java, scan_typescript, scan_python, scan_frontend):
        graph.merge(scanner(root))
    recover_controls(root, graph)
    enrich_traceability(graph)

    model = build_semantic_model(root.name, inventory, graph, root)
    if source_uri:
        model["project"]["source_uri"] = source_uri
    graph_dict = graph.to_dict()

    # Schema path is resolved relative to installed package layout when available.
    candidate = Path(__file__).resolve().parents[2] / "schemas" / "semantic-model.schema.json"
    validation = validate_model(model, candidate if candidate.exists() else None)
    if "semantic_quality" in model:
        model["semantic_quality"]["schema_status"] = validation["status"]
    manifest = build_manifest(inventory, model, graph_dict)
    sig = doc_signature(manifest)

    def dump_yaml(value):
        return yaml.safe_dump(value, sort_keys=False, allow_unicode=True)

    outputs = {
        out / "inventory.yaml": dump_yaml(inventory),
        out / "fact-graph.json": json.dumps(graph_dict, indent=2),
        out / "semantic-model.yaml": dump_yaml(model),
        out / "semantic-quality.json": json.dumps(model.get("semantic_quality", {}), indent=2),
        out / "manifest.json": json.dumps(manifest, indent=2),
        out / "validation.json": json.dumps(validation, indent=2),
        out / "consumer-context.json": json.dumps(generic_context(model), indent=2),
        out / "scanner-findings.json": json.dumps(scanner_findings(model), indent=2),
        # Signed (doc_signature): a consumer can tell these five are fully regenerated from the
        # current project state, and compare the embedded fingerprint against a fresh manifest.json
        # to decide if they are stale, instead of guessing from a file's mtime.
        docs / "SYSTEM-OVERVIEW.md": sig + system_overview(model, inventory),
        docs / "RAD.md": sig + recovered_rad(model),
        docs / "SDD.md": sig + recovered_sdd(model),
        docs / "ODD.md": sig + recovered_odd(model, graph_dict),
        docs / "TESTING.md": sig + testing_baseline(model),
        docs / "TRACEABILITY.yaml": dump_yaml({"trace_links": model["trace_links"]}),
        docs / "CONTROLS.yaml": dump_yaml({"controls": model.get("controls", [])}),
        docs / "QUALITY.md": quality_report(model),
    }
    for path, content in outputs.items():
        path.write_text(content, encoding="utf-8")

    return {
        "inventory": inventory,
        "graph": graph_dict,
        "semantic_model": model,
        "manifest": manifest,
        "validation": validation,
        "output": str(out),
    }
