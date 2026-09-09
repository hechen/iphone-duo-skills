---
name: iphone-duo-scenes
description: Implement or review iPhone Duo multiple scenes, hinge-driven interactions, and display accessories with explicit state ownership and capability-change handling.
---

# iPhone Duo scenes and interactions

Read [scenes evidence](references/scenes.md). Choose the relevant mode; an app needing resizing does not automatically need hinge effects or a second-display experience. Verify new APIs in the selected SDK before writing compilable integration code.

## Multiple scenes

Map app-shared data, document state, and scene-local presentation separately. A route or selected tab in one window should not unintentionally navigate another. Conversely, two windows editing the same document need a deliberate consistency model.

Follow existing storage and synchronization boundaries. Give new-scene requests a meaningful document or route identity and handle request failure without discarding the user's current work. Restore scene presentation without duplicating an in-progress operation.

## Hinge interaction

Use hinge input only for an interaction that benefits from it. Define a neutral state when input is unavailable and a touch or other accessible way to perform the essential task. Keep continuous input out of persistence and expensive work unless that work is actually needed; bound updates and cancel obsolete effects.

Use the layout mechanisms described in the source for geometry decisions rather than a custom hinge-angle breakpoint system.

## Display accessory

Separate user intent to enable an accessory from current system availability. Update UI when either changes. Keep accessory ownership attached to the relevant feature's lifecycle and release resources when that feature exits.

Define precisely what content appears on the outward-facing display. Use a purpose-specific presentation model so private editor controls or unrelated document data are not accidentally mirrored. This is a product data-boundary decision, not a reason to add a generic permission flow.

## Verify

Exercise two scenes independently, failed scene activation, accessory availability loss/recovery, and absent hinge input where relevant. Record continuity and cleanup results, plus the exact SDK/runtime tested. Do not infer arbitrary access to both displays from their physical existence.
