# Agent compatibility

Checked **2026-09-25**. The skills use the [Agent Skills specification](https://agentskills.io/specification): a `SKILL.md` entrypoint with `name` and `description` frontmatter, a concise body, and relative `references/`. One source folder serves every agent. Install all eight skill folders together; `iphone-duo-development` routes to the others by name.

## Option A: Skills CLI

From your application repository:

```sh
npx skills@1.5.25 add hechen/iphone-duo-skills --skill '*' --agent claude-code
```

The [Skills CLI v1.5.25 agent registry](https://github.com/vercel-labs/skills/blob/v1.5.25/src/agents.ts) supplies these targets, among many others:

| Agent | CLI target | Project directory the CLI uses |
| --- | --- | --- |
| Claude Code | `claude-code` | `.claude/skills/` |
| Codex | `codex` | `.agents/skills/` |
| Cursor | `cursor` | `.agents/skills/` |
| GitHub Copilot | `github-copilot` | `.agents/skills/` |
| Gemini CLI | `gemini-cli` | `.agents/skills/` |
| OpenClaw | `openclaw` | `skills/` (workspace) |
| OpenCode | `opencode` | `.agents/skills/` |
| Windsurf / Cascade | `windsurf` | `.windsurf/skills/` |
| Cline | `cline` | `.agents/skills/` |
| Roo Code | `roo` | `.roo/skills/` |
| Continue | `continue` | `.continue/skills/` |
| Antigravity | `antigravity` | `.agents/skills/` |
| Amp | `amp` | `.agents/skills/` |
| Goose | `goose` | `.goose/skills/` |
| Qwen Code | `qwen-code` | `.qwen/skills/` |

Several IDs can follow `--agent`. Add `--global` for a user-wide install, `--copy` when symlinks are unsuitable, and `--yes` only for noninteractive runs. `--all` installs to every CLI target and creates directories for agents you may not use. Do not mix installation managers for the same destination.

## Option B: GitHub CLI

GitHub CLI 2.97.0 includes `gh skill` as a preview:

```sh
gh skill install hechen/iphone-duo-skills --all --agent claude-code
gh skill install hechen/iphone-duo-skills --all --agent codex --scope user
```

Run one command per agent. `--pin <tag-or-commit>` gives a reproducible version, and `--dir` installs into a custom directory. The GitHub CLI adds source-tracking metadata to each installed `SKILL.md` frontmatter so `gh skill update` can find changes. Avoid `--force` over locally edited skills. See the [GitHub CLI manual](https://cli.github.com/manual/gh_skill_install).

## Option C: Python installer or manual copy

`python3 scripts/install.py --dest <directory> [skill ...]` copies whole skill folders, refuses to overwrite anything, and works without Node.js. Copying by hand works too; keep each folder's name and its `references/` and `agents/` contents.

Directories each agent's own documentation lists:

| Agent | Project | User-wide | Source |
| --- | --- | --- | --- |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | [Claude Code skills](https://code.claude.com/docs/en/skills) |
| Codex | `.agents/skills/` (current folder, its parent, or the repository root) | `~/.agents/skills/` | [Codex skills](https://developers.openai.com/codex/skills) |
| Cursor | `.agents/skills/` or `.cursor/skills/` | `~/.agents/skills/` or `~/.cursor/skills/` | [Cursor skills](https://cursor.com/docs/skills) |
| GitHub Copilot | `.github/skills/`, `.claude/skills/`, or `.agents/skills/` | `~/.copilot/skills/` or `~/.agents/skills/` | [About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) |
| Gemini CLI | `.agents/skills/` or `.gemini/skills/` | `~/.agents/skills/` or `~/.gemini/skills/` | [Gemini CLI skills](https://geminicli.com/docs/cli/skills/) |
| OpenClaw | `<workspace>/skills/` or `<workspace>/.agents/skills/` | `~/.agents/skills/`, or `skills/` in OpenClaw's state directory | [OpenClaw skills](https://docs.openclaw.ai/tools/skills) |
| OpenCode | `.opencode/skills/` or `.agents/skills/` | See source | [OpenCode skills](https://opencode.ai/docs/skills/) |
| Windsurf / Cascade | `.windsurf/skills/` | See source | [Cascade skills](https://docs.windsurf.com/windsurf/cascade/skills) |

`.agents/skills/` is the most widely shared project location. Some agents scan more than one directory; Cursor and Copilot also read `.claude/skills/`. Install one copy per agent's search path so the same skill does not appear twice. For Codex user-wide installs, the Skills CLI v1.5.25 `--global` route writes to `$CODEX_HOME/skills` (default `~/.codex/skills`), while Codex's documentation lists `~/.agents/skills`; if a user-wide install is not discovered, check which directory your Codex version scans.

## Agents that read only AGENTS.md

Some agents have no skill loader but read an `AGENTS.md` file at the repository root. Install the folders to `.agents/skills/` and add a short note to the app's `AGENTS.md`:

```markdown
## iPhone Duo work

For iPhone Duo (foldable iPhone) layout, toolbar, scene, camera, or testing work, read
`.agents/skills/iphone-duo-development/SKILL.md` first and follow its routing to the
matching `.agents/skills/iphone-duo-*/SKILL.md`. Read a skill's `references/` files when
the skill points to them.
```

This gives the agent the instructions as ordinary context. It does not create automatic discovery, slash commands, or tool permissions. The same approach works for any agent you can point at a file: give it the entrypoint path and let it read the linked references. Do not rename `SKILL.md` to a rules or system-prompt file and assume the same behavior.

## Activate and verify

1. Reload the agent's skill list or start a new session if the agent requires it.
2. Confirm `iphone-duo-development` appears in the agent's skill list or picker, where it has one.
3. Ask the agent to use it on a bounded task, such as listing the app's targets and the Duo work that needs the iOS 27.1 SDK.
4. Check that it can open a skill's `references/` file. An install that copied only `SKILL.md` files is incomplete.

Explicit invocation differs by agent: Codex uses `$iphone-duo-development`, Claude Code uses `/iphone-duo-development`, and other agents use a picker, an `@` mention, or plain language. The skills do not depend on any of these internally.

## Updating

Use the same installer and scope as the original install. Review upstream changes before replacing local edits. Teams can pin a tag or commit with the GitHub CLI, or vendor a reviewed snapshot into the app repository. The Python installer never overwrites; move the old folders aside first.

## Vendor metadata

`agents/openai.yaml` is optional Codex interface metadata (display name, short description, default prompt). Other agents ignore it, and every skill validates and installs without it. No `claude.yaml`, `cursor.yaml`, or other invented manifest is needed. Keep vendor extensions only when that vendor documents and uses them.

## What has been verified

- **Packaging:** `scripts/validate.py` checks every skill's frontmatter against the specification (name format and match with the folder, description length, optional fields), entrypoint length, links that stay inside the skill folder, reference files that the entrypoint actually links, and that `iphone-duo-development` routes to every other skill. All eight skills also validate with `agents/openai.yaml` removed. `gh skill publish --dry-run` (GitHub CLI 2.97.0) reported no skill errors on 2026-09-25.
- **Skills CLI installation:** `scripts/smoke_agents.py` installs all eight skills to every project target the pinned CLI exposes, in disposable projects, with and without the optional metadata, and checks the CLI inventory and file contents. On 2026-09-25 each run produced 55 installation directories and 440 verified skill copies. Files must match exactly except for the CLI's Eve frontmatter conversion, which drops the `name` field; there every other field and the body are compared.
- **GitHub CLI installation:** `gh skill install --from-local . --all --dir <temporary directory>` installed all eight skills with their references (GitHub CLI 2.97.0, 2026-09-25).
- **Host execution:** these checks do not launch Claude Code, Codex, Cursor, Copilot, or any other agent. Native discovery, automatic selection, and task quality have not been tested end to end.
- **Apple tooling:** reading the skills needs no Mac. Building or running iOS apps needs macOS and Xcode; an agent without them must report those checks as not performed. `scripts/check-sdk.sh` needs Xcode 27.1 or later.
