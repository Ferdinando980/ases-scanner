from __future__ import annotations

import json
from pathlib import Path
import re


def load_findings(path: Path) -> dict:
    if path.is_dir():
        path = path / "scanner-findings.json"
    return json.loads(path.read_text(encoding="utf-8"))


def diff_findings(before: dict, after: dict) -> dict:
    def keyed(payload):
        rows = payload.get("findings", []) + payload.get("hints", []) + payload.get("suppressed", [])
        return {r.get("fingerprint") or r.get("id"): r for r in rows}

    old, new = keyed(before), keyed(after)
    added_keys = sorted(new.keys() - old.keys())
    removed_keys = sorted(old.keys() - new.keys())
    common = old.keys() & new.keys()
    changed = sorted(k for k in common if _meaning(old[k]) != _meaning(new[k]))
    unchanged = sorted(common - set(changed))
    return {
        "schema": "ases-finding-diff/1.0",
        "summary": {
            "new": len(added_keys), "resolved": len(removed_keys),
            "changed": len(changed), "unchanged": len(unchanged),
        },
        "new": [new[k] for k in added_keys],
        "resolved": [old[k] for k in removed_keys],
        "changed": [{"before": old[k], "after": new[k]} for k in changed],
        "unchanged": [new[k] for k in unchanged],
    }


def _meaning(row: dict) -> tuple:
    normalized_evidence=tuple(sorted(re.sub(r":\d+$", "", str(x)) for x in row.get("evidence", [])))
    return (
        row.get("status"), row.get("confidence"), row.get("message"),
        tuple(row.get("counter_evidence", [])), normalized_evidence,
    )
