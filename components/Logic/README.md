# Logic Development Toolkit

Logic Development Toolkit helps AI-assisted development avoid the most expensive class of rework: code that works for the first visible path but is incomplete across states, transitions, dependencies, and failure modes.

It is intentionally separate from product specification and product stewardship. Its unit of work is the **behavior change**.

## Explicit non-goals

This repository does not define product requirements, choose delivery/release profiles, run product audits, manage repository metadata, maintain attribution/provenance, or judge handoff/publication readiness. Those remain owned by the other toolkits.

## What it covers

- state and transition modeling;
- invariant and precondition discovery;
- impact analysis across dependent surfaces;
- edge-case and failure-path matrices;
- pattern reuse and duplication detection;
- evidence-backed implementation review.

## Suggested project layout

```text
.logic/
  logic-map.md
  state-model.md
  invariants.md
  edge-cases.md
  patterns.md
  decisions.md
```

## Relationship to the other toolkits

```text
specification → logic model → implementation → stewardship
```

The logic model is the bridge: it translates a product request into behavior that can remain correct under real state changes.

## Ownership boundaries

| Concern | Owner | Output consumed here |
|---|---|---|
| What should be built and how delivery is gated | `spec-driven-product-toolkit` | Product request, acceptance criteria, implementation context |
| Whether the behavior is complete across states, effects, and failures | This toolkit | Logic map, state model, invariants, edge-case matrix |
| Whether the repository/product is maintainable, attributable, and handoff-ready | `product-stewardship-toolkit` | Logic evidence and implementation artifacts |

The three toolkits may be composed, but their artifacts and decisions must remain separate. A logic map is not a product spec, and passing a logic review is not a stewardship or release approval.

## Design principles

- model behavior before editing code;
- distinguish facts, assumptions, and decisions;
- prefer existing patterns over new local logic;
- make invariants executable where practical;
- use AI for discovery and synthesis, deterministic checks for evidence;
- report uncertainty instead of hiding it.

## Status

This is the initial workflow and reference model. It is designed to grow through real failure cases, not by accumulating generic rules.
