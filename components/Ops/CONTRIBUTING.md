# Contributing

Please read `README.md` and `references/source-catalog.md` before changing the toolkit.

Every inherited capability, copied text, configuration, or code must be recorded in the source catalog with its upstream URL, license/notice status, and adaptation notes.

Changes should remain within Ops Toolkit's operations scope. Feature specifications, product implementation, and technical quality gates belong to `spec-driven-product-toolkit`.

Before submitting a change:

```text
python scripts/inspect_repo.py --profile local
```

Do not add destructive remediation by default. Prefer a finding, evidence, and an explicit human-approved patch.
