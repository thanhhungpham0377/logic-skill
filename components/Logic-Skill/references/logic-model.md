# Logic Model

## Behavior map

For each action, capture:

| Field | Question |
|---|---|
| Actor | Who or what initiates it? |
| Preconditions | What must already be true? |
| Input | What values and boundaries are accepted? |
| Transition | What state changes? |
| Effects | What else changes: data, cache, UI, events, notifications? |
| Failure | What can fail and is the operation atomic? |
| Retry | Is retry safe, idempotent, or forbidden? |
| Recovery | How does the system return to a known state? |

Add **observable outcome** and **verification evidence** where useful: what can a user or dependent system observe after the action, and which test/check demonstrates the rule? Link to an existing product spec for intent and acceptance criteria; do not copy those artifacts into the logic map.

## State model

Represent each state with entry conditions, permitted actions, exit transitions, and terminality. Explicitly list forbidden transitions. If a state machine is not appropriate, document why and use a decision table instead.

## Invariant classes

- **Data:** relationships, uniqueness, conservation, ordering, referential integrity.
- **Authorization:** actor and ownership constraints remain true at mutation time.
- **Lifecycle:** only legal transitions occur; terminal states stay terminal unless an explicit reversal exists.
- **Concurrency:** duplicate, stale, or reordered actions cannot create invalid results.
- **UI:** derived state reflects source state; loading/error/empty/disabled states do not contradict one another.
- **Cross-cutting:** theme, locale, accessibility, responsive layout, and feature flags cover every relevant surface.

For cross-cutting behavior, trace semantic roles and every affected surface. Example theme invariant: for every supported theme and component state, each rendered foreground/background pair remains visible and meets the project's contrast rule; icons, borders, focus indicators, disabled controls, overlays, charts, images, and native controls are included where present. A claim such as “theme works” is not sufficient evidence.

## Edge-case matrix

At minimum consider: empty, zero, maximum, malformed, duplicate, stale, unauthorized, unavailable dependency, timeout, partial success, retry, cancellation, refresh, back navigation, and concurrent mutation. Select only cases relevant to the behavior, and explain exclusions.

## Evidence levels

1. **Observed:** existing code/test/log proves the behavior.
2. **Derived:** follows from a documented state or dependency model.
3. **Assumed:** needed to proceed but not confirmed.
4. **Unverified:** a risk requiring a test, inspection, or user decision.

Never present an assumption as an observed invariant.

## Choosing verification

Use the lightest method that gives useful evidence:

- examples or table-driven tests for a small, known set of cases;
- decision tables when combinations of conditions determine outcomes;
- stateful/model-based tests when sequences and transitions matter;
- property-based tests when a broad input space can be expressed as general properties.

Do not mirror the implementation in the test oracle, and do not add a framework dependency only to follow a technique. Record uncovered cases as unverified rather than implying they passed.
