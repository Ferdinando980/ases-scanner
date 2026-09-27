<p align="center">🔎</p>

<h1 align="center">ASES</h1>

<p align="center">Architecture &amp; Software Evidence Scanner — reconstructing what a codebase actually does before recommending what it should become.</p>

<p align="center"><b>English</b> · <a href="README.it.md">Italiano</a></p>

![ASES evidence pipeline](docs/images/ases-pipeline.svg)

## Why this exists

Architecture tools often start at the wrong end. They recognise a class name, match a pattern and jump straight to a recommendation. On a brownfield repository that produces confident diagrams of generated code, "Factory" findings for one-off constructors and refactoring advice aimed at vendored JavaScript.

I built ASES to make the order explicit: classify the source, collect facts, preserve counter-evidence, then infer. A finding is useful only when another person can see where it came from, how strong it is and what would contradict it.

ASES scans Java, Python, TypeScript and frontend projects. It reconstructs components, dependencies, routes, tests, persistence and observable architectural boundaries, then exports both readable documentation and a tool-neutral semantic model. Lantern can consume the scanner output, but the engine does not depend on Lantern.

## What makes the output different

Every claim has an epistemic state:

- `OBSERVED` for direct evidence;
- `INFERRED` for a conclusion supported by multiple observations;
- `OPPORTUNITY` for a change justified by a concrete smell;
- `HINT` for a weak, non-actionable signal;
- `UNKNOWN` or `CONTRADICTED` when the evidence is incomplete or conflicts;
- `SUPPRESSED` for an accepted finding that must remain auditable.

Stable fingerprints let two scans distinguish `NEW`, `RESOLVED`, `CHANGED` and `UNCHANGED` findings even when line numbers move. Counter-evidence, assumptions, source role and analysis coverage travel with the finding instead of disappearing behind a confidence score.

![ASES output contract](docs/images/ases-output.svg)

## Source hygiene before architecture

Before interpreting a file, ASES classifies it as owned source, test, generated output, vendored code, tooling, documentation or build artifact. Generated reports, Maven wrappers, minified libraries and JaCoCo/Javadoc output can be inventoried, but they do not get to invent the architecture of the application.

That rule came from testing against real repositories. One benchmark exposed noise from bundled and generated files; another showed that conservative detection still needed to recognise DAO/Repository, `*ServiceImpl`, layered structures and a real external API adapter. The regressions remain as executable fixtures.

## Supported analysis

- repository inventory and entry points;
- components, controllers, services, repositories/DAO and models;
- routes, behaviours, tests, persistence and dependency relations;
- Layered Architecture and MVC evidence;
- application and design patterns with explicit levels;
- architecture conformance and erosion against the architecture ASES first observed;
- frontend components, state/API layers and frontend ↔ backend contracts;
- baseline comparison, suppression and safe output cleanup.

ASES does not impose a target architecture and does not treat every anomaly as a vulnerability. It exports evidence that a security, documentation or maintenance tool can interpret in its own context.

## Install and scan

Requirements: Python 3.11 or newer.

```sh
cd runtime
python -m pip install -e ".[test]"
python -m pytest -q

ases scan https://github.com/OWNER/REPOSITORY
```

Compare a later scan with a baseline:

```sh
ases scan https://github.com/OWNER/REPOSITORY --baseline path/to/previous.ases
ases diff previous.ases current.ases
```

The main output directory contains `semantic-model.yaml`, `fact-graph.json`, `consumer-context.json`, `scanner-findings.json`, validation/quality reports and recovered documentation. `scanner-findings.json` is the stable feed intended for consumers.

## Status

ASES is an independent, actively developed scanner. Version 1.7 added source-role classification and frontend/cross-boundary analysis. It is being validated against additional real repositories, with precision prioritised over a large finding count. Zero speculative opportunities is a valid result.

## License

Copyright © 2026 Ferdinando Gregorio Fernandez. All rights reserved. The source is visible for portfolio evaluation; reuse, redistribution and derivative works are not permitted. See [LICENSE](LICENSE).
