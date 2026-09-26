# Conversation Memory Protocol

## Feature record

Each feature record should contain only durable logic:

```md
# Feature: <name>

Status: proposed | active | deprecated
Owner surfaces: <UI/API/domain/jobs>
Last reviewed: YYYY-MM-DD

## Intent
What the behavior is supposed to accomplish.

## Actors and states
- Actors:
- States:
- Legal transitions:
- Forbidden transitions:

## Invariants
- [ ] Invariant — evidence: <test/file/check>

## Dependencies and effects
- Reads:
- Writes:
- Derived UI/API effects:
- External side effects:

## Open questions
- [ ] Question — decision needed from: user | code inspection | test

## Decisions
- YYYY-MM-DD — decision and rationale

## Verification
- Tests/checks:
- Known gaps:
```

## Conversation checkpoint

A session record should answer:

- what feature was discussed;
- what existing memory was consulted;
- what was confirmed, proposed, rejected, or left open;
- what files/tests/decisions changed;
- what the next conversation must know.

Do not copy the whole transcript. A checkpoint is a recovery index, not a chat archive.

## Clarification policy

Ask a question when the answer changes one of these: legal state transitions, data ownership, authorization, side effects, failure/retry semantics, user-visible behavior, or persistence. Do not block on cosmetic preferences that can safely follow an existing project pattern.

## Conflict policy

When records disagree:

1. identify the conflicting records and code evidence;
2. prefer the latest explicit user decision only for its stated scope;
3. do not silently rewrite history;
4. record a new decision that resolves or intentionally preserves the conflict;
5. mark affected invariants as unverified until checked.
