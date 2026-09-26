# Hung Toolkit

Hung Toolkit packages three complementary development toolkits in one distributable bundle:

1. **Logic** — behavioral completeness, persistent logic memory, state transitions, invariants, and reusable logic patterns.
2. **Ops** — repository hygiene, provenance, documentation integrity, maintenance, and handoff readiness.
3. **Spec Driven** — product specifications, implementation workflow, quality gates, and release profiles.

The bundle preserves the three toolkits as independent components. It does not merge their checklists or create a second source of truth.

```text
hung-toolkit/
├── components/
│   ├── Logic/
│   ├── Ops/
│   └── Spec-Driven/
└── bundle.json
```

## Ownership flow

```text
Spec Driven → Logic → implementation → Ops
```

Use the Spec Driven component to define what to build, Logic to preserve behavioral correctness across conversations and projects, and Ops to keep the resulting repository maintainable and handoff-ready.

## Installation

Install each component using its own instructions. The component boundaries are intentional:

- `components/Spec-Driven/SKILL.md`
- `components/Logic/SKILL.md`
- `components/Ops/README.md`

For reusable logic discovery, use:

```powershell
python components/Logic/../..\logic-toolkit\scripts\scan_logic.py --project D:\path\to\project --write-report
```

When distributing the bundle outside this workspace, copy the reusable logic library from the standalone `logic-toolkit/library/` package alongside the bundle.
