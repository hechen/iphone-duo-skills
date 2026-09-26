#!/usr/bin/env python3
"""Validate skill packaging, metadata, and local Markdown links."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
ROUTER = "iphone-duo-development"
# Fields defined by https://agentskills.io/specification. Anything else is
# vendor-specific and would not travel to every agent.
SPEC_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
MAX_ENTRY_LINES = 500
LINK = re.compile(r"\[[^\]]*\]\(([^\s)]+)\)")


def local_links(path):
    """Yield (href, resolved target) for relative Markdown links outside code fences."""
    text = re.sub(r"```.*?```", "", path.read_text(), flags=re.S)
    for href in LINK.findall(text):
        parsed = urlsplit(href)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        yield href, (path.parent / unquote(parsed.path)).resolve()


def validate_frontmatter(meta, skill, relative):
    errors = []
    name = meta.get("name", "")
    if (not isinstance(name, str) or name != skill.parent.name
            or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
            or len(name) > 64):
        errors.append(f"{relative}: invalid or mismatched name")
    description = meta.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        errors.append(f"{relative}: description must be 1–1024 characters")
    unknown = sorted(set(meta) - SPEC_FIELDS)
    if unknown:
        errors.append(f"{relative}: frontmatter fields outside the Agent Skills specification: {', '.join(unknown)}")
    compatibility = meta.get("compatibility")
    if compatibility is not None and (not isinstance(compatibility, str)
                                      or not 1 <= len(compatibility) <= 500):
        errors.append(f"{relative}: compatibility must be 1–500 characters")
    metadata = meta.get("metadata")
    if metadata is not None and (not isinstance(metadata, dict) or not all(
            isinstance(key, str) and isinstance(value, str) for key, value in metadata.items())):
        errors.append(f"{relative}: metadata must map strings to strings")
    for field in ("license", "allowed-tools"):
        if field in meta and not isinstance(meta[field], str):
            errors.append(f"{relative}: {field} must be a string")
    return errors


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
        if len(text.splitlines()) > MAX_ENTRY_LINES:
            errors.append(f"{relative}: longer than {MAX_ENTRY_LINES} lines; move detail into references/")
        try:
            meta = yaml.safe_load(parts[1])
            if not isinstance(meta, dict):
                raise ValueError("frontmatter must be a mapping")
            errors.extend(validate_frontmatter(meta, skill, relative))
            name = meta.get("name", "")
            # Progressive disclosure only works if the entrypoint points at its references.
            linked = {target for _, target in local_links(skill)}
            for reference in sorted((skill.parent / "references").rglob("*")):
                if reference.is_file() and reference.resolve() not in linked:
                    errors.append(f"{relative}: reference not linked from SKILL.md: "
                                  f"{reference.relative_to(skill.parent)}")
            # Agent Skills need no vendor metadata. Validate Codex's extension only
            # when present, so a standards-only package remains independently valid.
            ui_path = skill.parent / "agents/openai.yaml"
            if not ui_path.exists():
                continue
            ui = yaml.safe_load(ui_path.read_text())
            if not isinstance(ui, dict) or not isinstance(ui.get("interface"), dict):
                raise ValueError("OpenAI UI metadata must contain an interface mapping")
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

    # The entry point must route to every other skill in the collection.
    router = root / "skills" / ROUTER / "SKILL.md"
    if router.is_file():
        routed = router.read_text()
        for skill in skills:
            other = skill.parent.name
            if other != ROUTER and f"`{other}`" not in routed:
                errors.append(f"{router.relative_to(root)}: does not route to {other}")

    # Only authored Markdown; never inspect dependency environments or git internals.
    markdown = list(root.glob("*.md")) + list((root / "skills").rglob("*.md"))
    for path in markdown:
        relative = path.relative_to(root)
        for href, target in local_links(path):
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
    count = len(list((ROOT / "skills").glob("*/SKILL.md")))
    print(f"Validated {count} skills: metadata, routing, references, and local links.")
