# Toolbar evidence

## Written documentation — start here

Checked 2026-09-11:

- [Duo HIG: Vertical controls](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Vertical-controls): placement, grouping, text/symbol choices, and space pressure.
- [SwiftUI Toolbars](https://developer.apple.com/documentation/swiftui/toolbars) / [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller): toolbar composition and container ownership.
- [ToolbarOverflowMenu](https://developer.apple.com/documentation/swiftui/toolbaroverflowmenu) / [additionalOverflowItems](https://developer.apple.com/documentation/uikit/uinavigationitem/additionaloverflowitems): direct API references for overflow content.
- [ToolbarItemVisibilityPriority](https://developer.apple.com/documentation/swiftui/toolbaritemvisibilitypriority) / [UIBarButtonItemVisibilityPriority](https://developer.apple.com/documentation/uikit/uibarbuttonitemvisibilitypriority): direct references for item priority.

These pages are available; read their platform availability and beta notices. Their publication is not proof that the project's selected SDK can compile every symbol. Other new names below remain session lookup points until individually verified.

## Supplementary session

Source: [Raise the bar](https://developer.apple.com/videos/play/tech-talks/111462/), verified 2026-09-09. New declarations still require SDK validation.

- **2:00–3:09:** Bars managed by navigation containers participate; standalone UIKit bar instances do not. Navigation, toolbar, and tab controls share a region. Hardware alignment does not mirror with language direction.
- **4:29:** Session lookup points: `.cancellationAction`, `.topBarPinnedTrailing`, and UIKit `pinnedTrailingGroup`.
- **5:56–9:00:** Titles remain important in overflow even for symbol presentations. `axisBehavior` controls axis preference for custom or changing content.
- **10:07:** `toolbarVerticalEdge` / `verticalBarEdge` describe placement. Flexible and fixed spacers behave differently on the vertical axis.
- **11:40–13:10:** Review compression policy, `ToolbarOverflowMenu` / `additionalOverflowItems`, and `visibilityPriority` when controls compete for room.
- **14:21:** `toolbarVerticalBehavior` / `preferredVerticalBarBehavior` can disable vertical bars where the experience warrants it.

This index locates relevant session sections; it does not establish exact signatures or per-symbol minimum versions. The action inventory and acceptance workflow are repository recommendations.
