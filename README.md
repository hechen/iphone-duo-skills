<div align="center">

# iPhone Duo Skills

**Help your coding agent adapt SwiftUI, UIKit, and AVFoundation apps to iPhone Duo.**

Eight portable agent skills grounded in Apple documentation and type-checked against the iOS 27.1 SDK.

[Install](#install) · [Choose a skill](#choose-a-skill) · [What's new](CHANGELOG.md) · [Sources](SOURCES.md) · [Agent compatibility](COMPATIBILITY.md)

</div>

<a href="https://developer.apple.com/iphone-duo/">
  <img src="https://developer.apple.com/iphone-duo/images/main_2x.png" alt="Apple's iPhone Duo opened to show its large inner display and central fold" width="900">
</a>

<sub>iPhone Duo illustration © Apple Inc. Source: [Get ready for iPhone Duo](https://developer.apple.com/iphone-duo/). This is Apple's device illustration, not an app built or tested by this project. [Image credits](IMAGE-CREDITS.md).</sub>

iPhone Duo folds: an app moves between a compact outer display and a large inner display, a fold can divide the screen, bars move to the side, and a front camera can end up facing the other way. These skills give an agent a focused workflow for each of those changes, the Apple sources behind it, and the checks that show whether the app still works.

Built on the [Agent Skills open format](https://agentskills.io/specification). The same folders work with **Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI, OpenClaw, OpenCode, Windsurf, Cline, Roo Code, Continue, Antigravity, Amp, Goose**, and agents that only read `AGENTS.md`. See [agent compatibility](COMPATIBILITY.md).

This is an independent community resource. It is not affiliated with Apple and is separate from Apple's App Resizability skill in Xcode 27.1.

## Companion to Apple Platforms 27 Skills

For iOS 27, iPadOS 27, macOS 27, SwiftUI migration, App Intents, Foundation Models, and Core AI, use [hechen/apple-platforms-27-skills](https://github.com/hechen/apple-platforms-27-skills). Its `apple-platforms-27` coordinator routes iPhone Duo work to this repository. The `iphone-duo-development` skill that used to live there moved here in September 2026 and now leads this collection. Install both collections when an app targets several Apple platforms.

## What's new in 1.0.0

- **One entry point.** `iphone-duo-development` sets the Xcode 27.1 baseline and routes to the seven focused skills.
- **Rechecked against Apple's written docs.** Apple has published the preparation article, the HIG page, API reference for every Duo symbol these skills use, and two camera articles. The references now cite them directly and record where sources disagree.
- **Corrected guidance.** Reserved-region queries are filtered on `isActive` explicitly, arrangement nesting follows the HIG and the article, camera direction follows Apple's coordinator guide, and the window-activation API has its real name. See the [changelog](CHANGELOG.md).
- **SDK-checked.** An [API probe](tests/iPhoneDuoProbe.swift) type-checks the Duo symbols with Xcode 27.1 (27A9269) for device and simulator targets.

**Toolchain note — September 25, 2026:** Apple's Xcode 27.2 beta notes direct Duo development to **Xcode 27.1 beta** for its SDK and simulator. Check which Xcode your project builds with before relying on a Duo API.

## Choose a skill

| Skill | Use it to |
| --- | --- |
| [iphone-duo-development](skills/iphone-duo-development/SKILL.md) | Start here: set the toolchain baseline, order the work, and route to the focused skills. |
| [iphone-duo-readiness](skills/iphone-duo-readiness/SKILL.md) | Audit an existing app and prioritize a migration grounded in its actual toolchain. |
| [iphone-duo-design](skills/iphone-duo-design/SKILL.md) | Review information hierarchy, reachability, presentations, and continuity across displays and poses. |
| [iphone-duo-layout](skills/iphone-duo-layout/SKILL.md) | Adapt custom layouts with reserved regions and split or overlay arrangements. |
| [iphone-duo-toolbars](skills/iphone-duo-toolbars/SKILL.md) | Prepare navigation, toolbar items, sheets, custom controls, and overflow for vertical bars. |
| [iphone-duo-scenes](skills/iphone-duo-scenes/SKILL.md) | Handle multiple windows, hinge-driven interactions, and camera-capture accessories. |
| [iphone-duo-camera](skills/iphone-duo-camera/SKILL.md) | Keep camera direction, mirroring, rotation, and capture ownership correct as displays change. |
| [iphone-duo-testing](skills/iphone-duo-testing/SKILL.md) | Build and run a pose and transition QA matrix with explicit evidence gaps. |

Install all eight together. The entry point names its siblings, and each skill folder stays self-contained, so any subset still loads.

## Install

### Skills CLI

Run this inside the project where you want the skills. The interactive installer lets you pick agents:

```sh
npx skills@1.5.25 add hechen/iphone-duo-skills --skill '*'
```

Or name the agents:

```sh
npx skills@1.5.25 add hechen/iphone-duo-skills --skill '*' --agent claude-code codex cursor github-copilot gemini-cli openclaw
```

This uses the [open Skills CLI](https://github.com/vercel-labs/skills/tree/v1.5.25); version 1.5.25 is the one our smoke test pins, and it needs Node.js 22.20+. Add `--global` for a user-wide installation. Keep the default project scope for a shared application repository.

### GitHub CLI

If your GitHub CLI has `gh skill` (preview in 2.97.0):

```sh
gh skill install hechen/iphone-duo-skills --all --agent claude-code
```

Use one command per agent, add `--scope user` for a user-wide install, and `--pin <tag-or-commit>` for a reproducible version.

### Without Node.js

The bundled Python installer (Python 3.9+, standard library only) copies skill folders into any directory and never overwrites existing ones:

```sh
git clone https://github.com/hechen/iphone-duo-skills.git
cd iphone-duo-skills
python3 scripts/install.py --dest /path/to/your-app/.claude/skills   # Claude Code
python3 scripts/install.py --dest /path/to/your-app/.agents/skills   # Codex, Cursor, Copilot, Gemini CLI, and others
python3 scripts/install.py --dest ~/.agents/skills iphone-duo-development iphone-duo-layout   # user-wide subset for Codex, Cursor, Copilot, Gemini CLI, or OpenClaw
```

[Agent compatibility](COMPATIBILITY.md) lists each agent's directories, explains activation, and shows how to point an `AGENTS.md`-only agent at the skills. To update, review the changes and move the old folders aside first. To uninstall, remove only the `iphone-duo-*` folders you installed.

`SKILL.md` and its relative references contain the complete instructions. `agents/openai.yaml` is optional Codex UI metadata that other agents ignore. There are no required tools, MCP servers, credentials, or model APIs.

## Example requests

```text
Use iphone-duo-development to assess this app for iPhone Duo. Keep our deployment
target, fix what compiles with our current SDK, and list what needs Xcode 27.1.

Use iphone-duo-layout to adapt this player and transcript screen. Preserve
playback, transcript position, and selection while the device folds and opens.

Use iphone-duo-camera to review our capture pipeline for display changes.
Keep our current deployment target and explain the camera-selection tradeoff.

Use iphone-duo-testing to verify our compose flow while opening and closing the
device, showing the keyboard, and presenting a sheet. Record untested cases.
```

Use your agent's skill picker or invocation syntax if it has one; for example, Codex uses `$iphone-duo-development` and Claude Code accepts `/iphone-duo-development`. Naming the skill in plain language also works.

## Evidence

- [Sources](SOURCES.md) maps the skills to Apple's preparation article, HIG, API reference, camera guides, release notes, and supplementary Tech Talks, and records where they disagree.
- Every skill has a local reference that separates written documentation, session evidence, and repository recommendations.
- The [SDK probe](tests/iPhoneDuoProbe.swift) proves spelling and availability, not runtime behavior. Camera capture and accessory presentation still need a device.
- SDK availability is a separate question from runtime availability: `if #available` cannot make a symbol compile in an older SDK.
- No private projects, credentials, or copied session transcripts are included. The README embeds one Apple illustration by link; nothing from Apple is stored here.

## Validate and contribute

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/smoke_agents.py
bash scripts/check-sdk.sh   # macOS with Xcode 27.1 or later
```

The cross-agent smoke test needs Node.js 22.20+, npm, and network access. It uses disposable project directories and never installs skills globally. CI runs the Python checks and the smoke test on Linux; the SDK check needs a Mac and is run by maintainers.

See [CONTRIBUTING.md](CONTRIBUTING.md) for source and validation requirements. Original repository content is available under the [MIT License](LICENSE). Apple images are embedded from Apple's site, credited in [image credits](IMAGE-CREDITS.md), and not covered by this repository's license; linked Apple materials keep their own terms.
