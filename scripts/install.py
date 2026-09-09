#!/usr/bin/env python3
"""Copy selected skills into an explicit directory without replacing files."""

import argparse
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]


def install(source, destination, names):
    source, destination = Path(source), Path(destination).expanduser().resolve()
    available = {p.name: p for p in source.iterdir() if (p / "SKILL.md").is_file()}
    selected = names or sorted(available)
    if not selected:
        raise ValueError("No skills found")
    if len(selected) != len(set(selected)):
        raise ValueError("Duplicate skill names")
    unknown = set(selected) - available.keys()
    if unknown:
        raise ValueError("Unknown skills: " + ", ".join(sorted(unknown)))
    targets = [destination / name for name in selected]
    conflicts = [p.name for p in targets if p.exists() or p.is_symlink()]
    if conflicts:
        raise ValueError("Existing destinations; nothing installed: " + ", ".join(conflicts))
    # Keep installations out of the source tree, including its ancestor paths.
    resolved_source = source.resolve()
    for target in targets:
        if (target == resolved_source or resolved_source in target.parents
                or target in resolved_source.parents):
            raise ValueError("Destination overlaps the source tree")
    destination.mkdir(parents=True, exist_ok=True)
    for name, target in zip(selected, targets):
        # mkdir is exclusive even if another process creates a target after preflight.
        target.mkdir()
        try:
            shutil.copytree(available[name], target, dirs_exist_ok=True)
        except Exception:
            shutil.rmtree(target)
            raise
    return targets


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", required=True, type=Path)
    parser.add_argument("names", nargs="*", help="Skill names; defaults to all")
    args = parser.parse_args()
    try:
        for path in install(ROOT / "skills", args.dest, args.names):
            print("Installed", path)
    except (ValueError, OSError) as error:
        print("Install failed:", error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
