# Working on this repository

This repository publishes portable Agent Skills for adapting iPhone apps to iPhone Duo. These notes are for agents and people editing the skills, not for apps that install them.

- Read [CONTRIBUTING.md](CONTRIBUTING.md) and [SOURCES.md](SOURCES.md) before editing a skill.
- Keep one canonical copy of each skill under `skills/`. Do not fork instructions per agent.
- Keep every skill folder self-contained: links from a skill may only point inside that folder. Refer to sibling skills by name, not by relative path.
- `iphone-duo-development` is the entry point. When you add, rename, or remove a skill, update its routing table, the README catalog, and the changelog.
- Tie every API claim to an Apple source link and a check date. Label session-only statements, repository recommendations, and field observations as such.
- Keep `agents/openai.yaml` optional; the core instructions must work without it.
- Run `scripts/validate.py` and the unit tests for any change, `scripts/smoke_agents.py` for packaging changes, and `scripts/check-sdk.sh` on a Mac with Xcode 27.1 or later when you change a probe-covered API.
- Do not describe an installer smoke check as an end-to-end agent test, or a type-check as runtime evidence.
