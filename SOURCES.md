# Sources and verification status

Written documentation checked on **2026-09-25**. The first edition leaned on Apple's Tech Talks because the written material was not out yet; Apple has since published a developer article, a HIG page, API reference for every Duo symbol these skills use, and two camera articles. The references now start from those. Documentation was checked through Apple's pages and their DocC JSON payloads, and declarations through the SDK in Xcode 27.1 (27A9269).

## Source priority

1. The selected SDK's declarations and a focused compile check establish spelling and availability.
2. Apple's API reference, developer articles, HIG, and release notes establish intended behavior and constraints.
3. Tech Talks explain design intent and show demonstrations; their examples can differ from the shipped SDK.
4. Field observations record behavior seen on a named toolchain. They are not Apple's statements.

A page may carry beta information. Publication does not establish compatibility with the SDK a project builds with.

## Written documentation

| Resource | Used for |
| --- | --- |
| [Preparing your app for iPhone Duo](https://developer.apple.com/documentation/technologyoverviews/preparing-your-app-for-iphone-duo) | Linked SDK, resizing, bars, arrangements, reserved regions, camera handling. |
| [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo) | Anatomy, poses, dynamic layouts, arrangements, vertical controls, games. |
| [Get ready for iPhone Duo](https://developer.apple.com/iphone-duo/) | Tooling and resource status. |
| [ReservedRegion](https://developer.apple.com/documentation/swiftui/reservedregion) / [UIView.ReservedRegion](https://developer.apple.com/documentation/uikit/uiview/reservedregion) | Divisions, occlusions, active state, margins, right-to-left geometry. |
| [ArrangementView](https://developer.apple.com/documentation/swiftui/arrangementview) / [UIArrangementViewController](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller) | Split and overlay arrangements. |
| [ToolbarItemAxisBehavior](https://developer.apple.com/documentation/swiftui/toolbaritemaxisbehavior), [toolbarVerticalEdge](https://developer.apple.com/documentation/swiftui/environmentvalues/toolbarverticaledge), [toolbarVerticalBehavior(_:)](https://developer.apple.com/documentation/swiftui/view/toolbarverticalbehavior(_:)), [ToolbarVerticalCompressionBehavior](https://developer.apple.com/documentation/swiftui/toolbarverticalcompressionbehavior) and their UIKit counterparts | Bars on the vertical axis. |
| [ToolbarOverflowMenu](https://developer.apple.com/documentation/swiftui/toolbaroverflowmenu), [additionalOverflowItems](https://developer.apple.com/documentation/uikit/uinavigationitem/additionaloverflowitems), [ToolbarItemVisibilityPriority](https://developer.apple.com/documentation/swiftui/toolbaritemvisibilitypriority), [UIBarButtonItemVisibilityPriority](https://developer.apple.com/documentation/uikit/uibarbuttonitemvisibilitypriority) | Overflow and priority. |
| [onHingeChange(isEnabled:_:)](https://developer.apple.com/documentation/swiftui/view/onhingechange(isenabled:_:)) / [UIHingeInteraction](https://developer.apple.com/documentation/uikit/uihingeinteraction) | Hinge state. |
| [Registering a camera capture accessory on iPhone Duo](https://developer.apple.com/documentation/avfoundation/registering-a-camera-capture-accessory-on-iphone-duo), [CameraCaptureAccessory](https://developer.apple.com/documentation/swiftui/cameracaptureaccessory), [UISceneAccessory](https://developer.apple.com/documentation/uikit/uisceneaccessory) | Outer-display content during capture. |
| [UIWindowScene.ActivationAction](https://developer.apple.com/documentation/uikit/uiwindowscene/activationaction), [WindowGroup](https://developer.apple.com/documentation/swiftui/windowgroup), [UIWindowScene](https://developer.apple.com/documentation/uikit/uiwindowscene), [Supporting multiple windows on iPad](https://developer.apple.com/documentation/uikit/supporting-multiple-windows-on-ipad) | Multiple scenes. The iPad article is not evidence of Duo-specific activation rules. |
| [Choosing a camera by the direction it faces](https://developer.apple.com/documentation/avkit/choosing-a-camera-by-the-direction-it-faces) and [AVCaptureDeviceDirectionCoordinator](https://developer.apple.com/documentation/avkit/avcapturedevicedirectioncoordinator) | Virtual front camera, direction, mirroring, rotation. |
| [AVCam](https://developer.apple.com/documentation/avfoundation/avcam-building-a-camera-app), [Setting up a capture session](https://developer.apple.com/documentation/avfoundation/setting-up-a-capture-session), [AVCaptureDevice.RotationCoordinator](https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator) | Capture pipeline and rotation. |
| [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview), [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller), [safeAreaLayoutGuide](https://developer.apple.com/documentation/uikit/uiview/safearealayoutguide), [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) | Adaptive navigation and safe areas. |
| [Xcode 27.1 beta notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes) and [Xcode 27.2 beta notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes) | Toolchain branch, Catalyst workarounds, simulator limits. |
| [Device Hub](https://developer.apple.com/documentation/xcode/device-hub), [Running your app on simulated or physical devices](https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices), [Configuring the environment of a simulated device](https://developer.apple.com/documentation/xcode/configuring-the-environment-of-a-simulated-device) | Simulated poses and device runs. |
| [Performing accessibility audits](https://developer.apple.com/documentation/accessibility/performing-accessibility-audits-for-your-app) and [testing](https://developer.apple.com/documentation/accessibility/performing-accessibility-testing-for-your-app) | Automated and manual accessibility checks. |
| [Screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications) | Duo screenshot sizes and upload status. |

## Where sources disagree

Keep these visible instead of silently picking one:

- **Inactive reserved regions.** The `ReservedRegion` overview says the query returns intersecting regions whether or not they are active; the layout Tech Talk says only active regions are returned by default. The skills filter on `isActive` explicitly.
- **Arrangements and navigation split views.** The HIG says to put navigation containers around an arrangement; the preparation article says to avoid putting an arrangement inside a navigation split view, list, or scroll view. The skills keep navigation out of arrangements, keep arrangements out of lists and scroll views, and ask for a reachability check when a split view column holds one.
- **Vertical bar edge.** The HIG says the vertical bar stays on the same hardware side in right-to-left languages; the `toolbarVerticalEdge` page says the edge depends on locale and device. The skills read the value instead of assuming either.
- **Accessory conditions.** The written article requires the app in the foreground, a running capture session, and the capture interface on the inner display. The scenes Tech Talk also says the app is full screen. The skills follow the article and mention the session detail.

## SDK verification

[`tests/iPhoneDuoProbe.swift`](tests/iPhoneDuoProbe.swift) covers arrangements, reserved-region queries, hinge callbacks, toolbar axis, edge, compression, and opt-out APIs, camera-capture accessory registration in SwiftUI and UIKit, the window activation action, and the camera direction coordinator. [`scripts/check-sdk.sh`](scripts/check-sdk.sh) type-checks it for `arm64-apple-ios27.1` and `arm64-apple-ios27.1-simulator`.

On 2026-09-25, Xcode 27.1 (27A9269) with the iOS 27.1 SDK (24A94403) passed both targets. Xcode 27.0 (27A266a) with the iOS 27.0 SDK failed, as expected, because it lacks the Duo declarations. The probe establishes spelling and availability only. The skills' API map marks which symbols it covers.

## Supplementary sessions

Session pages were first reviewed on 2026-09-09 and rechecked against their transcripts on 2026-09-25. They establish Apple's explanations and demonstrations; they do not establish compilation or runtime behavior.

| Resource | Used for |
| --- | --- |
| [Apple unveils iPhone Duo](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/) | Product identity and announcement. |
| [Design for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111466/) | Design skill. |
| [Prepare your app for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111461/) | Readiness skill, linked-SDK tiers, Device Hub. |
| [Raise the bar with iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111462/) | Toolbars skill. |
| [Strike a pose with adaptive layouts on iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111463/) | Layout skill. |
| [Leverage multiple displays and scenes on iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111464/) | Scenes skill, including the outer-display window limit. |
| [Build a great camera experience for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111465/) | Camera skill. |

## Interpreting the content

**Written documentation:** a current Apple API reference, article, HIG page, guide, sample, or release note. Read its platform and version scope; an iPad article cannot by itself establish a Duo rule.

**Session evidence:** a behavior or symbol shown in a linked Apple Tech Talk. Timestamps identify the section.

**Repository recommendation:** our engineering procedures, state-ownership checks, example scenarios, and reporting conventions. They are not Apple requirements.

**Field observation:** behavior a maintainer saw while testing on a named Xcode build and runtime. It is labeled with its date and environment, kept out of the main instructions, and must be rechecked on the runtime you use.

**SDK verified:** the declaration was checked in the selected SDK and compiled by the probe. It says nothing about runtime behavior.

**Runtime verified:** the scenario ran on the named runtime or physical device and its result was kept. Static review and compilation do not establish this. No scenario in this repository currently carries this status.

When sources change, update the affected skill, its check date, and any tested compatibility claim together. Do not infer public API access from a consumer feature announcement.
