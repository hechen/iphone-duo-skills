# Contributing

Keep changes focused on decisions an agent would otherwise get wrong when adapting an app for iPhone Duo.

## Sources

- Prefer Apple's written API reference for declarations and availability, the preparation article and HIG for behavior and design, and release notes for toolchain facts. Use Tech Talk timestamps for explanations the written material does not cover. Cite the specific source for every new claim and label repository recommendations separately.
- Check new declarations against the SDK you used. Report its Xcode build, SDK version, deployment target, and result. If a symbol belongs in the probe, add it to `tests/iPhoneDuoProbe.swift` and run `bash scripts/check-sdk.sh`.
- When sources disagree, record both in the affected reference and in [SOURCES.md](SOURCES.md) instead of picking one silently.
- A field observation (behavior you saw, not something Apple documents) goes in the relevant reference under a "Field observations" heading, with the date, Xcode build, runtime build, and what was and was not checked. Keep it out of the main `SKILL.md` instructions, and never turn one into a workaround that hides a failure, such as a retry tap.

## Skills

- Follow the [Agent Skills specification](https://agentskills.io/specification): `name` matches the folder, the `description` says what the skill does and when to use it with the words a user would type, and the body stays concise with detail in `references/`.
- Keep every skill independently installable: links must stay inside that skill folder. Refer to sibling skills by name. `iphone-duo-development` routes to every other skill; update its table when the set changes.
- Keep the shared `SKILL.md` independent of vendor manifests and invocation syntax. Validate vendor extensions only when present; do not make them a prerequisite for other agents.
- Avoid copying transcripts or proprietary examples. Use synthetic examples and redact private data from screenshots, logs, and issue reports.
- Exercise a realistic request with the affected skill. Record the request, the result, and its limits. A packaging check is not a behavioral evaluation.

## Agent compatibility

For an agent compatibility claim, cite the agent's loader documentation or the pinned installer's registry, with the date you checked. Keep package installation separate from execution inside that agent.

## Validate locally

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/smoke_agents.py
```

On a Mac with Xcode 27.1 or later, also run `bash scripts/check-sdk.sh`. CI runs the portable checks on Linux and does not need Xcode.

For a bug, include the skill name, the request that triggered it, the incorrect result, and the expected decision. For API corrections, include the authoritative URL and SDK evidence if available.
