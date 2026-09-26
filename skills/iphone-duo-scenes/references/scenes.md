# Scenes evidence

## Written documentation — start here

Checked 2026-09-25 against Apple's pages and the iOS 27.1 SDK in Xcode 27.1 (27A9269):

- [WindowGroup](https://developer.apple.com/documentation/swiftui/windowgroup), [UIWindowScene](https://developer.apple.com/documentation/uikit/uiwindowscene), and [Supporting multiple windows on iPad](https://developer.apple.com/documentation/uikit/supporting-multiple-windows-on-ipad). The iPad article describes the established architecture; it does not establish Duo's activation rules by itself.
- [UIWindowScene.ActivationAction](https://developer.apple.com/documentation/uikit/uiwindowscene/activationaction) (`UIWindowSceneActivationAction` in Objective-C).
- Hinge: [onHingeChange(isEnabled:_:)](https://developer.apple.com/documentation/swiftui/view/onhingechange(isenabled:_:)), [DeviceHingeContext](https://developer.apple.com/documentation/swiftui/devicehingecontext), [DeviceHinge](https://developer.apple.com/documentation/swiftui/devicehinge), and [UIHingeInteraction](https://developer.apple.com/documentation/uikit/uihingeinteraction).
- Accessories: [Registering a camera capture accessory on iPhone Duo](https://developer.apple.com/documentation/avfoundation/registering-a-camera-capture-accessory-on-iphone-duo), [sceneAccessory(content:)](https://developer.apple.com/documentation/swiftui/view/sceneaccessory(content:)), [CameraCaptureAccessory](https://developer.apple.com/documentation/swiftui/cameracaptureaccessory), [ExternalNonInteractiveAccessory](https://developer.apple.com/documentation/swiftui/externalnoninteractiveaccessory), [UISceneAccessory](https://developer.apple.com/documentation/uikit/uisceneaccessory), and [UISceneAccessoryRegistration](https://developer.apple.com/documentation/uikit/uisceneaccessoryregistration).

## Multiple scenes

The HIG describes Split View multitasking on the inner display. The [multiple displays and scenes session](https://developer.apple.com/videos/play/tech-talks/111464/) (2:59–3:38) says apps that support multiple windows on iPad support them on iPhone Duo too, that new windows cannot be created on the outer display, only on the inner one, and recommends handling errors from scene requests and using `UIWindowScene.ActivationAction`, which hides itself when new windows are unavailable. The written documentation checked here does not restate the outer-display rule, so treat it as session evidence and test it.

A second window needs its own scene presentation state backed by the shared domain model. An open inner display is still the phone idiom.

## Hinge

- SwiftUI: `onHingeChange(isEnabled:_:)` calls its action with the old and new `DeviceHingeContext`. The context's `hinge` is optional. `DeviceHinge` has an `angle` (an `Angle`) and a `status` of `closed`, `partiallyOpen`, or `fullyOpen`.
- UIKit: add a `UIHingeInteraction` to a view. Its handler runs with the initial state, on every change, and when the interaction moves between hierarchies. The update's `hinge` is `nil` when the interaction leaves a hierarchy that provides hinge updates. `UIHinge.angle` is in radians. While the interaction is disabled, updates are dropped, not queued; re-enabling delivers the current state.
- The UIKit header says the rate and granularity of angle updates are system policy and can change, and to prefer `status` when you only need closed, partially open, or fully open.
- An angle is not the available layout region. Use reserved regions for layout.

## Camera capture accessory

The written article describes the behavior:

- The system presents the content on the outer display while the app is in the foreground with an active capture session and its capture interface is on the inner display, which means the device is open. The session (5:00–6:25) adds that the app is full screen on the inner display.
- SwiftUI: apply `sceneAccessory` to the view that shows the capture interface and declare a `CameraCaptureAccessory` inside it. UIKit: create `UISceneAccessory.cameraCapture(sceneConfiguration:userInfo:)`, pass it to `registerSceneAccessory(_:)` on the capture view controller, and keep a strong reference to the returned registration. The system presents content only while that interface is on screen.
- Accessory scenes have no project-level configuration, so a scene-manifest entry has no effect. The system assigns the session role; compare against `UISceneSession.Role.windowCameraCaptureAccessory` if one delegate handles several kinds of scene. In UIKit, read the shared object back from `connectionOptions.sceneAccessoryUserInfo` and keep your own strong reference to it.
- Availability is set by the system: `onAvailabilityChange(perform:)` in SwiftUI, `isAvailable` on the registration in UIKit (observable, so reading it in `updateProperties()` keeps controls current). Content goes away when capture stops, the app leaves the foreground, or the device folds closed. The top-most registration of a kind wins, so navigating to another registering view makes the previous one unavailable until the person goes back.
- Let people turn the content off with `CameraCaptureAccessory(isEnabled:content:)` or the registration's `isEnabled`, rather than by unregistering. Content is on by default. Call `unregisterSceneAccessory(_:)` when the feature stops offering the content.
- Keep essential controls in the capture interface. The outer display accepts touch, which suits a single capture task such as tap to focus, not a second interface. Keep persistent state in the model, not in the accessory's views.
- Accessories of different kinds do not compete. `ExternalNonInteractiveAccessory` (iOS 27.0) presents non-interactive content on a connected or AirPlay display and is a different role from `CameraCaptureAccessory`.
- Check accessory layout in previews or Simulator. Simulator has no camera, so test presentation on a device.

Camera direction, mirroring, and rotation are covered by the camera skill.

## Supplementary session

[Multiple displays and scenes](https://developer.apple.com/videos/play/tech-talks/111464/), reviewed 2026-09-09 and rechecked 2026-09-25:

- **0:49–2:35:** Drive an interactive effect from the hinge angle; reset it outside its active state; use arrangements and regions for layout instead.
- **2:59–3:38:** Multiple scenes and the outer-display window limit described above.
- **4:22:** Scene accessory availability can change while an app runs.
- **5:34:** A teleprompter walkthrough using `sceneAccessory` on the camera view.

The state-boundary and cleanup procedures in this skill are repository recommendations.
