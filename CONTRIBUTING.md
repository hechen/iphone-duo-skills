# Contributing

Keep changes focused on decisions an agent would otherwise get wrong when adapting an app for iPhone Duo.

- Cite a public Apple source and a section or timestamp for new platform claims. Identify your own engineering recommendations separately.
- Check new declarations and availability against the SDK you actually used. Report its Xcode build, SDK version, deployment target, and validation result. Until verified, describe symbols as session references rather than compiled examples.
- Preserve independently installable skills: local references must remain inside that skill folder. Avoid copying entire transcripts or proprietary examples.
- Exercise a realistic request with the affected skill. Record the request, observed result, and limitations. Do not equate a packaging check with a behavioral evaluation.
- Keep the shared `SKILL.md` independent of vendor manifests and invocation syntax. Check vendor extensions only when present; do not make them a prerequisite for other agents.
- For an agent compatibility claim, cite its loader documentation or the pinned installer's registry. Distinguish package installation from execution inside that agent.
- Run `scripts/validate.py`, the unit tests, and `scripts/smoke_agents.py` using the README instructions.
- Use synthetic examples and redact private data from screenshots, logs, and issue reports.

For a bug, include the skill name, the request that triggered it, the incorrect result, and the expected decision. For API corrections, include the authoritative URL and SDK evidence if available.
