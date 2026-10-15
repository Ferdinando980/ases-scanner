# ASES Agent Contract v0.3

You are operating under the ASES software-engineering standard.

Read `.ases/STANDARD.md`, `.ases/GATES.md`, and `.ases/orchestrator/TASK-ROUTER.md` before substantial coding work.

## Mandatory behavior

1. Understand the real code path before editing. Search callers/dependencies and relevant tests first.
2. Classify the task as LEAN, STANDARD, or FORMAL.
3. Use only the skills required by the router; do not produce process artifacts for their own sake.
4. Run the Simplicity Gate before the Pattern Gate.
5. Prefer reuse, stdlib/native/framework capability, and the smallest correct diff.
6. Never add a design pattern merely because one can be named.
7. Never add speculative abstractions without concrete evidence.
8. Do not simplify away security, validation, accessibility, data-loss prevention, correctness, or explicit requirements.
9. Update documentation and traceability only where meaning changed.
10. Test the changed behavior and run relevant regression tests.
11. Do not claim completion while known material contradictions or test failures remain.

## Skill routing

Use `.ases/orchestrator/TASK-ROUTER.md`.

Available skills:

- requirements-auditor
- impact-analyzer
- simplicity-gate
- pattern-scout
- system-designer
- object-designer
- test-designer
- traceability-keeper
- consistency-auditor

## Output discipline

For ordinary coding tasks, keep process commentary short. Report:

- what changed;
- tests/checks run;
- any design/documentation decisions that matter;
- unresolved risk/incident if present.

Do not dump internal checklists unless asked.


## Brownfield bootstrap rule

If documentation is absent, incomplete, stale, or contradictory:
1. do not fail merely because docs are missing;
2. enter BROWNFIELD-UNDOCUMENTED mode;
3. recover evidence before editing architecture-level behavior;
4. distinguish CONFIRMED / OBSERVED / INFERRED / UNKNOWN / CONFLICTING;
5. generate only useful baseline documentation;
6. transition to normal documented-brownfield workflow afterward.

Never present recovered implementation behavior as original stakeholder intent without confirmation.
