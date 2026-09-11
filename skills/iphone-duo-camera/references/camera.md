# Camera evidence

## Written documentation — start here

Checked 2026-09-11:

- [AVCam: Building a camera app](https://developer.apple.com/documentation/avfoundation/avcam-building-a-camera-app): Apple's sample and explanation of a capture app's components.
- [Setting up a capture session](https://developer.apple.com/documentation/avfoundation/setting-up-a-capture-session): inputs, outputs, and the session pipeline.
- [AVCaptureDevice.RotationCoordinator](https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator): the Swift API for capture and preview rotation angles. Its Objective-C name is `AVCaptureDeviceRotationCoordinator`; prefer the declaration for the language being implemented.

These established capture APIs are documented. A standalone reference for the newly announced direction coordinator was not located during this check. Its Duo-specific behavior below remains session evidence until current documentation/SDK declarations can be verified.

## Supplementary session

Source: [Build a great camera experience](https://developer.apple.com/videos/play/tech-talks/111465/), verified 2026-09-09. Symbols are session references; exact declarations and availability are uncompiled here.

- **0:58–1:53:** The virtual front camera switches between physical cameras and exposes their common capabilities. Explicit devices provide camera-specific features but require more management.
- **2:46–4:50:** A camera's `.front` position does not establish direction relative to a view on a changing display. AVKit's `AVCaptureDeviceDirectionCoordinator` reports view-relative direction; separate display views need separate coordinators.
- **5:38:** The coordinator is main-actor-bound. Transfer its sendable `AVCaptureDeviceDescriptor` to the capture owner rather than performing session work in its UI callback.
- **6:17–7:51:** Review mirroring after selection changes. Preview framing uses `videoGravity`; the session also introduces `dynamicAspectRatio`.
- **8:03:** Adopt `AVCaptureDeviceRotationCoordinator` for transitions. The session discusses disabling `isCameraSensorOrientationCompensationEnabled` after adopting rotation coordination; verify this combination before changing it.

The transaction, stale-update, and saved-media checks in the main skill are repository recommendations.
