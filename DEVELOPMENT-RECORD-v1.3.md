# ASES v1.3 Development Record

This release was developed using the ASES process itself.

## 1. Inputs

### Authoritative process
- `STANDARD.md`
- `PROCESS.md`
- `GATES.md`
- ASES skill set

### Self-hosting baseline
ASES v1.2 scanned its own runtime before modification.

Observed baseline:
- schema validation: PASS
- self scan completed without crash
- raw trace graph was substantially larger than meaningful semantic traceability

### Brownfield benchmark
The user-tested ASES v1.2 output for `Progetto-JustInTime` was preserved under:

`benchmarks/justintime-v1.2-output/`

Observed benchmark facts:
- Java + JavaScript detected
- Spring detected
- 42 production/component-like entries
- 52 HTTP behaviors
- 36 tests
- 13 controls
- 1000 raw trace links
- validation PASS

## 2. Requirements derived from evidence

### R1 — Separate fact graph from semantic traceability
Raw declarations/calls/import-like relations MUST remain in `fact-graph.json`.
`semantic-model.yaml.trace_links` MUST contain only meaningful cross-artifact trace links.

### R2 — Prevent test self-trace
A recovered test MUST NOT be linked to its own test method/class as the production target.

### R3 — Normalize route composition
A base route `/` plus child `/login` MUST produce `/login`, never `//login`.

### R4 — Discover existing project documentation
PDF/DOCX/XLSX and diagram/document formats MUST be inventoried even when their contents are not parsed.

### R5 — Separate production architecture from test code
Test classes MUST NOT appear as production architecture components.

### R6 — Improve semantic classification
DTO, Factory, State implementation, application, domain object and test-class distinctions SHOULD be recovered conservatively.

### R7 — Preserve pattern uncertainty
State-like and factory-like structures MAY become pattern candidates, but ASES MUST NOT assert GoF intent without supporting evidence.

### R8 — Classify control enforcement layer
Recovered controls SHOULD identify `CLIENT`, `SERVER`, or `UNKNOWN`.

### R9 — Recover session/authentication evidence conservatively
Session reads/writes/invalidation and login/logout route semantics MAY refine actor inference without inventing roles.

### R10 — Add semantic-quality evidence
Schema validity MUST be separated from semantic recovery quality.

## 3. Simplicity Gate

Decision: PASS.

No new CLI mode or user-facing option was introduced.

The existing pipeline was extended with focused recovery logic and regression tests rather than a new orchestration subsystem.

## 4. Pattern Gate

Decision: NO NEW FRAMEWORK PATTERN.

Existing scanner/recovery modules remain sufficient. New abstractions were not introduced solely for future extensibility.

## 5. Implementation

Implemented:
- semantic traceability extraction;
- test self-link prevention;
- route normalization;
- rich document artifact discovery;
- production/test separation;
- DTO/factory/state/application/domain classification;
- client/server control layers;
- session evidence;
- refined actor inference;
- persistence logical boundary;
- State and simple-factory candidates;
- semantic quality metrics;
- benchmark-derived regression fixture.

## 6. Verification

The release is accepted only if:
- the full test suite passes;
- selfcheck passes;
- benchmark regression tests pass;
- semantic model validation passes;
- semantic trace links are fewer than raw fact edges in the benchmark fixture;
- no test verifies itself.
