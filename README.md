# iPhone Duo Skills

Reusable AI coding skills for preparing SwiftUI and UIKit apps for iPhone Duo. Each skill provides a focused engineering workflow, links to Apple sources, and checks for the behavior that matters.

**Status: announcement-day edition, September 9, 2026.** Apple has published developer sessions; its [developer hub](https://developer.apple.com/iphone-duo/) currently lists Xcode 27.1 beta and the detailed preparation article as coming later this month. New API names below were verified against those session pages, **not compiled against the iOS 27.1 SDK**. Recheck availability and declarations before implementation.

This is an independent community resource. It is not affiliated with Apple and is separate from Apple's App Resizability skill discussed in the preparation session.

## Choose a skill

| Skill | Use it to |
| --- | --- |
| [iphone-duo-readiness](skills/iphone-duo-readiness/SKILL.md) | Audit an existing app and prioritize a migration grounded in its actual toolchain. |
| [iphone-duo-design](skills/iphone-duo-design/SKILL.md) | Review information hierarchy, reachability, presentations, and continuity across configurations. |
| [iphone-duo-layout](skills/iphone-duo-layout/SKILL.md) | Adapt custom layouts using reserved regions and arrangements. |
| [iphone-duo-toolbars](skills/iphone-duo-toolbars/SKILL.md) | Prepare navigation, toolbar items, custom controls, and overflow for vertical bars. |
| [iphone-duo-scenes](skills/iphone-duo-scenes/SKILL.md) | Handle multiple scenes, hinge-driven interactions, and display accessories. |
| [iphone-duo-camera](skills/iphone-duo-camera/SKILL.md) | Preserve camera direction, rotation, capture ownership, and previews when displays change. |
| [iphone-duo-testing](skills/iphone-duo-testing/SKILL.md) | Build and execute a transition-based QA matrix with explicit evidence gaps. |

## Install

Clone this public repository and install all seven skills for Codex:

```sh
git clone https://github.com/hechen/iphone-duo-skills.git
cd iphone-duo-skills
python3 scripts/install.py --dest "${CODEX_HOME:-$HOME/.codex}/skills"
```

Install selected skills instead:

```sh
python3 scripts/install.py --dest "${CODEX_HOME:-$HOME/.codex}/skills" iphone-duo-readiness iphone-duo-layout
```

The installer uses Python 3.9+ and the standard library. It refuses to replace existing skill folders. To update, first review changes and move the old installation aside. To uninstall, remove only the installed `iphone-duo-*` folders you selected.

The `SKILL.md` instructions and relative references are portable Markdown. `agents/openai.yaml` contains Codex UI metadata. For another agent, use its documented skill directory or provide the appropriate `SKILL.md` directly; automatic discovery outside Codex has not been tested.

## Example requests

```text
Use $iphone-duo-readiness to audit this app. Identify concrete code locations,
prioritize fixes, and distinguish work possible with my SDK from deferred work.

Use $iphone-duo-layout to adapt this player and transcript screen. Preserve
playback, transcript position, and selection while the layout changes.

Use $iphone-duo-camera to review our capture pipeline for display transitions.
Keep our current deployment target and explain the camera-selection tradeoff.

Use $iphone-duo-testing to verify our compose flow while resizing, changing
displays, showing the keyboard, and presenting a sheet. Record untested cases.
```

## Evidence and compatibility

- [Sources](SOURCES.md) maps the skills to Apple's six announcement sessions.
- Every skill includes a local reference distinguishing session guidance from repository recommendations.
- SDK availability is a separate question from runtime availability: `if #available` cannot make a symbol compile in an older SDK.
- No private projects, credentials, Apple artwork, or copied session transcripts are included.
- Repository validation checks packaging and local links. It does not certify app behavior, simulator coverage, or device support.

## Validate and contribute

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s tests -v
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for source and validation requirements. Original repository content is available under the [MIT License](LICENSE); linked Apple materials retain their own terms.
