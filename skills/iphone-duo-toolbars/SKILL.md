---
name: iphone-duo-toolbars
description: Adapt SwiftUI and UIKit navigation bars, toolbar items, custom controls, and overflow for iPhone Duo vertical bars without losing essential actions or labels.
---

# iPhone Duo toolbars

Read [toolbar evidence](references/toolbars.md). Treat new symbols as lookup leads until their signatures and availability are checked in the actual build SDK. Preserve the current deployment target and provide supported fallbacks.

## Inventory actions by meaning

For each screen, list navigation, completion/cancellation, frequent actions, status-bearing items, and infrequent actions. Trace each to the owning navigation container. Identify custom bars and wide custom views before changing placements.

Decide which information is necessary to understand an action. A symbol can represent a familiar action, but a changing price or meaningful status may need visible text. Preserve localized labels and accessibility names in every representation. Keep the action's enabled state, shortcut, confirmation behavior, and target consistent between the bar and overflow.

## Adapt and prioritize

Use the source's system-bar behavior first, then tune only demonstrated problems. If an item changes from an icon to text while editing, verify both states before selecting an axis policy. Do not mark every item high priority: identify the action the user must retain access to under space pressure.

For a custom control, define a usable compact representation or leave it in a suitable horizontal location. Avoid shrinking text or touch targets merely to fit. If opting out of vertical bars is warranted, scope it to the affected screen and document the user-facing reason.

## Verify

Open the keyboard and overflow menu; enter selection/editing mode; present and dismiss a sheet; navigate back. Check that Save, Done, Close, or the equivalent task exit remains discoverable. Repeat with long localized titles, large text, and right-to-left content.

Return the action inventory, placement decisions, source/SDK evidence, and screenshots or interaction results for the constrained states. Report any unresolved overflow or accessibility issue explicitly.
