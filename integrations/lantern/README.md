# Optional Lantern Adapter

ASES does not depend on Lantern.

Lantern can consume the generic ASES consumer context and map it into its own security-analysis model.

Recommended flow:

```text
repository
  ↓
ASES
  ↓
ases-consumer-context.json
  ↓
Lantern adapter
  ↓
security hypotheses / scanner correlation / verification
```

Useful ASES fields for Lantern include:
- actors
- behaviors
- entry points
- components
- assets
- trust boundaries
- observed controls
- assumptions
- tests
- trace links
- conflicts / unknowns

Lantern should preserve ASES provenance and keep separate:
`observed fact → inference → security hypothesis → verified finding`.

The adapter is optional and external to the ASES core.
