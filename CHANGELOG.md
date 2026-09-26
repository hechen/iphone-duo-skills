# Changelog

## 1.0.0 — 2026-09-25

This repository is now the single home for iPhone Duo skills. The `iphone-duo-development` skill and its references moved here from [hechen/apple-platforms-27-skills](https://github.com/hechen/apple-platforms-27-skills), which now points to this collection.

### Added

- `iphone-duo-development`, the entry point: toolchain baseline, work order, routing to the seven focused skills, guidance for other UI stacks, and an API map with Apple links and availability.
- `tests/iPhoneDuoProbe.swift` and `scripts/check-sdk.sh`, which type-check the Duo SwiftUI, UIKit, AVKit, and AVFoundation symbols for `arm64-apple-ios27.1` and its simulator. Xcode 27.1 (27A9269) passes; Xcode 27.0 (27A266a) fails as expected.
- Toolchain facts from the Xcode 27.1 and 27.2 beta notes: Duo uses the 27.1 beta SDK and simulator, Mac Catalyst needs compile-time guards, and the Duo simulator runtime lacks StandBy and most app-extension debugging.
- Apple's bar placement rules (split view columns, inspectors, sheets, Split View multitasking), item representation rules, vertical bar compression, and the vertical bar opt-out guidance.
- Camera-capture accessory registration in SwiftUI and UIKit, availability versus the person's on/off choice, and the scene-role and scene-manifest details.
- The virtual front camera, the direction coordinator's device list and lifecycle, and Apple's mirroring and rotation steps.
- A merged pose and transition matrix, Duo screenshot sizes, and a clearly labeled field observation about sheet detents during XCUITest typing.
- `license: MIT` in every skill's frontmatter, `IMAGE-CREDITS.md`, `AGENTS.md`, GitHub CLI and `AGENTS.md`-only installation routes, and validator checks for frontmatter fields outside the specification, entrypoint length, unlinked reference files, and routing from the entry point.

### Changed

- References now start from Apple's published [preparation article](https://developer.apple.com/documentation/technologyoverviews/preparing-your-app-for-iphone-duo), HIG page, and API reference; the Tech Talks are supplementary.
- Reserved regions: filter on `isActive` explicitly. Apple's written overview says the query returns inactive regions too, which contradicts the earlier session-based statement that only active regions come back by default.
- Arrangement nesting: keep navigation outside arrangements (HIG) and do not put an arrangement inside a list or scroll view (preparation article).
- Scenes: the window activation API is `UIWindowScene.ActivationAction` (`UIWindowSceneActivationAction` in Objective-C), not `UIWindowSceneActivation`.
- Camera-capture accessory conditions follow the written article (app in the foreground, capture session running, capture interface on the inner display).
- `toolbarVerticalEdge` and `verticalBarEdge` report the preferred edge even when no vertical bar is visible.
- Codex user-wide installs use `~/.agents/skills`, as Codex's documentation now lists.

### Removed

- Statements that Xcode 27.1 beta and the preparation article were still to come, that standalone references for the Duo APIs could not be found, and that no Duo API had been compiled here.

## Before 1.0.0

- **2026-09-11:** Cross-agent installation with a Python installer and a pinned Skills CLI smoke test; optional Codex metadata; references reordered to start with Apple's written documentation.
- **2026-09-09:** Seven source-backed iPhone Duo skills: readiness, design, layout, toolbars, scenes, camera, and testing.
