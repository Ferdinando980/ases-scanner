# ASES Consumer Contract v1.5

ASES remains standalone. Lantern and other tools consume generic output; ASES core contains no Lantern-specific logic.

## Primary files

- `scanner-findings.json` (`ases-scanner-findings/1.3`) — normalized scanner feed.
- `consumer-context.json` (`ases-consumer-context/1.5`) — full recovered semantic context.
- `semantic-model.yaml` — canonical ASES model.
- `findings-diff.json` (`ases-finding-diff/1.0`) — optional baseline delta.

## v1.5 changes (additive over v1.4)

`external_systems` is now real, not the always-empty placeholder v1.4 deliberately left out of
the contract. `recover_external_systems` (`runtime/ases/recovery/semantic.py`) matches each
node's raw import strings (`node.metadata["imports"]`, already collected by the Java/
TypeScript/Python scanners) against a **fixed allowlist** of well-known third-party API/service
clients (OpenAI, Anthropic, Stripe, AWS SDK, Supabase, Twilio, SendGrid, Firebase). Every entry
is `provenance.state: "INFERRED"`, never `"OBSERVED"`: an import proves the client/SDK is
present in the code, not that it is actually called, which endpoint it hits, or what data it
sends — `provenance.assumptions` says this explicitly on every entry.

Generic database drivers (`pg`, `mongodb`, JDBC drivers, ...) are **not** in the allowlist on
purpose: they would overlap with `data_stores` (recovered separately from `entity` nodes),
which already covers "the app's own data", a different concept from "a third-party system".

This is a starting allowlist, not exhaustive — a client library not on the list simply produces
no `external_systems` entry for it; that is "not detected", never "confirmed absent".

## v1.4 changes (additive over v1.3)

`consumer-context.json` gained four top-level keys. A v1.3-only consumer can ignore all of
them and keep working unmodified; nothing from v1.3 was removed or reshaped.

- `ases_version` — the ASES release that produced this file (`ases.__version__`), so a
  consumer can tell which behavior/bug set generated the data without shelling out to
  `ases --version`.
- `generated_at` — ISO 8601 UTC timestamp of this export.
- `project_fingerprint` — the same fingerprint as `manifest.json`, when a manifest was
  available at export time (the full pipeline always produces one; a standalone `ases export`
  run against a bare `semantic-model.yaml` may not, in which case this is `null` — a consumer
  must treat `null` as "freshness unknown", never as "unchanged" or "stale").
- `data_stores` — entities ASES's graph classified as data-holding (`kind: "entity"`),
  excluding test code. Same shape as `components`/`interfaces` (`id`, `name`, `kind`,
  `description`, `provenance`). This says an entity exists and how it was found — it is not a
  personal-data or sensitivity classification; a consumer must not infer GDPR/PII status from
  presence alone.

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

## Two distinct epistemic vocabularies — do not conflate them

ASES uses two separate state enums; a consumer that merges them into one "confidence level"
will misread the model.

- `evidence_states` (`CONFIRMED`, `OBSERVED`, `INFERRED`, `UNKNOWN`, `CONFLICTING`) — attached
  to individual pieces of provenance (a node/behavior's evidence), i.e. "how was this single
  fact established".
- `claim_states` (`OBSERVED`, `INFERRED`, `OPPORTUNITY`, `HINT`, `UNKNOWN`, `CONTRADICTED`,
  `SUPPRESSED`) — the `status` on `claims`, `pattern_findings`, `conformance_findings`,
  `frontend_findings`, `cross_boundary_findings`, i.e. "what ASES concludes about a pattern or
  architectural expectation, and how it stands relative to counter-evidence".

They overlap in name (`OBSERVED`, `INFERRED`, `UNKNOWN`) but are not the same axis: a finding
can be `claim_states: CONTRADICTED` while every individual piece of evidence behind it is
`evidence_states: CONFIRMED` (the evidence is solid, the architectural expectation it
contradicts is what's in question) — collapsing the two into one scale loses that distinction.

## Architecture conformance

`CONTRADICTED` findings mean code evidence conflicts with an architecture ASES first observed from the same project. They are not universal style rules. This distinction should remain visible in Lantern.

## Coverage

`coverage` explicitly records analysis limitations. A validation `PASS` is schema/model consistency, not proof that runtime behavior, deployment, or external systems were verified.


## Source ownership and frontend

`source_classification` reports repository roles before inference. `GENERATED`, `VENDORED`, `TOOLING`, `DOCUMENTATION`, and `BUILD_ARTIFACT` files do not drive production design-pattern opportunities.

`frontend` in consumer context contains recovered owned components, templates, API/service modules, stores, and literal API calls. `frontend_findings` and `cross_boundary_findings` use the same epistemic states/fingerprints as backend findings, so Lantern should ingest them through the same pipeline rather than a frontend-specific parser.
