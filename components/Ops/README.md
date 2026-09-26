# Ops Toolkit

Ops Toolkit automates the non-feature operations needed to make a software project clean, attributable, publishable, handoff-ready, and maintainable.

It complements `spec-driven-product-toolkit`; it does not replace specification, implementation, testing, or code-security workflows.

## Scope

- repository hygiene and metadata consistency;
- authorship, attribution, and provenance records;
- documentation and reference integrity;
- public-release and handoff readiness;
- lifecycle and maintenance checks.

## Design principles

- deterministic checks before AI-assisted recommendations;
- findings are evidence-backed and traceable;
- safe preparation is separate from human-approved promotion;
- destructive actions are never automatic;
- every inherited idea is recorded in `references/source-catalog.md`.

## Commands

```powershell
python scripts/inspect_repo.py --profile local --write-report
python scripts/inspect_repo.py --profile public --json
```

Reports are written to `.steward/reports/` only when `--write-report` is supplied.

## Relationship to spec-driven-product-toolkit

The product-development toolkit owns specs, implementation workflow, product tests, technical audits, and release-quality gates. Ops Toolkit owns the operational work around those outputs. Its state is stored under `.steward/`, never `.spec-product/`.

## Provenance

See [`references/source-catalog.md`](references/source-catalog.md) for upstream repositories, URLs, licenses, adopted capabilities, adaptations, and exclusions.
