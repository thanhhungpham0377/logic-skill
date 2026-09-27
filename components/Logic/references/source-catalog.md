# Source Catalog

Logic Toolkit is an original, product-behavior-focused composition. It borrows ideas, not code. This catalog documents conceptual references; it does not imply a dependency or integration.

| Source | Relevant concept | Boundary |
|---|---|---|
| [Stately XState](https://github.com/statelyai/xstate) | Explicit state machines/statecharts, transitions, visualization, and model-based testing | Modeling reference only; no required XState runtime. |
| [Hypothesis stateful testing](https://hypothesis.readthedocs.io/en/latest/stateful.html) | Generated action sequences and invariants across changing states | Testing technique reference; Python API is optional and stack-specific. |
| [fast-check model-based testing](https://fast-check.dev/docs/advanced/model-based-testing/) | Commands, guards/preconditions, model-vs-system checks, and generated sequences | Testing technique reference; no JavaScript dependency is required. |
| [Stateful property-testing tutorial](https://github.com/stevana/property-based-testing-stateful-systems-tutorial) | Stateful sequence generation and invariant checking | Deeper systems-testing ideas; apply proportionately. |
| [OpenZeppelin/daml-props](https://github.com/OpenZeppelin/daml-props) | Checking invariants after generated transitions | Domain-specific example, not a toolkit dependency. |
| [OpenAI design-system rules](https://github.com/openai/skills/blob/main/skills/.curated/figma-create-design-system-rules/SKILL.md) | Actionable visual-system rules and progressive disclosure | Narrowly informs visual consistency analysis. |
| [archagent](https://github.com/BenedatLLC/archagent) | Machine-checkable invariants | Adjacent architecture focus; use only where an invariant directly protects product behavior. |

General agent memory, task tracking, coding workflow, and multi-agent orchestration are intentionally excluded from the core method. See [the source evaluation](../../../docs/logic-source-evaluation.md) for scope and rationale. `.logic/` is a small record of product behavior decisions, not a general agent-memory or coordination system.

## Non-overlap

- `spec-driven-product-toolkit` owns product scope, requirements/specification authoring, acceptance criteria, delivery workflow, and release gates.
- Logic Toolkit owns behavior completeness: state, transitions, conditions, effects, invariants, cross-surface impact, and failure/recovery paths.
- `ops-toolkit` owns repository hygiene, provenance, maintenance, and handoff.
- Multi-agent delegation and orchestration belong to a separate tool.

Logic records may link to specifications, code, and tests, but do not copy or replace their authoritative artifacts.
