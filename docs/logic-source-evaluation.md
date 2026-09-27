# Logic Toolkit Source Evaluation

Snapshot researched: 2026-09-27. GitHub stars are approximate popularity signals, not quality scores; they change over time. Repository descriptions and activity were reviewed alongside fit to Logic Toolkit's scope.

## Strongest relevant sources

| Repository | Stars observed | Strong contribution | Fit and limitation |
|---|---:|---|---|
| [agentmemory](https://github.com/rohitg00/agentmemory) | ~28.9k | Broad persistent coding-agent memory, many agent integrations, retrieval/evaluation work | Strongest popularity and mature memory reference; much broader runtime and scope than our behavior-contract library |
| [Beads](https://github.com/gastownhall/beads) | ~26.9k (Sep 3 snapshot) | Git-backed dependency graph and long-horizon task continuity | Strong for task/work dependency memory, not a feature invariant catalog |
| [Superpowers](https://github.com/obra/superpowers) | ~285k (search snapshot) | Agent skills, workflow routing, session-start behavior and structured development methodology | Very strong skill/workflow reference; not a durable project behavior memory system |
| [projectmem](https://github.com/riponcm/projectmem) | 834 | Local-first typed events for issues, attempts, fixes and decisions; MCP integrations and precheck | Closest workflow/memory reference for recording project experience; does not specialize in complete feature state/invariant models |
| [OKF Agent Memory](https://github.com/okf-memory/okf-agent-memory) | 708 | Search-before-write, provenance/trust metadata, progressive disclosure, validation and graph relationships | Strong architecture reference for knowledge hygiene; standard/tooling approach may be heavier than a Markdown-first toolkit |
| [common-knowledge](https://github.com/shihabshahrier/common-knowledge) | GitHub page showed no star count in fetched snapshot | Git-backed Markdown knowledge base, per-project and global learning separation, multi-agent distribution | Closest lightweight file-based pattern; activity/scale evidence is limited in the available snapshot |
| [archagent](https://github.com/BenedatLLC/archagent) | 0 in fetched page snapshot | Extracts architecture invariants and checks drift deterministically | Excellent conceptual fit for enforceable invariants; currently low community adoption, so use its ideas selectively |
| [Grove](https://github.com/alxshelepenok/grove) | 24 | Explicit state/protocol invariants and evidence-bound completion | Useful formal workflow ideas; broad orchestration and AGPL-3.0 are not assumed or copied |

## Assessment

The previous Logic design was not based on the most popular or most complete repositories in the persistent-memory space. It used `archagent`, Grove, testing/property concepts, and agent-rule guidance, but omitted key memory systems such as `agentmemory`, `projectmem`, Beads, and OKF Agent Memory from its source catalog.

No single repository is the best source for the whole goal. The best-fit synthesis is:

- use Superpowers as a reference for session/skill activation and agent workflow;
- use agentmemory, projectmem, common-knowledge and OKF Agent Memory for persistent memory, retrieval, provenance, and cross-agent portability;
- use archagent and property/model-based testing for invariants, state transitions, and evidence;
- use Beads only when the project also needs dependency-aware task tracking.

Stars alone do not prove quality. For adoption, evaluate license, active maintenance, tests/CI, agent compatibility, data model, security, portability, and scope fit. This document records research and design guidance; it does not claim these repositories' code or features are integrated.

## Recommended next design improvements

1. Keep project behavior records separate from reusable cross-project patterns.
2. Add provenance, trust/status, reviewed date, verification method, and scope to each memory entry.
3. Require search-before-write and deduplicate concepts before adding memory.
4. Add deterministic validation for record shape and references; keep semantic judgment agent-assisted.
5. Add optional agent-specific activation adapters (AGENTS.md, Codex skill, Claude hooks, MCP) while keeping Markdown as the portable source of truth.
6. Treat the current keyword scanner as candidate discovery only. Do not describe it as a logic validator or automatic pattern extractor.
