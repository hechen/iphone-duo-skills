---
name: iphone-duo-layout
description: Implement or review fold-aware SwiftUI and UIKit content layouts for iPhone Duo using reserved regions and arrangements while preserving navigation and state.
---

# iPhone Duo layout

Read [layout evidence and API lookup points](references/layout.md) before choosing a Duo-specific container. Verify declarations and availability in the selected SDK. With an older SDK, improve existing layout behavior and document the deferred adoption; do not insert unresolvable symbols behind runtime availability checks.

## Choose the right boundary

Identify whether the problem belongs to navigation, the relationship between two content panes, or an individual custom control. Keep navigation responsible for routes and selection. Keep the content container responsible for pane presentation. A layout change should not restart a network task or create a second document model.

Inventory persistent state before moving view boundaries. Keep models at a stable owner, preserve item IDs, and avoid assigning identity from transient geometry. For imperative layout, recompute from the current view's bounds and insets; verify coordinate conversions when an overlay lives elsewhere in the hierarchy.

## Adapt only what needs adaptation

Start with the system container appropriate to the content. Use the linked arrangement guidance for a meaningful two-pane relationship. For a manual layout, query the available regions rather than recreating a fold from guessed angles or physical dimensions.

Make the narrow fallback explicit: when one pane is hidden, provide a way to reach it and preserve its state. Test the layout at intermediate sizes, with a keyboard, and with large text. Avoid a feedback loop where measuring a child changes its parent size indefinitely.

## Verify the user's task

Exercise a realistic transition while editing, playing media, or navigating. Check selection, focus, scroll continuity, and operation count alongside visual placement. Test existing non-Duo targets too.

Report the chosen container, state owner, fallback behavior, actual SDK/build result, and runtime evidence. Keep session-only API guidance distinct from code compiled and exercised in the user's project.
