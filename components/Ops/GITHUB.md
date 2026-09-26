# GitHub repository procedure

This project is intended to be hosted as a private GitHub repository during development.

## Initial setup

```powershell
gh auth refresh -h github.com
git init
git add .
git commit -m "chore: initialize product stewardship toolkit"
gh repo create ops-toolkit --private --source . --remote origin --push
```

## Recommended repository settings

- Keep visibility private until the authorship, license, provenance, and public-release review is complete.
- Enable Issues and Discussions only when they have an owner and moderation policy.
- Protect the default branch and require pull requests.
- Require a successful CI check before merging.
- Restrict repository and environment secrets to the minimum required scope.
- Review collaborators, deploy keys, GitHub Apps, webhooks, and Actions permissions periodically.

## Release procedure

1. Run the local stewardship inspection.
2. Review `.steward/reports/` and resolve or explicitly suppress findings.
3. Confirm the license decision and update `LICENSE` and `NOTICE.md` if applicable.
4. Review Git history, branches, PRs, assets, and repository metadata before changing visibility.
5. Create a signed/versioned tag and GitHub release only after human approval.

## Current legal status

No license has been selected for this repository yet. Until a license is added, do not redistribute or treat the code as open source.
