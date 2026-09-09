---
name: iphone-duo-camera
description: Adapt an AVFoundation camera app for iPhone Duo display transitions, choosing virtual or physical cameras and preserving direction, rotation, preview, and capture-session correctness.
---

# iPhone Duo camera

Read [camera evidence](references/camera.md). Verify relevant declarations and availability in the installed SDK before implementation. Do not infer an API from a camera's marketing feature name.

## Choose the capture strategy

Establish the product requirement: ordinary front-camera continuity, a specific physical-camera capability, or a display-relative capture experience. Compare automatic switching against the additional lifecycle work of explicit selection. Inspect available device formats rather than assuming a model guarantees the requested resolution or frame rate in the current configuration.

Document the session owner, serialization mechanism, preview owner, and actor boundaries. Keep SwiftUI/UIKit-independent capture logic out of presentation models where the project already has a reusable capture layer; do not undertake an unrelated architectural rewrite.

## Handle transitions deliberately

Serialize session reconfiguration and prevent stale direction callbacks from replacing a newer selection. Check input compatibility, retain enough state to recover when replacement fails, and present a clear interruption state if recording cannot continue. Do not promise seamless recording across a device switch without measured evidence.

Keep preview mirroring, saved-media orientation, and camera selection as separate decisions. Verify output with text and an asymmetric subject: a plausible preview does not prove the saved file is correctly oriented. When a feature uses both displays, scope display-relative state to the view that owns it.

Preserve authorization handling, interruption recovery, and resource cleanup. Avoid synchronous camera startup or expensive session work on the UI thread. Use the project's established capture actor or serial executor and satisfy actual Swift concurrency constraints rather than adding unchecked sendability.

## Verify

Test permission denial, unavailable cameras, rapid display changes, background/foreground transitions, and capture interruption. Inspect saved photos/videos, not only screenshots. Exercise reduced-capability paths and confirm the UI stays responsive.

Return the strategy tradeoff, session/state boundary, compatibility evidence, and observed failures or untested hardware cases. Simulator success cannot establish physical-camera continuity.
