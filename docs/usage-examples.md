# Usage Examples

## New feature

User: “Add a notification preferences screen.”

Agent behavior:

1. Read existing notification/auth/settings records.
2. Check states such as enabled, disabled, pending save, save failed, and permission denied.
3. Ask whether preferences are per-user, per-device, or per-organization if memory does not decide it.
4. Record the decision and invariants before implementation.
5. Verify reload, duplicate save, stale data, failure, and authorization.

## Cross-cutting theme change

User: “Add light theme.”

Agent checks page background, surfaces, text, muted text, borders, icons, focus, disabled, overlays, shadows, charts, images, and native controls. It does not patch one component and assume the theme is complete.

## Continuing an old conversation

User: “Continue the checkout work.”

Agent searches `.logic/index.md` for checkout, reads its feature record and latest session checkpoint, then reports the current state and open questions before changing code.

## Reusing logic across projects

After a project establishes an idempotent mutation rule:

```powershell
python components/Logic/scripts/scan_logic.py --project D:\path\to\project --write-report
```

Review the candidate, generalize it, add evidence and portability notes, then append it to `components/Logic/reusable-library/index.md`.
