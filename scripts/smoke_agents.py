#!/usr/bin/env python3
"""Exercise cross-agent CLI installation in temporary projects (never globally)."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

import yaml

ROOT = Path(__file__).resolve().parents[1]
CLI = ["npx", "--yes", "skills@1.5.25"]
# Representative nonshared routes plus the shared route used by many agents.
# Full routing is delegated to the pinned CLI, not duplicated in our installer.
REQUIRED_ROOTS = (
    ".agents/skills", ".claude/skills", ".windsurf/skills", ".roo/skills",
    ".continue/skills", "skills", ".goose/skills", ".qwen/skills",
)


def run_cli(arguments, cwd):
    result = subprocess.run(
        CLI + arguments, cwd=cwd,
        env=dict(os.environ, DISABLE_TELEMETRY="1", NO_COLOR="1"),
        text=True, capture_output=True, timeout=180,
    )
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)
    return result.stdout


def verify(source, project):
    expected = {p.name: p for p in (source / "skills").iterdir() if (p / "SKILL.md").is_file()}
    run_cli(["add", str(source), "--all", "--copy"], project)
    inventory = json.loads(run_cli(["list", "--json"], project))
    names = {item["name"] for item in inventory if item["scope"] == "project"}
    if names != expected.keys():
        raise AssertionError(f"CLI inventory differs: {sorted(names)}")
    for route in REQUIRED_ROOTS:
        for name in expected:
            if not (project / route / name / "SKILL.md").is_file():
                raise AssertionError(f"Missing routed skill: {route}/{name}")

    entries = list(project.rglob("SKILL.md"))
    routes = {entry.parent.parent for entry in entries}
    for route in routes:
        installed = {p.name for p in route.iterdir() if (p / "SKILL.md").is_file()}
        if installed != expected.keys():
            raise AssertionError(f"Incomplete installation in {route}")
    for entry in entries:
        original = expected[entry.parent.name]
        for file in original.rglob("*"):
            if file.is_file():
                relative = file.relative_to(original)
                copied = entry.parent / relative
                if file.read_bytes() == copied.read_bytes():
                    continue
                # The CLI's Eve adapter removes the redundant name field and
                # reserializes frontmatter. Its description/body must survive.
                if relative == Path("SKILL.md") and entry.parent.parent == project / "agent/skills":
                    _, original_yaml, original_body = file.read_text().split("---", 2)
                    _, copied_yaml, copied_body = copied.read_text().split("---", 2)
                    expected_metadata = {"description": yaml.safe_load(original_yaml)["description"]}
                    if yaml.safe_load(copied_yaml) == expected_metadata and original_body.strip() == copied_body.strip():
                        continue
                raise AssertionError(f"Changed installed resource: {copied.relative_to(project)}")
        if not (original / "agents/openai.yaml").exists() and (entry.parent / "agents/openai.yaml").exists():
            raise AssertionError("Unexpected OpenAI metadata in portable installation")
    return len(expected), len(routes), len(entries)


def main():
    with tempfile.TemporaryDirectory(prefix="iphone-duo-agents-") as temporary:
        workspace = Path(temporary)
        for portable in (False, True):
            label = "standard-only" if portable else "with optional Codex metadata"
            source = workspace / ("portable-source" if portable else "full-source")
            shutil.copytree(ROOT / "skills", source / "skills")
            if portable:
                for file in (source / "skills").glob("*/agents/openai.yaml"):
                    file.unlink()
            project = workspace / ("portable-project" if portable else "full-project")
            project.mkdir()
            skills, routes, entries = verify(source, project)
            print(f"PASS ({label}): {skills} skills, {routes} installation directories, {entries} verified copies.")


if __name__ == "__main__":
    main()
