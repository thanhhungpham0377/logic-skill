# Reusable Logic Library

This library stores behavior patterns that are portable across projects. It is not a dump of project-specific requirements.

Promote a rule only when it has:

- a clear reusable abstraction;
- no project-specific names, IDs, URLs, secrets, or assumptions;
- a verification method;
- at least one source feature or project;
- an explicit portability note.

Use `scripts/scan_logic.py` to discover candidates. The scanner proposes; a human or agent must review and promote.
