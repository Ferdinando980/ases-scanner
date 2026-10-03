"""Evaluate declared scanner claims against a small, explicit local oracle.

This is a rule-quality benchmark, not a claim that all architecture is detectable.
Rules absent from an oracle case are unassessed, rather than negative examples.
"""

from __future__ import annotations


FINDING_GROUPS = ("pattern_findings", "frontend_findings", "cross_boundary_findings")


def evaluate_case(model: dict, oracle: dict) -> dict:
    expected = set(oracle["present"])
    negative = set(oracle["absent"])
    if expected & negative:
        raise ValueError("The same finding cannot be both present and absent")
    observed = {
        f"{finding['rule_id']}:{finding['status']}"
        for group in FINDING_GROUPS
        for finding in model.get(group, [])
    }
    assessed = expected | negative
    tp = sorted(expected & observed)
    fn = sorted(expected - observed)
    fp = sorted(negative & observed)
    tn = sorted(negative - observed)
    unassessed = sorted(observed - assessed)
    return {
        "true_positive": tp,
        "false_negative": fn,
        "false_positive": fp,
        "true_negative": tn,
        "unassessed_findings": unassessed,
        "unsupported_claims": list(oracle.get("unsupported", [])),
    }


def summarize(cases: dict[str, dict]) -> dict:
    totals = {
        key: sum(len(case[key]) for case in cases.values())
        for key in ("true_positive", "false_negative", "false_positive", "true_negative")
    }
    tp, fp, fn = totals["true_positive"], totals["false_positive"], totals["false_negative"]
    totals["precision"] = tp / (tp + fp) if tp + fp else None
    totals["recall"] = tp / (tp + fn) if tp + fn else None
    totals["cases"] = cases
    return totals
