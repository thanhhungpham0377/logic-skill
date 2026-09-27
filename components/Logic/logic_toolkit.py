"""Install the three non-overlapping development toolkits as one composition."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SIBLING_ROOT = ROOT.parent
COMPONENTS = {
    "spec-driven": SIBLING_ROOT / "spec-driven-product-toolkit",
}
PROFILES = ("prototype", "balanced", "production")


def read_version(path: Path) -> str:
    version = path / "VERSION"
    return version.read_text(encoding="utf-8").strip() if version.exists() else "unknown"


def check_component_sources(components: dict[str, Path]) -> list[str]:
    return [name for name, path in components.items() if not path.is_dir()]


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def install_spec(target: Path, profile: str, check_only: bool) -> int:
    installer = COMPONENTS["spec-driven"] / "scripts" / "install_profile.py"
    if not installer.exists():
        print(f"Missing spec installer: {installer}", file=sys.stderr)
        return 2
    command = [sys.executable, str(installer), "--target", str(target), "--profile", profile]
    if check_only:
        command.append("--check-only")
    return subprocess.run(command, check=False).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, type=Path)
    parser.add_argument("--profile", choices=PROFILES, required=True)
    parser.add_argument("--ops-source", type=Path, help="Path to ops-toolkit")
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    target = args.target.resolve()
    if not target.is_dir():
        parser.error(f"target is not a directory: {target}")

    components = dict(COMPONENTS)
    components["ops"] = (
        args.ops_source.resolve()
        if args.ops_source
        else SIBLING_ROOT / "ops-toolkit"
    )
    missing_sources = check_component_sources(components)
    if missing_sources:
        print("Missing sibling toolkits: " + ", ".join(missing_sources), file=sys.stderr)
        return 2

    state = target / ".toolkit"
    manifest = {
        "schema_version": 1,
        "installer_version": read_version(ROOT),
        "installed_at": datetime.now(timezone.utc).isoformat(),
        "profile": args.profile,
        "components": {
            name: {"path": str(path), "version": read_version(path), "state_dir": state_dir}
            for name, path, state_dir in (
                ("spec-driven", components["spec-driven"], ".spec-product"),
                ("logic", ROOT, ".logic"),
                ("ops", components["ops"], ".steward"),
            )
        },
        "ownership": {
            "spec-driven": "product scope, specifications, delivery workflow, release gates",
            "logic": "cross-conversation behavior memory, state models, invariants, reusable patterns",
            "ops": "repository/product hygiene, provenance, maintenance, handoff readiness",
        },
        "non_overlap": True,
    }
    print(json.dumps({"target": str(target), "profile": args.profile, "manifest": manifest}, indent=2))
    if args.check_only:
        return install_spec(target, args.profile, True)

    existing = state / "manifest.json"
    if existing.exists():
        old = json.loads(existing.read_text(encoding="utf-8"))
        if old.get("components") and old.get("components") != manifest["components"]:
            print(f"Refusing to overwrite incompatible manifest: {existing}", file=sys.stderr)
            return 2

    spec_rc = install_spec(target, args.profile, False)
    if spec_rc not in (0, 2):
        return spec_rc

    # The other two toolkits are documentation/state conventions, so installation
    # creates only their state directories and a pointer. It never copies or forks
    # their rules, preserving one source of truth per toolkit.
    for name, path, state_dir in (
        ("logic", ROOT, ".logic"),
        ("ops", components["ops"], ".steward"),
    ):
        pointer = target / state_dir / "SOURCE.md"
        write_text(pointer, f"# {name}\n\nInstalled by `toolkit`. Source of truth: `{path}`.\n")

    logic_state = target / ".logic"
    write_text(logic_state / "README.md", """# Logic Memory\n\nThis is the durable behavioral memory for the project. Every conversation that changes a feature must read the index and update the relevant feature record, invariant, decision, or session checkpoint.\n\nKeep confirmed facts, user decisions, proposals, and unverified assumptions distinct. Do not store raw transcripts or secrets.\n""")
    write_text(logic_state / "index.md", """# Logic Memory Index\n\n| Feature/concept | Record | States/invariants | Last reviewed | Open questions |\n|---|---|---|---|---|\n""")
    write_text(logic_state / "features/.gitkeep", "")
    write_text(logic_state / "sessions/.gitkeep", "")
    write_text(logic_state / "LIBRARY.md", f"# Reusable Logic Library\n\nShared library source: `{ROOT / 'library'}`. Search it before inventing a new cross-cutting behavior.\nUse `scan_logic.py` to propose candidates after a feature stabilizes.\n")

    write_text(state / "manifest.json", json.dumps(manifest, indent=2) + "\n")
    write_text(state / "README.md", """# Logic Toolkit integration\n\nThis directory is the durable behavior memory for the project. Read it before feature changes and update it when behavior decisions become durable.\n\nOwnership: Spec Driven defines product scope and delivery; Logic maintains behavior memory, state/invariant analysis, and cross-project patterns; Ops maintains repository health and handoff readiness.\n\nState directories remain separate: `.spec-product/`, `.logic/`, and `.steward/`.\n""")
    write_text(state / "index.md", """# Logic Memory Index\n\nAdd one row for each durable feature or cross-cutting behavior.\n\n| Feature/concept | Record | States/invariants | Last reviewed | Open questions |\n|---|---|---|---|---|\n""")
    write_text(state / "features/.gitkeep", "")
    write_text(state / "sessions/.gitkeep", "")
    print(f"Installed toolkit at {state}")
    return 2 if spec_rc == 2 else 0


if __name__ == "__main__":
    raise SystemExit(main())
