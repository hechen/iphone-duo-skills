---
name: iphone-duo-testing
description: Plan and execute iPhone Duo app QA across display changes, resizing, keyboard and presentation states, accessibility, and capability loss with reproducible evidence.
---

# iPhone Duo testing

Read [test matrix](references/test-matrix.md). Build a matrix around the requested flows and the actual available environment. Record the candidate revision/build, Xcode build, SDK, runtime/device, and relevant settings.

## Discover before executing

Use `xcodebuild -version`, `xcodebuild -showsdks`, and `xcrun simctl list devices available` when available. Discover the project's scheme and destinations. Never invent a device identifier or a fold-control CLI flag. Use supported simulator UI or documented automation for physical configurations.

If Duo tooling is absent, continue meaningful resize, model, and existing-platform tests. Label those results as proxies. Leave actual Duo transitions untested rather than converting proxy coverage into device validation.

## Exercise transitions

Select a real task with state: an unsaved draft, selected item, queued upload, or playing video. Establish the initial state, apply the transition, and then complete or cancel the task. Verify both visible UI and persistent output.

Test intermediate constraints, not just launch at two endpoint sizes. Check that asynchronous work runs the intended number of times, navigation remains coherent, and focus does not disappear into a hidden view. Include error recovery for features that depend on a camera or accessory.

Use automated assertions for stable observable outcomes. Use screenshots for layout evidence and interaction checks for reachability and accessibility. An accessibility audit supplements manual assistive-technology testing; it does not replace it.

## Report

For each scenario, record `precondition / action / expected / observed / environment / evidence / status`. Use `pass`, `fail`, `blocked`, or `not run`; give a reason for missing evidence. Link relevant screenshots, recordings, test results, or logs using synthetic or redacted data.

Finish with failures ranked by user impact, verified scope, and the remaining device-specific checks. A green build certifies neither correct folding behavior nor submission readiness.
