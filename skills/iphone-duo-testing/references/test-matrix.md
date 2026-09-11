# Transition matrix

## Written documentation — start here

Checked 2026-09-11:

- [Running your app on simulated or physical devices](https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices): schemes, destinations, and physical-device verification.
- [Configuring the environment of a simulated device](https://developer.apple.com/documentation/xcode/configuring-the-environment-of-a-simulated-device): appearance, accessibility, and simulator environment controls. Match these instructions to the installed Xcode version.
- [Performing accessibility audits](https://developer.apple.com/documentation/accessibility/performing-accessibility-audits-for-your-app) and [Performing accessibility testing](https://developer.apple.com/documentation/accessibility/performing-accessibility-testing-for-your-app): automated inspection plus testing with accessibility settings and assistive technologies.

## Repository test scenarios

This matrix is a repository-authored QA proposal. Select rows relevant to the app; do not require camera or multi-scene work for unrelated apps.

| Scenario | State to establish | Verify after transition |
| --- | --- | --- |
| Available space shrinks and expands | A selected detail and scrolled collection | Selection, return path, scroll identity. |
| Display open/close transition | Unsaved form with keyboard visible | Draft, focus, completion/cancel controls. |
| Partial fold and return to flat | Interactive control near the center | Visibility, hit testing, stable state. |
| Rotation and constrained multitasking | Primary task in progress | Content fits; essential actions remain reachable. |
| Sheet/popover while space changes | Anchored presentation with entered data | Presentation, anchor, dismissal, retained data. |
| Toolbar overflow under pressure | Editing mode with frequent actions | Correct labels, enabled state, action target. |
| Two app scenes | Different routes; optionally a shared document | Independent navigation and intentional data consistency. |
| Accessory disappears and returns | Accessory enabled in its feature | Availability UI, content boundary, resource cleanup. |
| Camera direction changes | Preview and capture in progress | Correct selection, mirroring, saved output, recovery. |
| Large text and right-to-left content | Long labels and populated screen | Reading order, clipping, navigation, usable controls. |
| Assistive technologies | Main task with VoiceOver; relevant motion settings | Focus order, labels, completion without hidden actions. |
| Existing supported device regression | Same core task | No loss of established behavior. |

## Source boundary

[Apple's accessibility audit guide](https://developer.apple.com/documentation/accessibility/performing-accessibility-audits-for-your-app), checked 2026-09-09, describes Inspector audits and `XCUIApplication.performAccessibilityAudit`. It also explains that a successful audit does not establish complete accessibility. Inspect each relevant screen and exercise assistive technologies.

For current Duo tooling, consult the [developer hub](https://developer.apple.com/iphone-duo/). On this matrix's verification date, Xcode 27.1 beta is listed as forthcoming. Record actual installed tooling independently.
