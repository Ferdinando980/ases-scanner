"""Evidence-aware changes between two ASES consumer snapshots.

This is an inventory delta, not an assertion that a change is insecure.
"""
from __future__ import annotations

import json
from pathlib import Path
import re


DIMENSIONS = (
    "behaviors", "components", "interfaces", "data_stores", "external_systems",
    "trust_boundaries", "controls", "sessions", "sensitive_paths", "frontend_findings",
    "cross_boundary_findings", "claims",
)


def load_context(path: Path) -> dict:
    if path.is_dir():
        path = path / "consumer-context.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if not str(data.get("schema", "")).startswith("ases-consumer-context/"):
        raise ValueError(f"Not an ASES consumer context: {path}")
    return data


def _key(row: dict) -> str | None:
    return row.get("fingerprint") or row.get("id")


def _meaning(value):
    if isinstance(value, dict):
        return {k: _meaning(v) for k, v in value.items()
                if k not in {"generated_at", "project_fingerprint", "evidence_strength"}}
    if isinstance(value, list):
        return [_meaning(v) for v in value]
    if isinstance(value, str):
        return re.sub(r":\d+$", "", value)
    return value


def semantic_diff(before: dict, after: dict) -> dict:
    dimensions = {}
    totals = {"added": 0, "removed": 0, "changed": 0}
    for dim in DIMENSIONS:
        old = {_key(row): row for row in before.get(dim, []) if isinstance(row, dict) and _key(row)}
        new = {_key(row): row for row in after.get(dim, []) if isinstance(row, dict) and _key(row)}
        added = sorted(new.keys() - old.keys())
        removed = sorted(old.keys() - new.keys())
        changed = sorted(key for key in old.keys() & new.keys() if _meaning(old[key]) != _meaning(new[key]))
        if added or removed or changed:
            dimensions[dim] = {
                "added": [new[key] for key in added],
                "removed": [old[key] for key in removed],
                "changed": [{"before": old[key], "after": new[key]} for key in changed],
            }
            totals["added"] += len(added)
            totals["removed"] += len(removed)
            totals["changed"] += len(changed)
    return {
        "schema": "ases-semantic-diff/1.0",
        "before_fingerprint": before.get("project_fingerprint"),
        "after_fingerprint": after.get("project_fingerprint"),
        "summary": totals,
        "dimensions": dimensions,
        "interpretation": "Inventory changes only; changed evidence is not a security verdict.",
    }
