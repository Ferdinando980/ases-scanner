from __future__ import annotations

def _ev(obj):
    p = obj.get("provenance", {})
    ev = ", ".join(p.get("evidence", [])) or "none"
    return f"{p.get('state','UNKNOWN')} / {p.get('confidence','?')} / {ev}"

def system_overview(model: dict, inventory: dict) -> str:
    p = model["project"]
    lines = [
        f"# Recovered System Overview — {p['name']}",
        "",
        "> Generated from repository evidence. It describes the current implementation and does not claim original stakeholder intent.",
        "",
        "## Provenance",
        f"- ASES: {model['ases_version']}",
        f"- Entry mode: {p['entry_mode']}",
        "",
        "## Technology inventory",
    ]
    for l in inventory.get("languages", []):
        lines.append(f"- {l['name']}: {l['files']} source files")
    for b in inventory.get("build_tools", []):
        lines.append(f"- Build: {b['tool']} (`{b['path']}`)")
    for f in p.get("frameworks", []):
        lines.append(f"- Framework: {f}")

    lines += ["", "## Actors"]
    for a in model.get("actors", []):
        lines.append(f"- **{a['name']}** — {_ev(a)}")
    if not model.get("actors"):
        lines.append("- None recovered.")

    lines += ["", "## Observed components"]
    for c in model.get("components", []):
        lines.append(f"- **{c['name']}** ({c['kind']}) — {_ev(c)}")

    lines += ["", "## Observed behaviors"]
    if model.get("behaviors"):
        for b in model["behaviors"]:
            flow = " → ".join(b.get("main_flow", []))
            lines.append(f"- **{b['name']}**")
            lines.append(f"  - actor: {b.get('actor')}")
            lines.append(f"  - flow: `{flow}`")
            lines.append(f"  - evidence: `{', '.join(b['provenance']['evidence'])}`")
    else:
        lines.append("- No externally meaningful behavior recovered yet.")

    lines += ["", "## Data / assets"]
    for a in model.get("assets", []):
        lines.append(f"- {a['name']} — {_ev(a)}")
    if not model.get("assets"):
        lines.append("- None recovered.")

    lines += ["", "## Trust boundaries"]
    for t in model.get("trust_boundaries", []):
        lines.append(f"- {t['name']} — {_ev(t)}")
    if not model.get("trust_boundaries"):
        lines.append("- None recovered.")

    lines += ["", "## Tests"]
    for t in model.get("tests", []):
        lines.append(f"- {t['name']} — {_ev(t)}")
    if not model.get("tests"):
        lines.append("- No tests recovered.")

    lines += ["", "## Assumptions / unknowns"]
    for u in model.get("assumptions", []) + model.get("unknowns", []):
        lines.append(f"- {u['statement']} [{u['provenance']['state']}]")
    return "\n".join(lines) + "\n"

def recovered_rad(model: dict) -> str:
    lines = [
        f"# Recovered RAD — {model['project']['name']}",
        "",
        "> Recovered requirements describe current observed/inferred behavior, not original stakeholder intent unless explicitly confirmed.",
        "",
        "## Actors",
    ]
    for a in model.get("actors", []):
        lines.append(f"- {a['name']} — {_ev(a)}")
    lines += ["", "## Recovered functional behavior"]
    for b in model.get("behaviors", []):
        lines.append(f"### {b['name']}")
        lines.append(f"- State: {b['provenance']['state']}")
        lines.append(f"- Actor: {b['actor']}")
        lines.append(f"- Trigger: {b['trigger']}")
        lines.append(f"- Main flow: {' → '.join(b.get('main_flow', []))}")
        lines.append(f"- Evidence: {', '.join(b['provenance']['evidence'])}")
        lines.append("")
    lines += ["## Unknown original requirements"]
    for u in model.get("unknowns", []):
        lines.append(f"- {u['statement']}")
    return "\n".join(lines) + "\n"

