from __future__ import annotations
from pathlib import Path
import yaml, json

def load_model(path: Path) -> dict:
    if path.is_dir():
        path = path / "semantic-model.yaml"
    return yaml.safe_load(path.read_text(encoding="utf-8"))

def generic_context(model: dict) -> dict:
    return {
        "schema":"ases-consumer-context/1.3",
        "project":model.get("project",{}),
        "actors":model.get("actors",[]),
        "behaviors":model.get("behaviors",[]),
        "components":model.get("components",[]),
        "interfaces":model.get("interfaces",[]),
        "assets":model.get("assets",[]),
        "frontend":model.get("frontend",{}),
        "trust_boundaries":model.get("trust_boundaries",[]),
        "controls":model.get("controls",[]),
        "sessions":model.get("sessions",[]),
        "documentation_artifacts":model.get("documentation_artifacts",[]),
        "source_classification":model.get("source_classification",{}),
        "pattern_findings":model.get("pattern_findings",[]),
        "conformance_findings":model.get("conformance_findings",[]),
        "frontend_findings":model.get("frontend_findings",[]),
        "cross_boundary_findings":model.get("cross_boundary_findings",[]),
        "architecture_patterns":model.get("architecture_patterns",[]),
        "pattern_candidates":model.get("pattern_candidates",[]),
        "pattern_opportunities":model.get("pattern_opportunities",[]),
        "pattern_hints":model.get("pattern_hints",[]),
        "semantic_quality":model.get("semantic_quality",{}),
        "claim_states":model.get("claim_states",[]),
        "claims":model.get("claims",[]),
        "assumptions":model.get("assumptions",[]),
        "tests":model.get("tests",[]),
        "trace_links":model.get("trace_links",[]),
        "conflicts":model.get("conflicts",[]),
        "unknowns":model.get("unknowns",[]),
    }

def export_json(model_path: Path, out: Path):
    data = generic_context(load_model(model_path))
    out.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return data
