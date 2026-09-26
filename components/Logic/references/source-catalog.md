# Source Catalog

This toolkit is an original composition. It borrows concepts, not code, and should preserve attribution when an implementation later adopts a specific upstream project.

| Source | Adopted idea | Boundary / exclusion |
|---|---|---|
| [archagent](https://github.com/BenedatLLC/archagent) | Architecture described as subsystems, lifecycles, flows, and machine-checkable invariants; deterministic checkers with LLM proposals | We focus on behavior completeness during feature work, not architecture enforcement only |
| [grove](https://github.com/alxshelepenok/grove) | Explicit protocol invariants, evidence-bound completion, dependency/causality thinking | We do not adopt its workflow protocol, persistence model, or orchestration |
| [OpenZeppelin/daml-props](https://github.com/OpenZeppelin/daml-props) | Generate action sequences and check invariants after transitions | We use this as a testing strategy, not a DAML dependency |
| [Agent Rigor](https://github.com/MeherBhaskar/agent-rigor) | Actionable gates, atomic transitions, anti-rationalization, and failure-mode thinking | We keep the scope to application logic, not a general agent operating system |
| [OpenAI design-system rules](https://github.com/openai/skills/blob/main/skills/.curated/figma-create-design-system-rules/SKILL.md) | Specific, actionable, prioritized rules with progressive disclosure | Design-system consistency is one domain of impact analysis, not the whole toolkit |
| [Sensei](https://github.com/globulario/sensei) | Behavioral memory, invariants, failure modes, proof obligations, and architectural impact | We do not claim graph extraction, closure, or governance features |

The research indicates that the missing combination is a lightweight, agent-facing behavior model that connects state transitions to dependent effects and repeatable edge-case checks.

## Excluded overlap

The existing local toolkits remain the owners of their current concerns:

- `spec-driven-product-toolkit`: profiles, specification-to-implementation workflow, product tests, technical audits, and release-quality gates.
- `product-stewardship-toolkit`: repository hygiene, authorship/attribution, provenance, documentation integrity, public release, handoff, and maintenance checks.

This toolkit therefore does not add replacement profiles, release gates, repository inspection reports, attribution files, or a second audit lifecycle. It contributes only behavior models and evidence about application logic.
