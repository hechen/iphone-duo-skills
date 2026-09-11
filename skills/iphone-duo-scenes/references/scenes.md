# Scenes evidence

## Written documentation — start here

Checked 2026-09-11:

- [WindowGroup](https://developer.apple.com/documentation/swiftui/windowgroup): SwiftUI scene structure.
- [UIWindowScene](https://developer.apple.com/documentation/uikit/uiwindowscene): UIKit's scene/window boundary.
- [Supporting multiple windows on iPad](https://developer.apple.com/documentation/uikit/supporting-multiple-windows-on-ipad): established multiwindow architecture. This article's iPad scope does not independently prove Duo's activation rules.

Standalone documentation for `UIHingeInteraction` and `CameraCaptureAccessory` was not located during this check. The session below remains the reference for their announced behavior, including Duo-specific activation and accessory constraints. Recheck the developer hub and actual SDK before implementation.

## Supplementary session

Source: [Multiple displays and scenes](https://developer.apple.com/videos/play/tech-talks/111464/), verified 2026-09-09. New names are session evidence pending SDK validation.

- **0:49–2:35:** `onHingeChange` and `UIHingeInteraction` expose status and angle. Handle an absent hinge and reset an effect outside its active state. Use arrangement/region APIs for layout instead.
- **2:59–3:38:** Duo supports multitasking and multiple app scenes. New-window creation is unavailable on the outer display; handle activation failure. The session discusses `UIWindowSceneActivation` for capability-aware actions.
- **4:22:** Scene accessory availability can change while an app runs.
- **5:00–6:25:** `CameraCaptureAccessory` supports supplementary outer-display content while a camera app is full-screen on the inner display with an active session. Register it with the camera view using `sceneAccessory`; observe availability through `onAvailabilityChange`.

These capabilities do not establish unrestricted independent rendering on every display. Verify current declarations and constraints before implementation. The state-boundary and cleanup procedures in this skill are repository recommendations.
