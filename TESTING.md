# ASES v1.6 Test Guide

## 1. Internal suite

```bash
cd runtime
python -m pip install -e ".[test]"
python -m pytest -q
```

## 2. Real repository scan

```bash
ases scan /path/to/repository
# or
ases scan https://github.com/LimeMoss/Progetto-JustInTime
```

Review:
- `validation.json` is `PASS`;
- `manifest.json` records a deterministic source fingerprint;
- `fact-graph.json` contains technical observations;
- `semantic-model.yaml` contains evidence-backed semantic recovery;
- `scanner-findings.json.findings` contains OBSERVED/OPPORTUNITY results only;
- `scanner-findings.json.hints` contains low-confidence pattern hints;
- `docs/ODD.md` separates pattern observations/opportunities from hints.

## 3. Pattern precision regressions

The suite explicitly checks that:
- test code does not generate pattern opportunities;
- exceptions, DTOs/responses and common value/framework types do not trigger Factory;
- three-way generic variant dispatch is a HINT, not an actionable Strategy opportunity;
- Facade requires repeated graph-level subsystem dependencies, not receiver count;
- DOM APIs and local variables do not trigger Facade;
- Adapter requires both shape translation and boundary evidence for an OPPORTUNITY;
- weak Adapter/Template/Decorator evidence is downgraded to HINT;
- architectural observations are recovered from actual dependency structure.

## 4. Consumer integration

```bash
ases export /path/to/repository/.ases --out context.json
```

The export uses `ases-consumer-context/1.2`. Scanner ingestion uses `ases-scanner-findings/1.2`.

## 5. Repeatability and cleanup

Repeated scans refresh the same generated output directory.

```bash
ases clean ./my-repo.ases
ases clean --all
```

Cleanup only targets recognized ASES output directories.

## Acceptance criteria

- all internal tests pass;
- Java, TypeScript and Python fixtures scan;
- semantic model validation passes;
- scanner and consumer JSON validate against their schemas;
- pattern precision regressions pass;
- source fingerprint remains deterministic;
- malformed-source resilience tests pass.
