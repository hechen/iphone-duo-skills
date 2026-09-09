#!/usr/bin/env python3
"""Validate skill packaging, metadata, and local Markdown links."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]


def validate(root):
    root = Path(root).resolve()
    errors = []
    skills = sorted((root / "skills").glob("*/SKILL.md"))
    if not skills:
        errors.append("No skills found")
    for skill in skills:
        relative = skill.relative_to(root)
        text = skill.read_text()
        parts = text.split("---", 2)
        if len(parts) != 3 or parts[0].strip():
            errors.append(f"{relative}: missing frontmatter")
            continue
        try:
            meta = yaml.safe_load(parts[1])
            if not isinstance(meta, dict):
                raise ValueError("frontmatter must be a mapping")
            name = meta.get("name", "")
            if (not isinstance(name, str) or name != skill.parent.name
                    or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
                    or len(name) >= 64):
                errors.append(f"{relative}: invalid or mismatched name")
            if not isinstance(meta.get("description"), str) or not meta["description"].strip():
                errors.append(f"{relative}: missing description")
            ui = yaml.safe_load((skill.parent / "agents/openai.yaml").read_text())
            interface = ui["interface"]
            if not interface.get("display_name"):
                errors.append(f"{relative}: missing display name")
            short = interface.get("short_description", "")
            if not 25 <= len(short) <= 64:
                errors.append(f"{relative}: short description must be 25–64 characters")
            if "$" + name not in interface.get("default_prompt", ""):
                errors.append(f"{relative}: default prompt does not name the skill")
        except (ValueError, OSError, KeyError, TypeError, yaml.YAMLError) as error:
            errors.append(f"{relative}: {error}")

    # Only authored Markdown; never inspect dependency environments or git internals.
    markdown = list(root.glob("*.md")) + list((root / "skills").rglob("*.md"))
    for path in markdown:
        text = re.sub(r"```.*?```", "", path.read_text(), flags=re.S)
        relative = path.relative_to(root)
        for href in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text):
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            boundary = root
            if relative.parts[0] == "skills":
                boundary = root / "skills" / relative.parts[1]
            if target != boundary and boundary not in target.parents:
                errors.append(f"{relative}: link escapes package: {href}")
            elif not target.exists():
                errors.append(f"{relative}: broken link: {href}")
    return errors


if __name__ == "__main__":
    issues = validate(ROOT)
    for issue in issues:
        print(issue, file=sys.stderr)
    if issues:
        raise SystemExit(1)
    print("Validated skill metadata and local links.")
