---
name: logic-development-toolkit
description: Prevent incomplete or contradictory application behavior by modeling states, transitions, dependencies, invariants, and edge cases before and during implementation. Use for feature development, behavior changes, refactors, UI state changes, and any task where missing logic could cause repeated fixes. Do not use as a product-specification or repository-stewardship workflow.
---

# Logic Development Toolkit

Use this toolkit to make behavior complete before code is written and to keep changes consistent with existing behavior. The goal is not to produce more prose; it is to expose the logic that a feature depends on and turn important rules into checks.

## Persistent conversation mode

When this toolkit is installed in a project, treat `.logic/` as the project's durable behavioral memory. For every conversation that touches a feature, behavior, bug, refactor, UI state, API contract, or workflow:

1. Read `.logic/README.md`, `.logic/index.md`, and the relevant feature record before proposing implementation.
2. Match the user's request to an existing feature, state, invariant, decision, or pattern. Do not assume a new conversation means a new logic context.
3. Summarize the existing logic that is affected, identify missing or conflicting parts, and ask focused clarification questions when an unresolved choice changes behavior.
4. During the exchange, maintain a distinction between confirmed facts, user decisions, proposed logic, and unverified assumptions.
5. Before implementation, update the relevant feature record or create one under `.logic/features/`; do not wait until the end if the conversation establishes a durable rule.
6. After implementation or a decision, append a concise session entry to `.logic/sessions/` and update `.logic/index.md` so later conversations can recover the reasoning.

This is an active protocol, not a one-time documentation task. If the memory is stale, contradictory, or missing, surface that explicitly and reconcile it with the user before silently overwriting it.

Do not store secrets, raw transcripts, personal data, or every conversational detail. Store only durable behavioral knowledge and links to code/tests.

## Cross-project logic reuse

When installed through `logic-toolkit`, also consult the reusable logic library. Before inventing a rule, search the library for an applicable pattern. After a feature stabilizes, scan the project's `.logic/` records for candidates that are portable across projects.

Never promote a project-specific rule automatically. A candidate must be generalized, stripped of identifiers and assumptions, linked to evidence, and reviewed for portability before entering the shared library. Keep project-specific details in `.logic/features/`; keep reusable abstractions in the library.

## Core distinction

- `spec-driven-product-toolkit` decides what product capability is requested and how delivery is gated.
- `logic-development-toolkit` discovers what must remain true for that capability to work across states, actors, surfaces, and failures.
- `product-stewardship-toolkit` evaluates the long-term health, provenance, and handoff readiness of the repository.

Do not replace a product spec with a logic map, and do not treat a clean repository as evidence that behavior is complete.

## Strict non-overlap boundary

This toolkit owns **behavioral completeness of an application change**. It does not own:

- product discovery, prioritization, roadmap, requirements authoring, acceptance criteria, release profiles, or implementation/release gates;
- repository metadata, attribution, provenance, documentation hygiene, public-release readiness, handoff readiness, or maintenance lifecycle checks;
- generic code style, security review, dependency governance, CI orchestration, or project management.

Use the other toolkits when those are the primary request. Invoke this toolkit only when the question is whether a behavior is logically complete and consistent across its possible states and effects.

### Ownership test

Ask: “What is the smallest unit being evaluated?”

- A **product requirement or delivery process** belongs to `spec-driven-product-toolkit`.
- A **behavior change and its state/effect correctness** belongs here.
- A **repository/product lifecycle or handoff condition** belongs to `product-stewardship-toolkit`.

If a task crosses boundaries, keep one owner per concern and pass artifacts between them. Do not duplicate their checklists or create a second source of truth.

## Required reasoning loop

Before editing behavior:

1. Identify the changed capability and its entry points.
2. Locate existing state, transitions, derived state, side effects, persistence, and consumers.
3. Build a behavior map: actor/action, preconditions, state change, effects, success, failure, retry, cancellation, and recovery.
4. List invariants that must hold before, during, and after each transition.
5. Trace impact to dependent UI, API, permissions, cache, events, analytics, notifications, and accessibility states.
6. Find an existing pattern to reuse before introducing a new abstraction.
7. Implement the smallest change that preserves the map.
8. Verify happy path, invalid input, boundary values, repeated action, refresh/reload, concurrency, permission changes, and partial failure as applicable.
9. Record newly discovered reusable rules in the project's logic artifacts.

If the change is too ambiguous to model, pause implementation and state the missing assumption rather than silently inventing behavior.

## Artifacts

Prefer these files under `.logic/` in the target project:

- `logic-map.md`: feature-to-behavior and dependency map.
- `state-model.md`: states, legal transitions, guards, effects, and terminal states.
- `invariants.md`: rules that must always hold, with owners and verification methods.
- `edge-cases.md`: boundary and failure matrix.
- `patterns.md`: reusable behavior patterns and anti-patterns.
- `decisions.md`: durable decisions when multiple valid logic designs exist.
- `index.md`: searchable map from features and concepts to their logic records.
- `features/<feature>.md`: durable behavior contract for one feature.
- `sessions/<date>-<topic>.md`: compact reasoning checkpoint from a conversation.
- `reusable-candidates.md`: scanner output requiring review before promotion.

Read only the artifacts relevant to the current change. Update them only when the behavior model actually changes.

## Invariant quality

An invariant must be observable and testable. Prefer:

```text
After payment succeeds, an order cannot return to unpaid.
When theme changes, every semantic surface has a readable foreground/background pair.
While a request is pending, duplicate submission cannot create duplicate mutation.
Only the owner or an authorized role can transition a resource to archived.
```

Avoid vague rules such as “the UI should feel consistent.” Attach each important invariant to a test, static check, or explicit verification command. An LLM may propose an invariant; deterministic checks provide evidence.

## UI and cross-cutting behavior

Treat visual changes as behavior changes when they affect theme, responsive layout, loading, errors, permissions, localization, or accessibility. Trace semantic tokens and dependent surfaces rather than patching one component in isolation. For a theme change, inspect background, surface, text, muted text, border, icon, focus, disabled, overlay, shadow, chart, image, and native-control variants.

## Completion standard

A logic change is complete only when:

- the affected states and legal transitions are known;
- dependent effects and failure paths are accounted for;
- important invariants have evidence;
- no existing reusable pattern was bypassed without rationale;
- the final report names unverified assumptions and residual risk.

For the conceptual model and artifact templates, read [references/logic-model.md](references/logic-model.md). For upstream provenance and exclusions, read [references/source-catalog.md](references/source-catalog.md).
