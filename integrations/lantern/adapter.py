"""Optional example adapter. It is not imported by ASES core."""
from __future__ import annotations
import json, sys
from pathlib import Path

def adapt(generic_context: dict) -> dict:
    return {
        "schema":"lantern-semantic-context/1",
        "project":generic_context.get("project",{}),
        "attack_surface":{
            "behaviors":generic_context.get("behaviors",[]),
            "trust_boundaries":generic_context.get("trust_boundaries",[]),
            "assets":generic_context.get("assets",[]),
        },
        "observed_controls":generic_context.get("controls",[]),
        "assumptions":generic_context.get("assumptions",[]),
        "trace_links":generic_context.get("trace_links",[]),
        "uncertainty":{
            "conflicts":generic_context.get("conflicts",[]),
            "unknowns":generic_context.get("unknowns",[]),
        }
    }

if __name__ == "__main__":
    src = Path(sys.argv[1])
    out = Path(sys.argv[2])
    out.write_text(json.dumps(adapt(json.loads(src.read_text(encoding="utf-8"))), indent=2), encoding="utf-8")
