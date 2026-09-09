# Toolbar evidence

Source: [Raise the bar](https://developer.apple.com/videos/play/tech-talks/111462/), verified 2026-09-09. New declarations still require SDK validation.

- **2:00–3:09:** Bars managed by navigation containers participate; standalone UIKit bar instances do not. Navigation, toolbar, and tab controls share a region. Hardware alignment does not mirror with language direction.
- **4:29:** Session lookup points: `.cancellationAction`, `.topBarPinnedTrailing`, and UIKit `pinnedTrailingGroup`.
- **5:56–9:00:** Titles remain important in overflow even for symbol presentations. `axisBehavior` controls axis preference for custom or changing content.
- **10:07:** `toolbarVerticalEdge` / `verticalBarEdge` describe placement. Flexible and fixed spacers behave differently on the vertical axis.
- **11:40–13:10:** Review compression policy, `ToolbarOverflowMenu` / `additionalOverflowItems`, and `visibilityPriority` when controls compete for room.
- **14:21:** `toolbarVerticalBehavior` / `preferredVerticalBarBehavior` can disable vertical bars where the experience warrants it.

This index locates relevant session sections; it does not establish exact signatures or per-symbol minimum versions. The action inventory and acceptance workflow are repository recommendations.
