# ASES Runtime v1.8

```bash
python -m pip install -e ".[test]"
pytest -q
ases scan <local-path-or-git-url>
ases scan-site https://example.org --max-pages 5
ases scan <project> --out current.ases --baseline previous.ases
ases semantic-diff previous.ases current.ases
```

`scan-site` fetches only public HTML pages from the same origin, obeys `robots.txt`, and never submits forms or executes JavaScript. It records sampled pages, form actions, script references, and cautious framework hints in `site-observations.json` and the existing semantic/consumer/scanner reports. For a trusted local test server, pass `--allow-local`. Source architecture, client-rendered routes, and frontend/backend contracts remain `NOT_OBSERVED` in this mode. Use `ases scan` on the repository to recover those.

Repeated scans refresh the same ASES output directory. Use `ases clean <output.ases>` or `ases clean --all` for explicit cleanup.

When a baseline includes `consumer-context.json`, the scan also writes `semantic-diff.json`.
It reports changed recovered entities and paths, not security verdicts. `docs/SUMMARY.md` is a
short review aid; the detailed RAD/SDD/ODD remain evidence-based reconstructions. A document
fingerprint matches its scan manifest, but does not by itself prove the current source is unchanged.

Pattern analysis is precision-first. `scanner-findings.json.findings` contains observed/actionable pattern results; weak signals are isolated in `scanner-findings.json.hints`.
