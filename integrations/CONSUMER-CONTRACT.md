# ASES Consumer Contract v1.3

ASES remains standalone. Lantern and other tools consume generic output; ASES core contains no Lantern-specific logic.

## Primary files

- `scanner-findings.json` (`ases-scanner-findings/1.3`) — normalized scanner feed.
- `consumer-context.json` (`ases-consumer-context/1.3`) — full recovered semantic context.
- `semantic-model.yaml` — canonical ASES model.
- `findings-diff.json` (`ases-finding-diff/1.0`) — optional baseline delta.

## Scanner feed

`findings[]` contains normal actionable/observed results. `hints[]` contains weak evidence. `suppressed[]` contains explicit accepted exceptions.

Each finding exposes:

- stable `fingerprint` and `id`;
- `rule_id`, `type`, `category`, `level`, and optional `pattern`/`subject`;
- epistemic `status` and `confidence`;
- `evidence`, `evidence_strength`, `counter_evidence`, and `assumptions`;
- location, message, signals, and guidance;
- `surface` (`backend`, `frontend`, `cross_boundary`, `project`), `actionability`, normalized `entity`, and `source_role`.

Consumers should key history on `fingerprint`, not line number or display ID.

## Baseline/diff semantics

`ases diff` and `scan --baseline` classify findings as:

- `new`
- `resolved`
- `changed`
- `unchanged`

A line-number-only move remains the same fingerprint and does not count as a semantic change.

## Architecture conformance

`CONTRADICTED` findings mean code evidence conflicts with an architecture ASES first observed from the same project. They are not universal style rules. This distinction should remain visible in Lantern.

## Coverage

`coverage` explicitly records analysis limitations. A validation `PASS` is schema/model consistency, not proof that runtime behavior, deployment, or external systems were verified.


## Source ownership and frontend

`source_classification` reports repository roles before inference. `GENERATED`, `VENDORED`, `TOOLING`, `DOCUMENTATION`, and `BUILD_ARTIFACT` files do not drive production design-pattern opportunities.

`frontend` in consumer context contains recovered owned components, templates, API/service modules, stores, and literal API calls. `frontend_findings` and `cross_boundary_findings` use the same epistemic states/fingerprints as backend findings, so Lantern should ingest them through the same pipeline rather than a frontend-specific parser.
