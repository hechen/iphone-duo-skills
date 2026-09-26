# Platform evidence

## Written documentation — start here

Checked 2026-09-25:

- [Preparing your app for iPhone Duo](https://developer.apple.com/documentation/technologyoverviews/preparing-your-app-for-iphone-duo): Apple's developer article on resizing, reserved regions, arrangement views, bars on the vertical axis, and camera handling.
- [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo): the device-specific HIG page.
- [Get ready for iPhone Duo](https://developer.apple.com/iphone-duo/): Apple's hub. It now lists Xcode 27.1 beta, the HIG page, the preparation article, and the six Tech Talks.
- [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview), [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller), and [safeAreaLayoutGuide](https://developer.apple.com/documentation/uikit/uiview/safearealayoutguide): existing adaptive containers and safe-area constraints.
- [Adapting your app when traits change](https://developer.apple.com/documentation/uikit/adapting-your-app-when-traits-change) and [Running your app on simulated or physical devices](https://developer.apple.com/documentation/xcode/running-your-app-on-simulated-or-physical-devices).

## What the linked SDK changes

The preparation article says to build with the latest Xcode to use all of the screen; apps built with Xcode 26 or earlier do not extend under the status bar and camera. The [preparation session](https://developer.apple.com/videos/play/tech-talks/111461/) (0:30–1:33) describes three tiers:

- Built with an SDK older than iOS 27, the app runs beside the status bar and camera on the outer display, and at a familiar size and aspect ratio on the inner display.
- Built with the iOS 27 SDK, the app also extends beside the status bar area on the inner display.
- Built with the iOS 27.1 SDK, the app extends to the screen edges, and standard navigation and toolbar buttons move to the vertical axis under the status bar.

Size classes, not the idiom, describe the space. The outer display behaves like a compact-width iPhone; the inner display can report regular width while the app keeps the phone idiom. Split View multitasking changes the space again. The article says not to use `userInterfaceIdiom` or `UIInterfaceOrientation` for UIKit layout decisions, and to size views relative to their container and scene rather than the screen.

## Toolchain branches

As checked 2026-09-25:

- The [Xcode 27.1 beta notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes) ship the iOS 27.1 SDK. Projects that use iOS 27.1 APIs fail to compile for Mac Catalyst; Apple's workaround is `#if !targetEnvironment(macCatalyst)`. Projects that target iOS 27.1 can lose their Catalyst run destination; the workaround is a separate Mac Catalyst 27.0 minimum deployment. Apply it only to the affected configuration.
- The [Xcode 27.2 beta notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_2-release-notes) tell developers to download Xcode 27.1 beta for the iOS SDK and simulator support for iPhone Duo. They also say the 27.2 macOS, watchOS, tvOS, and visionOS SDKs wrongly accept 27.1 as a deployment target, and that Catalyst builds with a 27.1 or 27.2 deployment target may not be able to use new API.
- Verify the branch you build with. Do not infer Duo support or platform availability from the version number alone.

## Audit leads

Search for `UIScreen.main`, cached screen bounds, orientation locks used as layout logic, `.phone` / `.pad` branches, hard-coded bar heights, doubled left/right insets, and hand-built `UIToolbar`, `UINavigationBar`, or `UITabBar` instances. Replace only the assumptions responsible for a demonstrated problem. Hand-built bars do not move to the vertical axis when the app links the new SDK; see the toolbars skill.

## Supplementary session

[Prepare your app](https://developer.apple.com/videos/play/tech-talks/111461/), reviewed 2026-09-09 and rechecked 2026-09-25:

- **1:17:** Choose the iPhone Duo simulator in Device Hub; the controls open, close, rotate, and fold the device.
- **2:46:** The inner display has regular size classes; supported interface orientations do not constrain it.
- **3:57:** Use view and scene geometry and traits. A globally selected screen is ambiguous across displays.
- **5:01–7:30:** System navigation adapts. Foreground content should respect safe areas; opposite insets can differ.
- **9:12:** Apple's App Resizability skill (renamed in Xcode 27.1) is a separate tool.

The audit prioritization and reporting workflow in this skill are repository recommendations.
