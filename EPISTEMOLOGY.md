# ASES Epistemology — v1.7

ASES does not treat every signal as a finding. Every claim must expose what supports it, what weakens it, and what remains assumed.

## Claim states

- `OBSERVED` — direct repository evidence supports the claim.
- `INFERRED` — multiple observations support a derived claim, but it is not directly encoded.
- `OPPORTUNITY` — a concrete smell and sufficient evidence support a refactoring suggestion.
- `HINT` — weak signal; normally hidden from the default scanner feed.
- `UNKNOWN` — evidence is insufficient.
- `CONTRADICTED` — evidence conflicts with an already observed architectural claim.
- `SUPPRESSED` — a valid finding was explicitly accepted by project policy; it remains traceable.

## Evidence rules

Every scanner-facing finding carries a stable fingerprint, rule ID, confidence, evidence, counter-evidence, assumptions, and guidance. Line-number-only movement must not create a new finding identity.

Architecture conformance is derived from the architecture ASES first observes. ASES never imposes Layered Architecture, MVC, or another pattern on a repository that has not supplied evidence for it.

## Coverage

A `PASS` validates ASES output consistency; it does not mean the whole system was verified. `analysis_coverage` records what static analysis inspected and what remains unknown or unobserved (runtime behavior, deployment topology, external-system behavior).

## Suppression

Create `.asesignore` in the scanned repository:

```text
conformance.layered_dependency | intentional legacy shortcut
opportunity.strategy_dispatch | stable three-way dispatch; abstraction not justified
```

Suppressed findings move to `scanner-findings.json.suppressed`; they are not deleted from evidence history.


## Source ownership precedes inference

No inference is stronger than its source. Before facts enter architecture/pattern rules, ASES classifies their files. Generated documentation, vendored/minified libraries, build/tooling code and ordinary documentation cannot be promoted into production architecture claims. This gate applies equally to backend and frontend analysis.
