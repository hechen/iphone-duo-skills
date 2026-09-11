# iPhone Duo Skills

Reusable AI coding skills for preparing SwiftUI and UIKit apps for iPhone Duo. Each skill provides a focused engineering workflow, links to Apple sources, and checks for the behavior that matters.

Built on the [Agent Skills open format](https://agentskills.io/specification). Use the same seven skills with **Claude Code, Cursor, GitHub Copilot, Gemini CLI, Codex, OpenCode, Windsurf, Cline, Roo Code, Continue, Antigravity, OpenClaw**, and other compatible agents. See [agent compatibility](COMPATIBILITY.md) for installation routes and verification scope.

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

### Choose your agents

Run this inside the project where you want to use the skills. The interactive installer lets you select skills and agents:

```sh
npx skills@1.5.25 add hechen/iphone-duo-skills
```

Or select several agents explicitly:

```sh
npx skills@1.5.25 add hechen/iphone-duo-skills --skill '*' --agent claude-code cursor github-copilot gemini-cli codex
```

This uses the [open Skills CLI](https://github.com/vercel-labs/skills/tree/v1.5.25); version 1.5.25 requires Node.js 22.20+. Add `--global` for a user-wide installation. Keep the default project scope for a shared application repository. The external CLI manages its own overwrite and update behavior.

### Install without Node.js

The bundled Python installer accepts any skill directory. For example, install all seven into a Claude Code project:

```sh
git clone https://github.com/hechen/iphone-duo-skills.git
cd iphone-duo-skills
python3 scripts/install.py --dest /path/to/your-app/.claude/skills
```

For agents using the shared project directory, or a Codex user installation:

```sh
python3 scripts/install.py --dest /path/to/your-app/.agents/skills
python3 scripts/install.py --dest "${CODEX_HOME:-$HOME/.codex}/skills" iphone-duo-readiness iphone-duo-layout
```

Use the [compatibility guide](COMPATIBILITY.md) to choose a directory supported by your agent. The Python installer uses Python 3.9+ and the standard library. It refuses to replace existing skill folders. To update, first review changes and move the old installation aside. To uninstall, remove only the installed `iphone-duo-*` folders you selected.

`SKILL.md` and its relative references contain the complete instructions. `agents/openai.yaml` is optional Codex UI metadata; other agents do not need it. We validate and test installation both with and without that metadata. There are no required OpenAI tools, credentials, or model APIs.

## Example requests

```text
Use the iphone-duo-readiness skill to audit this app. Identify concrete code locations,
prioritize fixes, and distinguish work possible with my SDK from deferred work.

Use the iphone-duo-layout skill to adapt this player and transcript screen. Preserve
playback, transcript position, and selection while the layout changes.

Use the iphone-duo-camera skill to review our capture pipeline for display transitions.
Keep our current deployment target and explain the camera-selection tradeoff.

Use the iphone-duo-testing skill to verify our compose flow while resizing, changing
displays, showing the keyboard, and presenting a sheet. Record untested cases.
```

Use your agent's skill picker or invocation syntax if it offers one. If it cannot discover skill folders, ask it to read the selected `SKILL.md` and follow its relative references; that is manual use, not automatic skill discovery.

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
.venv/bin/python scripts/smoke_agents.py
```

The cross-agent smoke test requires Node.js 22.20+, npm, and network access. It uses disposable project directories and never installs skills globally. CI runs it alongside the Python checks.

See [CONTRIBUTING.md](CONTRIBUTING.md) for source and validation requirements. Original repository content is available under the [MIT License](LICENSE); linked Apple materials retain their own terms.
