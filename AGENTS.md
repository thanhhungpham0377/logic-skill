# Hung Toolkit Agent Instructions

These instructions are the entrypoint for coding agents using Hung Toolkit. Apply them when the repository has been installed into a project or when working on the bundle itself.

## Purpose

Hung Toolkit coordinates three independent concerns:

- **Spec Driven:** what the product should build and how delivery is gated.
- **Logic:** whether product behavior is complete and coherent across states, transitions, effects, failures, and dependent surfaces.
- **Ops:** whether the repository is clean, attributable, maintainable, and handoff-ready.

Do not merge their checklists or let one component silently take ownership of another's decisions.

## Routing

| User request | Read first | Primary output |
|---|---|---|
| New product capability, scope, acceptance criteria, release profile | `components/Spec-Driven/` | specification and delivery context |
| Feature behavior, state, edge case, UI/API consistency, bug logic | `components/Logic/` | behavior map, state model, invariants, decisions |
| Repository cleanup, provenance, docs, maintenance, handoff | `components/Ops/` | evidence-backed ops report |
| Feature work involving more than one concern | read Spec Driven → Logic → Ops | separate artifacts with explicit ownership |

## Logic feature protocol

When a project contains `.logic/`, every development task that designs or changes product behavior must:

1. Read `.logic/README.md` and `.logic/index.md`.
2. Find the existing feature record before proposing a new model.
3. State what is already known, what changed, and what is uncertain.
4. Check states, legal/forbidden transitions, dependencies, side effects, failure/retry, persistence, authorization, and user-visible states.
5. Ask focused clarification questions when an answer changes behavior. Do not block on a cosmetic choice covered by an existing pattern.
6. Update `.logic/features/`, `.logic/invariants.md`, or `.logic/decisions.md` when durable logic changes.
7. Add a compact checkpoint under `.logic/sessions/` after a meaningful behavior decision or implementation.
8. Update `.logic/index.md` so another conversation can recover the context.

Do not store raw transcripts, secrets, or personal data. Separate confirmed facts, user decisions, proposals, and unverified assumptions.

`.logic/` is a supporting record of product behavior decisions, not a general agent memory engine, chat archive, task tracker, or multi-agent coordination system. Delegation and coordination belong to a separate tool. Spec Driven remains the owner of product scope/specification; Logic analyzes behavior completeness and consistency without replacing requirements or acceptance criteria.

## Cross-project reuse

Before creating a new cross-cutting rule, search `components/Logic/reusable-library/`. After a feature stabilizes, run:

```powershell
python components/Logic/scripts/scan_logic.py --project D:\path\to\project --write-report
```

The scanner proposes candidates only. Promote a candidate only after removing project-specific assumptions, adding a verification method, and documenting portability. Never treat a project-specific rule as a global rule automatically.

## Completion evidence

Before claiming completion, report:

- the component(s) used;
- affected states and transitions;
- important invariants and how they were checked;
- unresolved assumptions or open questions;
- files/artifacts updated;
- tests or deterministic checks run.

If the logic memory conflicts with code or a new user decision, surface the conflict and create a new decision record; do not silently rewrite history.
