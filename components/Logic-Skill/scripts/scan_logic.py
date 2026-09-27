"""Scan a project's .logic memory and propose reusable cross-project rules."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

MARKERS = ("invariant", "pattern", "retry", "idempot", "transition", "permission", "theme", "loading")
PROJECT_SPECIFIC = re.compile(r"\b(user|account|order|tenant|workspace|customer|project)\s*[_-]?\d+\b", re.I)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--project", type=Path, required=True, help="Project containing .logic/")
    ap.add_argument("--library", type=Path, default=Path(__file__).resolve().parents[1] / "library")
    ap.add_argument("--write-report", action="store_true")
    args = ap.parse_args()
    logic = args.project.resolve() / ".logic"
    if not logic.is_dir():
        ap.error(f"missing logic memory directory: {logic}")

    candidates: list[dict[str, str]] = []
    for path in sorted(logic.rglob("*.md")):
        if "sessions" in path.parts or path.name in {"README.md", "SOURCE.md", "index.md"}:
            continue
        for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            line = raw.strip()
            lower = line.lower()
            if not line or line.startswith("#") or not any(marker in lower for marker in MARKERS):
                continue
            if PROJECT_SPECIFIC.search(line):
                continue
            candidates.append({"source": str(path.relative_to(logic)), "line": str(number), "rule": line})

    print(f"Found {len(candidates)} reusable candidates")
    for item in candidates:
        print(f"- {item['source']}:{item['line']} — {item['rule']}")
    if args.write_report:
        report = logic / "reusable-candidates.md"
        lines = ["# Reusable Logic Candidates", "", "Review each candidate before promotion.", ""]
        lines.extend(f"- `{x['source']}:{x['line']}` — {x['rule']}" for x in candidates)
        report.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"Wrote {report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
