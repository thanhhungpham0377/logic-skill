# Source catalog and inheritance record

This toolkit is an original composition and integration layer. It is not an official fork or distribution of the projects listed below. Before redistributing code, re-check each upstream repository's current license and notices.

| Capability | Upstream source | Adopted idea | Adaptation in this toolkit | License/provenance status |
|---|---|---|---|---|
| Repository health checks | [spbuilds/repohealth](https://github.com/spbuilds/repohealth) | Deterministic, offline, CI-ready hygiene scoring and actionable findings | Findings-first model; score is optional and never replaces severity/status | Reference only; no source code copied |
| Repository maturity tiers | [DSACMS/repo-scaffolder](https://github.com/DSACMS/repo-scaffolder) | Maturity tiers, templates, outbound checklist, existing-repo linting | Profiles are local/public/handoff/maintained and target product stewardship | Reference only; no source code copied |
| Public-release privacy review | [Okavango-SAS/RepoPrivacyGuardian](https://github.com/Okavango-SAS/RepoPrivacyGuardian) | Clean-clone validation, release readiness, privacy leakage review, evidence reports | Read-only inspectors first; remediation is opt-in and approval-gated | Reference only; no source code copied |
| Public repository release checklist | [pikos-apikos/pnyx](https://github.com/pikos-apikos/pnyx/blob/main/PUBLIC_RELEASE_CHECKLIST.md) | Git history, branches, PR visibility, asset/license, and repository-settings review | Converted into machine-checkable checks plus explicit manual-review items | Documentation inspiration; preserve attribution if text is reused |
| Release readiness evidence | [releaseatelier/release-readiness-playbook](https://github.com/releaseatelier/release-readiness-playbook) | Evidence classes and go/no-go checklist | Evidence is attached to each finding and profile gate | Reference only; no source code copied |
| Handoff and ownership | [happysnaker/production-readiness-checklist](https://github.com/happysnaker/production-readiness-checklist) | Ownership, rollback, monitoring, and handoff checklist | Limited to administrative/handoff readiness; product tests remain external | Reference only; no source code copied |
| Multi-repository lifecycle health | [Zejnilovic/github-repo-health](https://github.com/Zejnilovic/github-repo-health) | Activity, maintenance, resilience, hygiene, and lifecycle status | Future GitHub adapter; local mode does not require API access | Reference only; no source code copied |
| Documentation integrity | [your-ko/link-validator](https://github.com/your-ko/link-validator) | Local/GitHub/HTTP link validation and CI integration | Adds referenced-file, command, version, and screenshot drift checks | Reference only; no source code copied |

## Excluded overlap

The following are deliberately not reimplemented here: feature specification, implementation orchestration, unit/E2E testing, SAST, secret scanning, dependency vulnerability scanning, SQL quality, migration authority, and PR code review. Those belong to `spec-driven-product-toolkit` or the project's existing quality system.

## Change policy

Every new inherited capability must add a row to this catalog, identify its upstream URL, record whether code/text/configuration was copied, and include the applicable license/notice review before release.
