---
name: iphone-duo-readiness
description: Audit an existing SwiftUI or UIKit app for iPhone Duo readiness and prioritize a migration using its actual SDK, layouts, navigation, and scene model.
---

# iPhone Duo readiness

Produce a concrete migration assessment before broad edits. Read [platform evidence](references/platform.md) for announcement-specific constraints and current verification status.

## Establish the baseline

Inspect repository instructions, supported platforms, deployment targets, project generation inputs, and the app's main flows. Record the selected Xcode and installed SDKs with `xcodebuild -version` and `xcodebuild -showsdks`. Discover actual destinations instead of assuming a Duo simulator is installed.

Separate improvements that compile today from work requiring a newer SDK. A runtime `#available` check cannot resolve a symbol absent from the build SDK. Do not increase a deployment target, change the team's selected Xcode, or install a beta as an incidental audit step.

## Trace assumptions to behavior

Search production sources and project configuration for candidates such as:

```sh
rg -n 'UIScreen\.main|UIDevice\.current\.orientation|userInterfaceIdiom|UIRequiresFullScreen|UISupportedInterfaceOrientations|supportedInterfaceOrientations' .
```

Treat matches as review leads. An idiom check for an unrelated platform behavior may be valid. Follow each layout use to its container, coordinate space, and owner; don't replace strings mechanically. Inspect manually positioned overlays, fixed toolbar heights, cached screen metrics, and separate compact/regular view trees that may recreate editor state.

For each issue, explain a user-visible trigger, the responsible code location, a scoped remedy, and how to reproduce and verify it. Rank data loss or unavailable primary actions above cosmetic spacing. Keep public interfaces and existing platform behavior intact unless the requested change requires otherwise.

## Deliver or implement within scope

For an audit, return prioritized findings, applicable SDK constraints, and a proposed sequence. For an implementation request, make the supported changes and run relevant checks; isolate deferred API adoption with its reason.

Use a report table with `flow / file / failure / proposed change / evidence / remaining check`. Distinguish source review, compilation, simulator execution, and device execution. Never convert an unexecuted scenario into a pass.
