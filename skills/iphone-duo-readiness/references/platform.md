# Platform evidence

Verified against Apple session pages on 2026-09-09; new SDK declarations remain uncompiled here.

[Prepare your app](https://developer.apple.com/videos/play/tech-talks/111461/) describes these considerations:

- **0:30–1:33:** Linking SDK affects available screen space and system-bar adaptation. The session demonstrates Xcode 27.1 and DeviceHub pose controls.
- **2:46:** The inner display has regular size classes; supported interface orientations do not constrain it. Select layouts from the current environment.
- **3:57:** Use view/scene geometry and traits. A globally selected screen is ambiguous across displays.
- **5:01–7:30:** System navigation adapts. Foreground content should respect safe areas; opposite insets can differ.
- **9:12:** Apple's App Resizability skill is a separate tool.

The [developer hub](https://developer.apple.com/iphone-duo/) still lists Xcode 27.1 beta and the preparation article as coming later this month on the verification date. The session demonstration does not prove that toolchain is available locally. Refresh this status before adopting new APIs.

The audit prioritization and reporting workflow in this skill are repository recommendations.
