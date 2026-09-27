---
name: logic-skill
description: "Analyze and preserve product feature logic: actors, states, transitions, invariants, effects, failure paths, and cross-surface consistency. Use when designing or changing application behavior to expose missing logic before implementation and verify it afterward. Does not own product specifications, repository stewardship, or multi-agent orchestration."
---

# Logic Skill

Use this toolkit to make product behavior logically complete before code is written and consistent with existing behavior afterward. The goal is not to produce more prose; it is to expose missing states, transitions, conditions, effects, and failure paths, then turn important rules into checks.

## Scope and boundaries

This is a **product-behavior reasoning tool**, not a general agent-memory or multi-agent tool. Its subject is application semantics: what actors can do, how state changes, what must remain true, how dependent surfaces respond, and what happens on failure. `.logic/` is only the compact project record needed to preserve those behavior decisions across development sessions; session notes are checkpoints, not chat history or agent coordination.

- Spec Driven owns product intent, scope, requirements, acceptance criteria, and delivery gates. Logic takes an established or emerging capability and checks whether its behavior is coherent and complete.
- Logic owns behavior maps, state/transition models, invariants, edge cases, effects, and evidence for those rules.
- Ops owns repository health, provenance, maintenance, and handoff.
- Agent assignment, delegation, shared agent state, and orchestration belong to a separate multi-agent tool; do not add them here.

## Ongoing product-logic mode

When installed, consult `.logic/` whenever a product feature or behavior is being designed or changed. Treat it as a durable behavior record, not the purpose of the toolkit. For each relevant feature discussion:

1. Read `.logic/README.md`, `.logic/index.md`, and the relevant feature record before proposing implementation; if no record exists, inspect the code and the user's stated intent.
2. Match the user's request to an existing feature, state, invariant, decision, or pattern. Do not assume a new conversation means a new logic context.
3. Summarize affected existing behavior and identify gaps or contradictions. Ask a focused clarification question only when an unresolved choice materially changes product behavior.
4. During the exchange, maintain a distinction between confirmed facts, user decisions, proposed logic, and unverified assumptions.
5. Before implementation, update the relevant behavior record or create one under `.logic/features/` when a durable behavior rule has been decided.
6. After a meaningful decision or implementation, add a concise checkpoint under `.logic/sessions/` and update `.logic/index.md` only as needed to make the authoritative logic easy to find.

This is an active protocol, not a one-time documentation task. If the memory is stale, contradictory, or missing, surface that explicitly and reconcile it with the user before silently overwriting it.

Do not store secrets, raw transcripts, personal data, or every conversational detail. Store only durable behavioral knowledge and links to code/tests.

## Product behavior analysis loop

For the changed capability, map actor/action, preconditions, input boundaries, current state, legal and forbidden transitions, effects, success, failure, retry, cancellation, and recovery. Trace the change to dependent data, UI surfaces, APIs, authorization, cache, events, accessibility, localization, and other consumers as applicable. State which cases are out of scope and why. Prefer an existing verified pattern over inventing a new one.

For visual behavior, reason across semantic roles rather than one component at a time. For example, a theme switch must keep foreground/background contrast and visibility coherent for text, surfaces, borders, icons, focus, disabled/loading/error states, overlays, charts, images, and native controls in every supported theme.

## Cross-project logic reuse

When installed through `logic-skill`, also consult the reusable logic library. Before inventing a rule, search the library for an applicable pattern. After a feature stabilizes, scan the project's `.logic/` records for candidates that are portable across projects.

Never promote a project-specific rule automatically. A candidate must be generalized, stripped of identifiers and assumptions, linked to evidence, and reviewed for portability before entering the shared library. Keep project-specific behavior in `.logic/features/`; keep reusable product-behavior abstractions in the library. The scanner finds possible text candidates only; it does not infer, validate, or promote logic.

## Core distinction

- `spec-driven-product-toolkit` decides what product capability is requested and how delivery is gated.
- `logic-skill` discovers and preserves what must remain true for behavior to work across states, actors, surfaces, failures, and conversations.
- `ops-toolkit` evaluates repository hygiene, provenance, maintenance, and handoff readiness.

Do not replace a product spec with a logic map, and do not treat a clean repository as evidence that behavior is complete.

## Strict non-overlap boundary

This skill owns **logical completeness and consistency of product behavior during development**. It does not own:

- product discovery, prioritization, roadmap, requirements authoring, acceptance criteria, release profiles, or implementation/release gates;
- repository metadata, attribution, provenance, documentation hygiene, public-release readiness, handoff readiness, or maintenance lifecycle checks;
- multi-agent delegation/orchestration, generic agent memory or chat-history retrieval;
- generic code style, security review, dependency governance, CI orchestration, or project management.

Use the other toolkits when those are the primary request. Invoke this toolkit only when the question is whether a behavior is logically complete and consistent across its possible states and effects.

### Ownership test

Ask: “What is the smallest unit being evaluated?”

- A **product requirement or delivery process** belongs to `spec-driven-product-toolkit`.
- A **behavior change and its state/effect correctness** belongs here.
- A **repository/product lifecycle or handoff condition** belongs to `ops-toolkit`.

If a task crosses boundaries, keep one owner per concern and pass artifacts between them. Do not duplicate their checklists or create a second source of truth.

## Required reasoning loop

Before editing behavior:

1. Identify the capability and behavior change; use the product spec as context when available, without rewriting its scope or acceptance criteria.
2. Locate existing states, transitions, derived state, side effects, persistence, permissions, and consumers.
3. Build a behavior map: actor/action, preconditions, input boundaries, state change, effects, success, failure, retry, cancellation, and recovery.
4. List invariants that must hold before, during, and after each transition.
5. Trace impact to dependent UI, API, permissions, cache, events, analytics, notifications, and accessibility states.
6. Find an existing pattern to reuse before introducing a new abstraction.
7. Identify the smallest useful verification: example-based tests, decision tables, stateful/model-based tests, or property-based tests where suitable. Do not add a framework dependency merely to use a testing technique.
8. Implement the smallest change that preserves the behavior model.
9. Verify happy path, invalid input, boundary values, repeated action, refresh/reload, concurrency, permission changes, and partial failure as applicable.
10. Record changed durable behavior and any reusable-rule candidate in the appropriate logic artifact.

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

For the conceptual model and artifact templates, read [references/logic-model.md](references/logic-model.md). For in-scope upstream concepts and exclusions, read [references/source-catalog.md](references/source-catalog.md).
