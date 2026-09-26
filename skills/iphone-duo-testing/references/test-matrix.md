# Transition matrix

## Written documentation — start here

Checked 2026-09-25:

- [Device Hub](https://developer.apple.com/documentation/xcode/device-hub) and [Running your app on simulated or physical devices](https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices): destinations, simulated devices, and physical-device runs. The Duo HIG points to Device Hub for previewing poses.
- [Configuring the environment of a simulated device](https://developer.apple.com/documentation/xcode/configuring-the-environment-of-a-simulated-device): appearance, accessibility, and simulator environment controls. Match the instructions to the installed Xcode.
- [Performing accessibility audits](https://developer.apple.com/documentation/accessibility/performing-accessibility-audits-for-your-app) and [Performing accessibility testing](https://developer.apple.com/documentation/accessibility/performing-accessibility-testing-for-your-app): automated inspection, including `XCUIApplication.performAccessibilityAudit`, plus testing with accessibility settings and assistive technologies. A passing audit does not establish complete accessibility.
- [Preparing your app for iPhone Duo](https://developer.apple.com/documentation/technologyoverviews/preparing-your-app-for-iphone-duo): check both displays closed, open, and partially folded, rotate in each pose, and visit every view, sheet, and popover.

## Tooling status

As checked 2026-09-25, the [developer hub](https://developer.apple.com/iphone-duo/) offers Xcode 27.1 beta for the Duo SDK and simulator, and the [Xcode 27.2 beta notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes) point back to 27.1 beta for Duo. The [Xcode 27.1 beta notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes) list these simulator limits:

- StandBy is unavailable in the iPhone Duo simulator runtime.
- Running and debugging most app extensions is unavailable in that runtime.
- The first simulator launch can take several minutes.
- The Previews canvas has a Display group for previewing content on a device's alternative display.

A simulator limitation is neither an app failure nor a pass. Simulator has no camera, so camera direction and camera-capture accessory presentation need a device.

In the [preparation session](https://developer.apple.com/videos/play/tech-talks/111461/), Device Hub's controls open, close, rotate, and fold the Duo simulator, and Split View is started by dragging the app by its home indicator to one side of the inner display.

## Scenarios

This matrix is a repository-authored QA proposal. Select rows relevant to the app; do not require camera or multi-scene work for unrelated apps.

| Scenario | State to establish | Verify after transition |
| --- | --- | --- |
| Closed outer display, both orientations | Main flows | Reachable navigation, independent safe-area insets, readable sheets. |
| Inner display, tall and wide | Selected detail and scrolled collection | Suitable columns, stable selection, no idiom-based layout. |
| Open and close during editing | Unsaved form with keyboard visible | Draft, focus, selection, scroll, and presentation kept; completion and cancel reachable. |
| Partial fold, book and tabletop poses | Interactive control near the center | Targets clear of active divisions; media and controls usable; state stable. |
| Rotation and constrained multitasking | Primary task in progress | Content fits; essential actions remain reachable. |
| Split View on each side | Two scenes or two apps | Correct control edge, scene-local geometry, no shared navigation by accident. |
| Sheet or popover while space changes | Anchored presentation with entered data | Presentation, anchor, dismissal, retained data. |
| Toolbar overflow under pressure | Editing mode with frequent actions; keyboard or Picture in Picture shown | Correct labels, enabled state, action target, overflow order. |
| Two app scenes | Different routes; optionally a shared document | Independent navigation and intentional data consistency; failed request on the outer display handled. |
| Active inner camera | Content under the inner camera | Occlusion change moves content without hiding essential controls. |
| Camera direction changes (device) | Preview and capture in progress | Correct selection, mirroring, rotation, saved output, recovery. |
| Accessory disappears and returns (device) | Accessory enabled in its feature | Availability UI, user off-switch, content boundary, resource cleanup. |
| Large text, long translations, right-to-left | Long labels and populated screen | No double mirroring, clipping, or unreachable overflow actions. |
| VoiceOver and hardware keyboard | Main task after each transition | Focus order, labels, completion without hidden actions. |
| Older iPhone and minimum supported OS | Same core task | Working fallback without hinge, accessory, or 27.1-only APIs. |

## Release evidence

As checked 2026-09-25, Apple's [screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications) list iPhone Duo outer-display screenshots at 1398 × 2034 (2034 × 1398 landscape) and inner-display screenshots at 2007 × 2853 (2853 × 2007 landscape). The same page says App Store Connect upload support for this device arrives later this year. Recheck before producing or uploading a release set; the dimensions alone do not show that App Store Connect accepts it.

Report untested cases explicitly. Do not label a migration Duo-ready on the strength of type-checking or a static screenshot.

## Field observations

These are observations from running UI tests on a named toolchain. They are not Apple-documented behavior, may change in later builds, and have not been checked on the iPhone Duo simulator runtime or on a device. Recheck them on the runtime you test.

**Sheet detent drops after `typeText` (observed 2026-09-25).** Environment: Xcode 27.1 (27A9269), iPhone 18 Pro simulator on the iOS 27.0 runtime (24A434), hardware keyboard not connected, XCUITest. Right after [`XCUIElement.typeText(_:)`](https://developer.apple.com/documentation/xcuiautomation/xcuielement/typetext(_:)) into a `TextField` inside a sheet with [`presentationDetents([.medium, .large])`](https://developer.apple.com/documentation/swiftui/view/presentationdetents(_:)), the software keyboard was briefly hidden. The sheet dropped back to the medium detent (the grabber's accessibility value read "Half screen") and expanded again about 0.5–1 s later when the keyboard returned. An element resolved in that window was tapped at its stale medium-detent position, which by then lay under the keyboard, so the tap did nothing. A person typing on the on-screen keys did not trigger it.

What to do in tests:

- End the typed string with `"\n"` to dismiss the keyboard before the next interaction, when return simply ends editing in that field. If return submits a form or the field is multiline, wait for the layout to settle instead, for example until the sheet's detent and the next element's frame stop changing.
- Never add a retry tap. It hides real bugs, including the one it seems to fix.
- Record the runtime, simulator device, and hardware-keyboard setting next to any sheet or keyboard failure, so a toolchain quirk is not reported as an app regression.
