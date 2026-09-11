# Sources and verification status

Written documentation checked on **2026-09-11**. The initial edition relied too heavily on sessions; the references now start with Apple's HIG, API documentation, guides, and sample code. Documentation content was checked through Apple's pages and their DocC JSON payloads, not just an HTTP response from a JavaScript page shell.

## Source priority

Use written API references for declarations and availability, the HIG for design guidance, and guides/sample code for implementation context. Use videos for demonstrations or details whose standalone reference has not been located. A page may contain beta information; publication does not establish compatibility with the selected build SDK.

## Written documentation

| Resource | Used for |
| --- | --- |
| [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo) | Device-specific HIG: design, layout, readiness, and toolbars. |
| [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) | General HIG layout guidance. |
| [Apple Design Resources](https://developer.apple.com/design/resources/) | Official design resources and assets. |
| [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview) | SwiftUI adaptive navigation. |
| [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller) | UIKit split-view navigation. |
| [safeAreaLayoutGuide](https://developer.apple.com/documentation/uikit/uiview/safearealayoutguide) | UIKit safe-area constraints. |
| [SwiftUI Toolbars](https://developer.apple.com/documentation/swiftui/toolbars) | Toolbar composition. |
| [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) | UIKit navigation container ownership. |
| [ToolbarOverflowMenu](https://developer.apple.com/documentation/swiftui/toolbaroverflowmenu) | SwiftUI overflow content. |
| [additionalOverflowItems](https://developer.apple.com/documentation/uikit/uinavigationitem/additionaloverflowitems) | UIKit overflow content. |
| [ToolbarItemVisibilityPriority](https://developer.apple.com/documentation/swiftui/toolbaritemvisibilitypriority) | SwiftUI item priorities. |
| [UIBarButtonItemVisibilityPriority](https://developer.apple.com/documentation/uikit/uibarbuttonitemvisibilitypriority) | UIKit item priorities. |
| [WindowGroup](https://developer.apple.com/documentation/swiftui/windowgroup) | SwiftUI scenes. |
| [UIWindowScene](https://developer.apple.com/documentation/uikit/uiwindowscene) | UIKit scenes. |
| [Supporting multiple windows on iPad](https://developer.apple.com/documentation/uikit/supporting-multiple-windows-on-ipad) | Existing multiwindow architecture; not evidence of Duo-specific activation rules. |
| [AVCam: Building a camera app](https://developer.apple.com/documentation/avfoundation/avcam-building-a-camera-app) | Apple's camera sample and implementation guide. |
| [Setting up a capture session](https://developer.apple.com/documentation/avfoundation/setting-up-a-capture-session) | Capture pipeline configuration. |
| [AVCaptureDevice.RotationCoordinator](https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator) | Capture and preview rotation. |
| [Running your app on simulated or physical devices](https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices) | Build/run destinations and hardware verification. |
| [Configuring the environment of a simulated device](https://developer.apple.com/documentation/xcode/configuring-the-environment-of-a-simulated-device) | Simulator environment testing. |
| [Performing accessibility audits](https://developer.apple.com/documentation/accessibility/performing-accessibility-audits-for-your-app) | Automated inspection. |
| [Performing accessibility testing](https://developer.apple.com/documentation/accessibility/performing-accessibility-testing-for-your-app) | Accessibility settings and assistive-technology testing. |

## Remaining documentation gaps

As of 2026-09-11, the [developer hub](https://developer.apple.com/iphone-duo/) links the published HIG but lists Xcode 27.1 beta and the separate **Preparing your app for iPhone Duo** article as forthcoming.

Standalone references were not located for the announced arrangement/region types, hinge interaction, camera capture accessory, and camera direction coordinator. This is a record of this check, not proof that no reference exists under another name. The HIG provides written conceptual coverage for arrangements and reserved regions; the affected skill references retain session evidence for new API details. Recheck current documentation and SDK declarations before adopting those APIs.

## Supplementary sessions and announcement

Session pages were reviewed on **2026-09-09**. Their summaries and displayed code establish announcement evidence; they do not establish successful compilation or runtime behavior.

| Resource | Used for |
| --- | --- |
| [Get ready for iPhone Duo](https://developer.apple.com/iphone-duo/) | Toolchain/documentation release status. |
| [Apple unveils iPhone Duo](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/) | Official product identity and announcement. |
| [Design for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111466/) | Design skill. |
| [Prepare your app for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111461/) | Readiness skill. |
| [Raise the bar with iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111462/) | Toolbar skill. |
| [Strike a pose with adaptive layouts on iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111463/) | Layout skill. |
| [Leverage multiple displays and scenes on iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111464/) | Scenes and hinge interactions skill. |
| [Build a great camera experience for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111465/) | Camera skill. |

## Interpreting the content

**Written documentation:** A current Apple API reference, HIG page, guide, or sample. Read its platform and version scope; an iPad article cannot by itself establish a Duo-specific rule.

**Session evidence:** A behavior or symbol shown in a linked Apple session. Timestamps in skill references identify the relevant section.

**Repository recommendation:** Our engineering procedures, state-ownership checks, example scenarios, and reporting conventions. They are not Apple requirements.

**SDK verified:** Requires inspecting declarations in the actual selected SDK and building the affected target. No iOS 27.1 implementation in this repository currently carries this status.

**Runtime verified:** Requires executing the relevant scenario and retaining its result on the named runtime or physical device. Static review and compilation do not establish this status.

When sources change, update the affected skill, its verification date, and any tested compatibility claim together. Do not infer public API access from a consumer feature announcement.
