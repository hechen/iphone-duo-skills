# Camera evidence

## Written documentation — start here

Checked 2026-09-25 against Apple's pages and the iOS 27.1 SDK in Xcode 27.1 (27A9269):

- [Choosing a camera by the direction it faces](https://developer.apple.com/documentation/avkit/choosing-a-camera-by-the-direction-it-faces): Apple's guide to the virtual front camera, the direction coordinator, mirroring, and rotation on iPhone Duo.
- [AVCaptureDeviceDirectionCoordinator](https://developer.apple.com/documentation/avkit/avcapturedevicedirectioncoordinator) (AVKit, iOS 27.1), with `AVCaptureDeviceDirectionMap` and `AVCaptureDeviceDescriptor`.
- [builtInOuterUltraWideCamera](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtinouterultrawidecamera) and [builtInInnerUltraWideCamera](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtininnerultrawidecamera) (iOS 27.1).
- [AVCaptureDevice.RotationCoordinator](https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator) and [Supporting device rotation in your camera app](https://developer.apple.com/documentation/avfoundation/supporting-device-rotation-in-your-camera-app). The Objective-C name is `AVCaptureDeviceRotationCoordinator`.
- [AVCam: Building a camera app](https://developer.apple.com/documentation/avfoundation/avcam-building-a-camera-app) and [Setting up a capture session](https://developer.apple.com/documentation/avfoundation/setting-up-a-capture-session).

## Virtual front camera

A discovery session for the front position with `builtInWideAngleCamera` or `builtInUltraWideCamera` returns the virtual front camera on iPhone Duo. It streams from the camera above the display the app is on and switches as the device opens and closes, so an app that captures from the front camera keeps working. `isVirtualDevice` is `true`; read [`activePrimaryConstituent`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/activeprimaryconstituent) to see which physical camera is streaming (it is `nil` until the session runs). Its capabilities are the ones both front cameras share, and the system decides which one streams.

## Physical cameras and direction

When capture is the app's main job, use `builtInOuterUltraWideCamera` and `builtInInnerUltraWideCamera` for each camera's full capabilities. Following their direction is then the app's work.

`position` still reports where a camera sits, not which way it points. The direction coordinator takes the preview view as its frame of reference and sorts the listed cameras into forward-facing (same way as the view) and backward-facing. A rear camera can be forward-facing after the device opens or closes, which is how a person takes a selfie with it.

- List every built-in camera you capture from, including rear cameras. The coordinator ignores the virtual front camera, external cameras, Continuity Camera, and Desk View; list the two physical front cameras in place of the virtual one.
- Create the coordinator and handle its updates on the main actor. Hold a strong reference while the view is on screen. Use one coordinator per preview view; the same rear camera can be forward-facing for one view and backward-facing for another.
- The handler runs soon after creation with the current directions and again on every change. `deviceDirections` is an empty map until that first call.
- Compare the active camera against the forward-facing array; when it is gone, pick a replacement.
- Descriptors and maps are `Sendable`. Do not call AVFoundation from the handler. Pass the descriptor to the actor that owns the session, resolve it with `AVCaptureDevice(uniqueID:)`, and handle a `nil` result because the set of cameras can change while you dispatch. A descriptor identifies a camera; it does not reserve it.
- Reconfigure a single video input rather than connecting both cameras in a multicamera session.
- On a single-display iPhone the same code works: front cameras arrive forward-facing, back cameras backward-facing, and the handler runs once.

## Preview, mirroring, and rotation

- Mask the preview when the handler fires and restore it once the new device delivers frames.
- A connection mirrors any camera whose position is front. Decide mirroring from the direction map instead: mirror a rear camera that faces forward, and show a front camera that faces backward unmirrored. Check `isVideoMirroringSupported`, set [`automaticallyAdjustsVideoMirroring`](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/automaticallyadjustsvideomirroring) to `false` before assigning `isVideoMirrored` (assigning it first raises an exception), and reapply after every input change, because a new input creates a new preview connection.
- A rotation coordinator reports angles for the device it was created with, and on iPhone Duo the angle also changes as the app moves between displays. Create a new one each time you switch cameras.

## Supplementary session

[Build a great camera experience](https://developer.apple.com/videos/play/tech-talks/111465/), reviewed 2026-09-09 and rechecked 2026-09-25:

- **0:58–1:53:** The virtual front camera switches between physical cameras and exposes their common capabilities.
- **2:46–5:38:** Direction relative to a view, one coordinator per display view, and main-actor handling.
- **6:17–7:51:** Review mirroring after selection changes. Frame the preview with `videoGravity`; when streaming from the ultra-wide front cameras, [`dynamicAspectRatio`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/dynamicaspectratio) (iOS 26) can select a landscape aspect ratio to fill the inner display.
- **8:03–8:34:** Adopt rotation coordination. The session shows turning off [`isCameraSensorOrientationCompensationEnabled`](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/iscamerasensororientationcompensationenabled) (iOS 26) for performance; the SDK header says to turn it off only if the app does not need that compensation. Verify saved orientation before and after changing it.

The transaction, stale-update, and saved-media checks in the main skill are repository recommendations.
