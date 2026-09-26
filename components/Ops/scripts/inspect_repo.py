#!/usr/bin/env python3
"""Deterministic, read-only first-pass Ops Toolkit inspector."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED_BY_PROFILE = {
    "local": ["README.md", "LICENSE", ".gitignore"],
    "public": ["README.md", "LICENSE", "SECURITY.md", "CONTRIBUTING.md"],
    "handoff": ["README.md", "LICENSE", "SECURITY.md", "CONTRIBUTING.md", "CHANGELOG.md"],
    "maintained": ["README.md", "LICENSE", "SECURITY.md", "CHANGELOG.md"],
}
TEXT_SUFFIXES = {".md", ".txt", ".yml", ".yaml", ".json", ".toml", ".ini", ".py", ".js", ".ts", ".tsx", ".jsx"}
PLACEHOLDER_PATTERNS = ("TODO", "FIXME", "CHANGE_ME", "YOUR_", "example.com", "localhost", "127.0.0.1")


def inspect(root: Path, profile: str) -> dict:
    findings = []
    for relative in REQUIRED_BY_PROFILE[profile]:
        path = root / relative
        findings.append({
            "id": f"repository.required-file.{relative}",
            "category": "repository-hygiene",
            "status": "pass" if path.exists() else "fail",
            "severity": "error" if not path.exists() else "info",
            "evidence": {"path": relative},
            "remediation": f"Create {relative}" if not path.exists() else None,
        })

    for name in (".env", ".env.local", ".env.production"):
        if (root / name).exists():
            findings.append({
                "id": f"repository.environment.{name}-present",
                "category": "public-release",
                "status": "manual-review",
                "severity": "warning",
                "evidence": {"path": name, "details": "Environment file exists; contents were not read."},
                "remediation": "Confirm it is ignored and contains no publishable material.",
            })

    text_files = [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in TEXT_SUFFIXES and ".git" not in p.parts and ".steward" not in p.parts]
    placeholder_hits = []
    local_path_hits = []
    for path in text_files:
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        relative = path.relative_to(root).as_posix()
        for line_number, line in enumerate(content.splitlines(), 1):
            if "PLACEHOLDER_PATTERNS" not in line and any(token in line for token in PLACEHOLDER_PATTERNS):
                placeholder_hits.append({"path": relative, "line": line_number, "details": line.strip()[:240]})
            if "re.search" not in line and re.search(r"(?:[A-Z]:\\|/Users/|/home/|/tmp/|\\Users\\)", line):
                local_path_hits.append({"path": relative, "line": line_number, "details": line.strip()[:240]})

    for category, hits, severity in (("placeholder", placeholder_hits, "warning"), ("local-path", local_path_hits, "warning")):
        findings.append({
            "id": f"public-release.{category}-detected",
            "category": "public-release",
            "status": "manual-review" if hits else "pass",
            "severity": severity if hits else "info",
            "evidence": {"matches": hits[:50], "count": len(hits)},
            "remediation": "Review each match; not every placeholder or local path is publishable data." if hits else None,
        })

    markdown_files = [p for p in text_files if p.suffix.lower() == ".md"]
    broken_refs = []
    markdown_link = re.compile(r"\[[^]]+\]\(([^)#]+)(?:#[^)]*)?\)")
    for path in markdown_files:
        content = path.read_text(encoding="utf-8")
        for target in markdown_link.findall(content):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            candidate = (path.parent / target).resolve()
            if not candidate.exists():
                broken_refs.append({"path": path.relative_to(root).as_posix(), "target": target})
    findings.append({
        "id": "documentation.local-reference-integrity",
        "category": "documentation",
        "status": "fail" if broken_refs else "pass",
        "severity": "error" if broken_refs else "info",
        "evidence": {"matches": broken_refs[:50], "count": len(broken_refs)},
        "remediation": "Fix or remove broken local Markdown references." if broken_refs else None,
    })

    assets = []
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".ico", ".woff", ".woff2", ".ttf", ".otf"} and ".git" not in path.parts and ".steward" not in path.parts:
            assets.append({"path": path.relative_to(root).as_posix(), "bytes": path.stat().st_size, "extension": path.suffix.lower()})
    findings.append({
        "id": "provenance.asset-inventory",
        "category": "provenance",
        "status": "manual-review" if assets else "pass",
        "severity": "warning" if assets else "info",
        "evidence": {"assets": assets},
        "remediation": "Record source, license, and attribution for each distributable asset." if assets else None,
    })

    return {"version": "0.1.0", "profile": profile, "root": str(root), "findings": findings}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--profile", choices=sorted(REQUIRED_BY_PROFILE), default="local")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--write-report", action="store_true")
    args = parser.parse_args()
    report = inspect(args.root.resolve(), args.profile)
    if args.write_report:
        output = args.root.resolve() / ".steward" / "reports"
        output.mkdir(parents=True, exist_ok=True)
        (output / f"{args.profile}.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        for finding in report["findings"]:
            print(f"[{finding['status']}] {finding['id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
