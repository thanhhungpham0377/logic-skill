# Project Product-Logic Records

These files preserve durable decisions about **application behavior** so later development work does not reintroduce missing or contradictory logic. They are a supporting record format, not a generic agent memory engine, transcript archive, task graph, or multi-agent coordination channel. Keep scope, product requirements, and acceptance criteria authoritative in Spec Driven artifacts and link to them instead of copying them here.

## Files

```text
.logic/
├── README.md              # purpose and update rules
├── SOURCE.md              # installed component reference
├── index.md               # feature/concept lookup table
├── invariants.md          # project-wide rules
├── state-model.md         # shared state machines
├── patterns.md            # project patterns and anti-patterns
├── decisions.md           # decisions with rationale
├── features/<name>.md     # one durable record per feature
├── sessions/<date>-*.md   # compact conversation checkpoints
└── reusable-candidates.md # scanner output awaiting review
```

Only create files that the project needs. The index must link to the authoritative record rather than duplicate it.

## Feature record minimum

```md
# Feature: <name>
Status: proposed | active | deprecated

## Intent
## Actors and states
## Legal and forbidden transitions
## Invariants
## Dependencies and effects
## Failure, retry, and recovery
## Open questions
## Decisions
## Verification
```

## Reusable logic promotion

Use this test before adding a rule to the shared library:

- Can it be expressed without project names or identifiers?
- Does it describe behavior rather than a local implementation detail?
- Does it apply to at least two plausible projects?
- Is there a verification method?
- Are portability limits documented?

If any answer is no, keep it in the project's `.logic/` memory.
