# Logic Toolkit Source Evaluation

Reviewed: 2026-09-27. This comparison is scoped to **application behavior logic**: modeling states and transitions, expressing invariants, finding edge cases, and checking behavior. Popularity is a discovery signal, not evidence of quality or fit. No source code is copied or dependency is required by this evaluation.

## In-scope references

| Source | Relevant contribution | Fit and boundary |
|---|---|---|
| [Stately XState](https://github.com/statelyai/xstate) | Statecharts/state machines, explicit transitions, visual inspection, and model-based testing concepts | Strong reference for making behavior and legal paths visible. Logic Toolkit borrows the modeling approach; it does not require XState or prescribe a runtime. |
| [Hypothesis stateful testing](https://hypothesis.readthedocs.io/en/latest/stateful.html) | Generate action sequences against a model and check invariants after each action | Strong testing reference for stateful behavior. Python-specific API; use only when suitable for the product stack. |
| [fast-check model-based testing](https://fast-check.dev/docs/advanced/model-based-testing/) | Commands, preconditions, model-vs-real-system checks, and generated command sequences | Useful language-agnostic testing pattern with JavaScript/TypeScript examples; not a required test framework. |
| [Property-based testing of stateful systems](https://github.com/stevana/property-based-testing-stateful-systems-tutorial) | Stateful property testing, generated sequences, and failure exploration | Useful deeper treatment for complex stateful systems; can be more machinery than ordinary UI/product features need. |
| [OpenZeppelin/daml-props](https://github.com/OpenZeppelin/daml-props) | Generate action sequences and check invariants after transitions | A domain-specific example of invariant-based testing, not a DAML dependency or general product workflow. |
| [OpenAI design-system rules](https://github.com/openai/skills/blob/main/skills/.curated/figma-create-design-system-rules/SKILL.md) | Specific, actionable rules and progressive disclosure | Relevant narrowly to cross-surface visual consistency; not a substitute for product state/transition analysis. |

## Adjacent, selective references

| Source | Potentially useful idea | Why it is not a core source |
|---|---|---|
| [archagent](https://github.com/BenedatLLC/archagent) | Machine-checkable architecture invariants and drift checks | Primarily architecture-level; borrow only invariant/evidence techniques that directly protect product behavior. |
| [Sensei](https://github.com/globulario/sensei) | Linking invariants, failure modes, proof obligations, and impact | Broader behavioral/architectural knowledge system; Logic Toolkit does not claim graph extraction, closure, or governance. |
| [Grove](https://github.com/alxshelepenok/grove) | Explicit protocol invariants and evidence-bound completion | Primarily agent protocol/orchestration. Do not adopt its orchestration or persistence model in Logic Toolkit. |

## Explicitly out of scope

General coding-agent memory, session retrieval, task/dependency tracking, skill workflow systems, and multi-agent orchestration are not sources for Logic Toolkit's core behavior-analysis method. Examples include [agentmemory](https://github.com/rohitg00/agentmemory), [Beads](https://github.com/gastownhall/beads), and [Superpowers](https://github.com/obra/superpowers). They may inform a separate memory or multi-agent product, but they do not answer whether a product feature has coherent states, transitions, effects, and invariants.

Project-local `.logic/` files are a deliberately small support mechanism for preserving **decided product behavior** between development conversations. They are not a generic agent memory engine, chat archive, task tracker, or agent coordination protocol.

## Design conclusions

1. Start from the behavior: actor/action, preconditions, input bounds, states, transitions, effects, failures, retries, cancellation, and recovery.
2. Make invariants observable and pair important ones with proportionate evidence: examples, decision tables, stateful/model-based tests, or property-based tests.
3. Trace cross-surface consequences (such as theme, permissions, loading, localization, and accessibility) instead of analyzing only the edited control.
4. Use `.logic/` to preserve confirmed behavior decisions and unresolved behavior questions. Keep product scope and acceptance criteria with Spec Driven.
5. Keep reusable patterns behavior-specific, generalized, evidence-linked, and human-reviewed. A keyword scan only proposes candidate passages.
6. Do not introduce testing libraries or runtime dependencies solely because an upstream reference uses them.

This evaluation is a scoped design comparison, not a claim that the toolkit has exhaustively benchmarked every repository or that star counts rank quality.
