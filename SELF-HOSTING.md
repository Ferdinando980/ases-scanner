# ASES Self-Hosting Policy

ASES uses ASES as one of its own validation targets.

Every release SHOULD:

1. scan its own runtime;
2. recover a semantic model without crashing;
3. verify expected scanner/recovery/export capabilities;
4. run fixture-based regression tests;
5. audit its stored baseline for drift when a baseline is committed.

Command:

```bash
cd runtime
python -m ases selfcheck ..
```

Self-hosting is a validation mechanism, not proof of correctness. External repositories and fixtures remain necessary because a tool can share blind spots with its own test corpus.
