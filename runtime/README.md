# ASES Runtime v1.7

```bash
python -m pip install -e ".[test]"
pytest -q
ases scan <local-path-or-git-url>
```

Repeated scans refresh the same ASES output directory. Use `ases clean <output.ases>` or `ases clean --all` for explicit cleanup.

Pattern analysis is precision-first. `scanner-findings.json.findings` contains observed/actionable pattern results; weak signals are isolated in `scanner-findings.json.hints`.
