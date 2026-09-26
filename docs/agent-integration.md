# Agent Integration Guide

## What Hung Toolkit is

Hung Toolkit is a repository-resident context system for coding agents. It makes important reasoning durable instead of leaving it trapped in one chat. It is not a single autonomous daemon and does not replace the agent; it gives the agent a routing protocol, durable artifacts, and reusable behavior knowledge.

## Recommended project installation

Copy or install the bundle into the project, then create these directories:

```text
.toolkit/
.logic/
  features/
  sessions/
.spec-product/
.steward/
```

Keep the directories separate. `.logic/` is the behavioral memory; `.spec-product/` belongs to the Spec Driven component; `.steward/` belongs to Ops.

## First conversation

The agent should:

1. read `AGENTS.md`;
2. inspect `.toolkit/manifest.json` if present;
3. read `.logic/index.md` and relevant feature records;
4. identify whether the request is product scope, behavior logic, or repository operations;
5. summarize relevant existing context before asking questions or editing code.

## Feature conversation lifecycle

```text
user request
  → route concern
  → recover project memory
  → detect affected behavior
  → model states/dependencies/invariants
  → clarify unresolved decisions
  → update durable records
  → implement
  → verify evidence
  → checkpoint conversation
```

## Recommended response shape

For a behavior change, an agent should communicate:

```text
Existing logic: ...
Affected states: ...
Dependent effects: ...
Invariant risks: ...
Open question(s): ...
Proposed change: ...
Verification: ...
Memory updates: ...
```

This prevents a later conversation from treating a proposal as an established fact.

## When to ask for clarification

Ask when ambiguity affects authorization, state transitions, persistence, duplicate/retry behavior, partial failure, user-visible states, external side effects, or data ownership. Make questions narrow and explain the behavior that changes depending on the answer.

## When not to ask

Use an existing project pattern for naming, formatting, ordinary layout, or other reversible details. Do not create ceremony for a change whose behavior is already explicit and covered by existing invariants.

## Updating memory

A feature record is durable when it describes behavior that another conversation must know. A session checkpoint is a compact recovery note. The index is a map, not a second copy of every feature record.
