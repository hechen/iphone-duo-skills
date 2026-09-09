# Layout evidence and API lookup points

Source: [Strike a pose](https://developer.apple.com/videos/play/tech-talks/111463/), verified 2026-09-09. Names below are session references, not a compiled API recipe.

- **2:26–5:12:** Displace related controls together when needed; continuously scrolling content should not be moved as a unit around the fold.
- **6:39–8:39:** Query `reservedRegions` in local view geometry. `.division` describes partitioning; `.occlusion` describes covered space. Queries return active regions by default; `.includeInactive` also exposes inactive ones.
- **9:20–13:21:** `ArrangementView` and `UIArrangementViewController` arrange primary and secondary content. Split arrangements partition space; axis restrictions can leave only one pane visible. Overlay arrangements suit overlapping content.
- **13:21–14:39:** `overlayArrangementZIndex` and UIKit arrangement state help adapt an overlapping pane's presentation.
- **16:09:** Put arrangements below navigation and above scrollable content. They do not supply navigation infrastructure; do not wrap a navigation container in an arrangement or place an arrangement inside a scrolling container.

Confirm exact signatures, availability, and behavior in the installed SDK before implementation. State ownership and transition checks in the main skill are repository recommendations.