def recovered_sdd(model: dict) -> str:
    lines = [
        f"# Recovered SDD — {model['project']['name']}",
        "",
        "> Evidence-based reconstruction of the current implementation.",
        "",
        "## Architecture overview",
    ]
    by_kind = {}
    for c in model.get("components", []):
        by_kind.setdefault(c["kind"], []).append(c)
    for kind, items in sorted(by_kind.items()):
        lines.append(f"### {kind.title()}")
        for c in items:
            lines.append(f"- {c['name']} — {_ev(c)}")
    lines += ["", "## Persistence / data"]
    for d in model.get("data_stores", []):
        lines.append(f"- {d['name']} — {_ev(d)}")
    if not model.get("data_stores"):
        lines.append("- UNKNOWN / not recovered.")

    lines += ["", "## Trust boundaries"]
    for t in model.get("trust_boundaries", []):
        lines.append(f"- {t['name']} — {_ev(t)}")
    if not model.get("trust_boundaries"):
        lines.append("- None recovered.")

    lines += ["", "## Conflicts and unknowns"]
    for x in model.get("conflicts", []) + model.get("unknowns", []):
        lines.append(f"- {x.get('statement') or x.get('reason') or x.get('message','')}")
    return "\n".join(lines) + "\n"

def recovered_odd(model: dict, graph: dict) -> str:
    lines = [
        f"# Recovered ODD — {model['project']['name']}",
        "",
        "> Significant implementation objects recovered from code. Pattern names are not asserted without intent evidence.",
        "",
        "## Classes / interfaces / components",
    ]
    relevant = model.get("components", []) + model.get("interfaces", []) + model.get("data_stores", [])
    for c in relevant:
        lines.append(f"### {c['name']}")
        lines.append(f"- Kind: {c['kind']}")
        lines.append(f"- Provenance: {_ev(c)}")
        lines.append("")
    lines += ["## Pattern analysis"]
    patterns = model.get("pattern_findings", [])
    visible = [p for p in patterns if p.get("status") != "HINT"]
    if visible:
        for p in visible:
            lines.append(f"- **{p['pattern']}** ({p['category']}) — {p['status']} / {p['confidence']} confidence")
            lines.append(f"  - Rule: `{p.get('rule_id', '')}`")
            lines.append(f"  - Reason: {p['reason']}")
            lines.append(f"  - Evidence: {', '.join(p.get('evidence', []))}")
            if p.get('guidance'):
                lines.append(f"  - Guardrail: {p['guidance']}")
    else:
        lines.append("- No evidence-backed pattern observation or opportunity recovered.")
    hints = model.get("pattern_hints", [])
    lines += ["", "## Pattern hints (suppressed from the main scanner feed)"]
    if hints:
        for p in hints:
            lines.append(f"- **{p['pattern']}** ({p['category']}) — low-confidence hint")
            lines.append(f"  - Reason: {p['reason']}")
    else:
        lines.append("- No suppressed pattern hints.")
    lines += [
        "",
        "## Unknown rationale",
        "- Historical design rationale is UNKNOWN unless documented or confirmed.",
    ]
    return "\n".join(lines) + "\n"

def testing_baseline(model: dict) -> str:
    lines = [
        f"# Testing Baseline — {model['project']['name']}",
        "",
        "## Recovered tests",
    ]
    if model.get("tests"):
        for t in model["tests"]:
            lines.append(f"- {t['name']} — {_ev(t)}")
    else:
        lines.append("- None recovered.")
    lines += [
        "",
        "## Coverage interpretation",
        "- Presence of a test is OBSERVED evidence only; semantic coverage is not assumed unless linked explicitly.",
    ]
    return "\n".join(lines) + "\n"


def quality_report(model: dict) -> str:
    q=model.get("semantic_quality",{})
    lines=[
        f"# Semantic Quality — {model['project']['name']}",
        "",
        f"- Schema validation: {q.get('schema_status','UNKNOWN')}",
        f"- Evidence coverage: {q.get('evidence_coverage',{}).get('supported',0)}/{q.get('evidence_coverage',{}).get('total',0)}",
        f"- Route-handler coverage: {q.get('route_handler_coverage',{}).get('covered',0)}/{q.get('route_handler_coverage',{}).get('total',0)}",
        f"- Test-target coverage: {q.get('test_target_coverage',{}).get('linked_tests',0)}/{q.get('test_target_coverage',{}).get('total_tests',0)}",
        f"- Semantic trace links: {q.get('semantic_trace_links',0)}",
        f"- Raw fact edges: {q.get('raw_fact_edges',0)}",
        f"- Trace noise reduction: {q.get('trace_noise_reduction',0)}",
        f"- Unsupported inference count: {q.get('unsupported_inference_count',0)}",
        f"- Documentation artifacts discovered: {q.get('documentation_artifacts_discovered',0)}",
        "",
        "## Control layers",
    ]
    for layer,count in q.get("control_layers",{}).items():
        lines.append(f"- {layer}: {count}")
    return "\n".join(lines)+"\n"
