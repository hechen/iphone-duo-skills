# Layout evidence

## Written documentation — start here

Checked 2026-09-25 against Apple's pages and the iOS 27.1 SDK in Xcode 27.1 (27A9269):

- [Preparing your app for iPhone Duo](https://developer.apple.com/documentation/technologyoverviews/preparing-your-app-for-iphone-duo): resizing checklist, arrangement views, and reserved regions.
- [Duo HIG: Dynamic layouts](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Dynamic-layouts): reserved regions, split views, and arrangement views.
- [ReservedRegion](https://developer.apple.com/documentation/swiftui/reservedregion), [GeometryProxy.reservedRegions(kind:options:layoutDirectionBehavior:)](https://developer.apple.com/documentation/swiftui/geometryproxy/reservedregions(kind:options:layoutdirectionbehavior:)), [UIView.ReservedRegion](https://developer.apple.com/documentation/uikit/uiview/reservedregion), and [UIView.reservedRegions(kind:options:)](https://developer.apple.com/documentation/uikit/uiview/reservedregions(kind:options:)).
- [ArrangementView](https://developer.apple.com/documentation/swiftui/arrangementview), [arrangementViewStyle(_:)](https://developer.apple.com/documentation/swiftui/view/arrangementviewstyle(_:)), [overlayArrangementZIndex](https://developer.apple.com/documentation/swiftui/environmentvalues/overlayarrangementzindex), and [UIArrangementViewController](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller).
- [NavigationSplitView](https://developer.apple.com/documentation/swiftui/navigationsplitview), [UISplitViewController](https://developer.apple.com/documentation/uikit/uisplitviewcontroller), and [safeAreaLayoutGuide](https://developer.apple.com/documentation/uikit/uiview/safearealayoutguide).

All of these APIs are iOS 27.1 unless the page says otherwise. They are in this repository's SDK probe.

## Container and safe-area audit

Search for `UIScreen.main`, cached screen bounds, orientation locks used as layout logic, `.phone` / `.pad` branches, hard-coded bar heights, and doubled left/right insets. Replace only the assumptions responsible for a demonstrated problem.

The outer display uses a compact width; the inner display can provide a regular width while the app keeps the phone idiom. Split View multitasking changes the space again. Use current traits together with actual container geometry. Safe-area edges are independent: a vertical bar adds an inset on one side only, and in Split View each app keeps its bars along its own outer edge. Keep decorative backgrounds and interactive content on separate safe-area policies.

## Reserved regions

A **division** is where the fold splits a large view into smaller ones. An **occlusion** is where hardware covers content. On iPhone Duo the outer front camera always occludes the outer display, the inner front camera occludes only while it is active, and the fold is active when the device is partially open and inactive when it is fully open. System alerts, context menus, and sheets move around the fold, and standard split views adjust their column widths on their own.

Query regions from the view that needs them and keep the results in that view's coordinate space:

- Filter on `isActive` for current avoidance. The written `ReservedRegion` overview says the query returns every region that intersects the view, active or not, while the [layout session](https://developer.apple.com/videos/play/tech-talks/111463/) (7:22–7:50) says only active regions are returned by default. Filtering explicitly works under either reading. Do not let an inactive fold reserve permanent blank space.
- Use `.includeInactive` for planning. The session suggests preferring an even number of grid columns when a division exists, whatever its state; the HIG says the same for grids.
- `frame` already includes `margins`. Do not add the margins again.
- SwiftUI mirrors region geometry for right-to-left layout by default (`layoutDirectionBehavior: .mirrors`). Pass `.fixed` only when you deliberately work in fixed coordinates. The UIKit query has no layout-direction parameter; check right-to-left behavior on the runtime you test.

Prefer relocating a control or resizing a panel over forcing every pixel away from the fold. The HIG asks for small adjustments instead of dramatic rearrangement, because controls that jump are hard to find again.

## Arrangement containers

An arrangement holds a primary and a secondary view.

- **Split** places them side by side when the arrangement is wider than tall, and stacked when it is taller than wide, adjusting for reserved regions such as the fold. `ArrangementView`'s default automatic style resolves to split.
- **Overlay** layers the primary view over the secondary view when no division is active (closed or fully open). When the device is partially open, the primary view moves to the trailing or bottom part and the secondary view to the leading or top part.
- Both styles accept `axes(_:)`. Constrain axes only when hiding or moving the secondary content is intentional, and keep a path to whatever the constrained layout hides.
- In an overlay arrangement, read `overlayArrangementZIndex` (SwiftUI) or `state(for:)` on `UIArrangementViewController` (UIKit, which also reports `isHidden` and `splitAxis`) to switch a pane between collapsed and expanded presentations.

Where the arrangement sits matters. The HIG says to keep navigation outside arrangement views, with navigation split views and tab views around the arrangement rather than inside it. The preparation article says to avoid placing an arrangement inside a navigation split view, list, scroll view, or other container that can make part of it inaccessible. Together they rule out navigation containers inside an arrangement (HIG) and an arrangement inside a list or scroll view (article). They read differently for a navigation split view parent, so when you put an arrangement in a split view column, verify that every part stays reachable in each pose. Inspect the full hierarchy before adding one; do not blanket-wrap existing containers.

## Supplementary session

[Strike a pose](https://developer.apple.com/videos/play/tech-talks/111463/), reviewed 2026-09-09 and rechecked 2026-09-25:

- **2:26–5:12:** Displace related controls together when needed; continuously scrolling content should not be moved as a unit around the fold. A folded device can put glanceable content in the top region and touch controls in the bottom region.
- **6:39–8:39:** Query reserved regions in local view geometry. The fold's division has zero width when the device is flat.
- **9:20–13:21:** Split arrangements partition space; axis restrictions can leave only one pane visible. Overlay arrangements suit overlapping content.
- **13:21–14:39:** `overlayArrangementZIndex` and UIKit arrangement state adapt an overlapping pane's presentation.
- **16:09:** Put arrangements below navigation and above scrollable content.

State ownership and transition checks in the main skill are repository recommendations.
