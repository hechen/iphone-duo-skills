# Agent compatibility

Verified **2026-09-11**. The content uses the [Agent Skills specification](https://agentskills.io/specification): a `SKILL.md` entrypoint with `name` and `description`, plus relative references. One source folder serves every agent.

## Installation routes

The [Skills CLI v1.5.25 agent registry](https://github.com/vercel-labs/skills/blob/v1.5.25/src/agents.ts) supplies routing for these examples and many additional agents:

| Agent | CLI target |
| --- | --- |
| Claude Code | `claude-code` |
| Cursor | `cursor` |
| GitHub Copilot | `github-copilot` |
| Gemini CLI | `gemini-cli` |
| Codex | `codex` |
| OpenCode | `opencode` |
| Windsurf / Cascade | `windsurf` |
| Cline | `cline` |
| Roo Code | `roo` |
| Continue | `continue` |
| Antigravity | `antigravity` |
| OpenClaw | `openclaw` |
| Goose | `goose` |
| Qwen Code | `qwen-code` |

Use `--agent` with the desired identifiers. Consult the [complete upstream list](https://github.com/vercel-labs/skills/tree/v1.5.25#supported-agents) for other targets. To install all skills to every CLI target in the current project:

```sh
npx skills@1.5.25 add hechen/iphone-duo-skills --all
```

This intentionally creates directories for agents you may not use. Selecting specific agents is usually more convenient. Do not mix installation managers for the same destination.

## Manual directory choices

For `scripts/install.py --dest`, these first-party docs identify supported project directories:

| Agent documentation | Project directory |
| --- | --- |
| [Claude Code](https://code.claude.com/docs/en/skills) | `.claude/skills/` |
| [Cursor](https://prod.cursor.com/docs/skills) | `.cursor/skills/` |
| [GitHub Copilot](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) | `.github/skills/` or `.agents/skills/` |
| [Gemini CLI](https://geminicli.com/docs/cli/using-agent-skills/) | `.gemini/skills/` or `.agents/skills/` |
| [OpenCode](https://opencode.ai/docs/skills/) | `.opencode/skills/` or `.agents/skills/` |
| [Windsurf / Cascade](https://docs.windsurf.com/windsurf/cascade/skills) | `.windsurf/skills/` |

These are manual choices, not a promise that the CLI always chooses the same alias. It can route several agents through `.agents/skills/`. Copy the entire selected skill folder, including `references/`, into the chosen directory. Then use the agent's documented discovery/reload flow.

For an agent without native skills, explicitly provide the entrypoint and allow it to read the linked references. Do not rename `SKILL.md` to a rule or system-instruction file and assume equivalent behavior: loading and invocation semantics differ.

## What has been verified

- **Packaging:** all seven skills validate without `agents/openai.yaml`. The optional metadata is checked when present.
- **CLI installation:** `scripts/smoke_agents.py` installs all seven to every project target exposed by the pinned CLI and verifies CLI inventory. On the verification date this produced 55 distinct installation directories and 385 skill copies per run. It repeats this with all OpenAI metadata removed. Files must match exactly except for the CLI's Eve frontmatter conversion, where the test checks the description and instruction body; reference files still match byte for byte.
- **Host execution:** this does not run Claude, Cursor, Copilot, or every other agent. Their native discovery UI, automatic selection, and task execution have not been end-to-end tested here.
- **Apple tooling:** reading and reviewing the skills is platform-independent. Building or running iOS apps still needs an appropriate macOS/Xcode environment; a cloud agent without one must report those checks as unperformed.

No `claude.yaml`, `cursor.yaml`, or other invented vendor manifest is needed. Agents consume the shared entrypoint through their own skill loaders. Preserve vendor extensions only when that vendor documents and uses them.
