# Contributing

Keep changes focused on decisions an agent would otherwise get wrong when adapting an app for iPhone Duo.

- Cite a public Apple source and a section or timestamp for new platform claims. Identify your own engineering recommendations separately.
- Check new declarations and availability against the SDK you actually used. Report its Xcode build, SDK version, deployment target, and validation result. Until verified, describe symbols as session references rather than compiled examples.
- Preserve independently installable skills: local references must remain inside that skill folder. Avoid copying entire transcripts or proprietary examples.
- Exercise a realistic request with the affected skill. Record the request, observed result, and limitations. Do not equate a packaging check with a behavioral evaluation.
- Run `scripts/validate.py` and the unit tests using the README instructions.
- Use synthetic examples and redact private data from screenshots, logs, and issue reports.

For a bug, include the skill name, the request that triggered it, the incorrect result, and the expected decision. For API corrections, include the authoritative URL and SDK evidence if available.
