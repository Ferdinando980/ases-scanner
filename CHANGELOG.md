# ASES Changelog

## 1.7.1
- Regenerable docs (SYSTEM-OVERVIEW.md, RAD.md, SDD.md, ODD.md, TESTING.md) now carry an
  `<!-- ases:doc fingerprint=... ases_version=... -->` signature so an external consumer (e.g.
  Lantern) can tell whether a doc still matches the current project state, without guessing from a
  file's mtime. Data files (TRACEABILITY.yaml, CONTROLS.yaml, QUALITY.md) stay unsigned.
- 37 tests pass.

## 1.7.0
- Added source-role classification before analysis: OWNED_SOURCE, TEST, GENERATED, VENDORED, TOOLING, DOCUMENTATION, BUILD_ARTIFACT.
- Generated JaCoCo/Javadoc output, minified/vendor libraries and wrapper/tooling code no longer drive findings.
- Tightened Factory to branch-local alternative-product selection and Facade to repeated active subsystem calls.
- Added DAO/ServiceImpl architecture recovery and observed external Adapter detection.
- Added frontend component/template/API-service/store recovery and frontend conformance.
- Added conservative frontend↔backend route-contract correlation.
- Scanner contract 1.3 adds surface, actionability, entity, source_role and source classification for Lantern.
- Consumer contract 1.3 adds source classification, frontend inventory/findings and cross-boundary findings.
- 34 tests pass.

## 1.6.0
- Added unified claim states: OBSERVED, INFERRED, OPPORTUNITY, HINT, UNKNOWN, CONTRADICTED, and SUPPRESSED.
- Added stable semantic fingerprints for scanner findings.
- Added counter-evidence, assumptions, evidence-strength metadata, and explicit analysis coverage.
- Added architecture conformance/erosion findings derived only from already-observed architecture.
- Added conceptual pattern levels: ARCHITECTURE, APPLICATION_PATTERN, GOF, and FRAMEWORK_IDIOM.
- Added `.asesignore` rule suppression while preserving suppressed findings in scanner output.
- Added `ases diff` and `ases scan --baseline` with NEW/RESOLVED/CHANGED/UNCHANGED semantics.
- Upgraded scanner contract to 1.2 and consumer contract to 1.2.
- Expanded regression suite for fingerprints, suppression, diffing, and architecture conformance.

## 1.5.0
- Rebuilt pattern analysis around explicit evidence rules and `OBSERVED / OPPORTUNITY / HINT` states.
- Added architectural observations for Layered Architecture, MVC, Repository, and Service Layer.
- Added precision-first rules for Factory, State, Strategy, Command, Observer, Chain of Responsibility, Template Method, Adapter, Facade, Decorator, and Proxy.
- Excluded test code from pattern opportunities.
- Filtered Factory noise from exceptions, DTO/request/response/value types and common stdlib/framework wrappers.
- Replaced receiver-count Facade detection with project-level dependency overlap.
- Split weak hints from actionable scanner findings for Lantern/downstream consumers.
- Added rule IDs, positive/negative signals, scope, evidence, confidence, and guardrails to pattern findings.
- Updated scanner/consumer contracts to v1.1.
- Fixed Java field scanning for one-character type names.

## 1.4.1
- Scan outputs are refreshed in place instead of accumulating stale generated files.
- Added `ases clean <path>` and `ases clean --all` for safe removal of generated ASES output directories.
- Added `.ases-output` marker to custom output directories so cleanup never targets arbitrary folders.
- Fixed package `__version__` consistency.

# Changelog

## 1.3.0 — Self-Hosted Benchmark Release
- Developed through ASES requirements/impact/simplicity/pattern/test flow.
- Separated raw fact graph from semantic traceability.
- Fixed test-to-self traceability.
- Fixed route `//` normalization.
- Added discovery of PDF/DOCX/XLSX/diagram documentation.
- Excluded test classes from production component model.
- Added conservative DTO/factory/state/application/domain classification.
- Added control enforcement layers.
- Added session-operation recovery and conservative actor refinement.
- Added persistence logical boundary.
- Added State-specific and Simple Factory/Factory-idiom candidates.
- Added semantic quality metrics and quality report.
- Added real-benchmark-derived regression fixture.

## 1.2.0
- Added direct Git URL scanning.
