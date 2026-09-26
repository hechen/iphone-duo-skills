# Toolbar evidence

## Written documentation — start here

Checked 2026-09-25 against Apple's pages and the iOS 27.1 SDK in Xcode 27.1 (27A9269):

- [Preparing your app for iPhone Duo: Optimize bars for vertical presentation](https://developer.apple.com/documentation/technologyoverviews/preparing-your-app-for-iphone-duo#Optimize-bars-for-vertical-presentation) and its "Organize items in your bars" section.
- [Duo HIG: Vertical controls](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo#Vertical-controls): placement order, priorities, compression, overflow, and representations.
- Axis: [axisBehavior(_:)](https://developer.apple.com/documentation/swiftui/toolbarcontent/axisbehavior(_:)) / [ToolbarItemAxisBehavior](https://developer.apple.com/documentation/swiftui/toolbaritemaxisbehavior) and UIKit [axisBehavior](https://developer.apple.com/documentation/uikit/uibarbuttonitem/axisbehavior-swift.property).
- Edge: [toolbarVerticalEdge](https://developer.apple.com/documentation/swiftui/environmentvalues/toolbarverticaledge) and [verticalBarEdge](https://developer.apple.com/documentation/uikit/uitraitcollection/verticalbaredge).
- Opt-out: [toolbarVerticalBehavior(_:)](https://developer.apple.com/documentation/swiftui/view/toolbarverticalbehavior(_:)) and [preferredVerticalBarBehavior](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredverticalbarbehavior).
- Compression: [toolbarVerticalCompressionBehavior(_:)](https://developer.apple.com/documentation/swiftui/view/toolbarverticalcompressionbehavior(_:)) and [verticalBarCompressionBehavior](https://developer.apple.com/documentation/uikit/uinavigationitem/verticalbarcompressionbehavior).
- Priority and overflow: [ToolbarItemVisibilityPriority](https://developer.apple.com/documentation/swiftui/toolbaritemvisibilitypriority) / [UIBarButtonItemVisibilityPriority](https://developer.apple.com/documentation/uikit/uibarbuttonitemvisibilitypriority), [ToolbarOverflowMenu](https://developer.apple.com/documentation/swiftui/toolbaroverflowmenu) / [additionalOverflowItems](https://developer.apple.com/documentation/uikit/uinavigationitem/additionaloverflowitems).
- Placement: [topBarPinnedTrailing](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/topbarpinnedtrailing) / [pinnedTrailingGroup](https://developer.apple.com/documentation/uikit/uinavigationitem/pinnedtrailinggroup), [cancellationAction](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/cancellationaction) / [leadingItemGroups](https://developer.apple.com/documentation/uikit/uinavigationitem/leadingitemgroups).
- [SwiftUI Toolbars](https://developer.apple.com/documentation/swiftui/toolbars) and [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) for container ownership.

## Which bars move

Bars supplied by navigation containers move to the vertical axis: SwiftUI `toolbar(content:)` on a `NavigationStack` or `NavigationSplitView`, or UIKit items on a view controller inside a navigation controller. A hand-built `UIToolbar`, `UINavigationBar`, or `UITabBar` does not.

- Controls sit on the side on the outer display and on the inner display in landscape. The inner display in portrait keeps standard horizontal bars.
- In a split view showing several columns, the sidebar and content columns keep horizontal bars and the detail column gets the vertical bar. Inspectors keep horizontal bars.
- Sheets on the outer display get vertical bars by default. On the inner display, centered and leading sheets keep horizontal bars and trailing sheets get vertical ones. Choose the sheet position with [presentationPlacement(_:)](https://developer.apple.com/documentation/swiftui/view/presentationplacement(_:)) or [preferredPlacement](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/preferredplacement).
- In Split View multitasking on the inner display, each app puts its controls along its own outer edge.
- To extend a hero or background image under the vertical bar, use [backgroundExtensionEffect()](https://developer.apple.com/documentation/swiftui/view/backgroundextensioneffect()) or [UIBackgroundExtensionView](https://developer.apple.com/documentation/uikit/uibackgroundextensionview).

## Order and representation

Reserve the top of the vertical axis for Back or Close, followed by prominent actions such as Done. A navigation controller adds Back automatically. Use `topBarPinnedTrailing` or `pinnedTrailingGroup` for a prominent item like Done, and `cancellationAction` or `leadingItemGroups` for a custom Back or Close. Group items with `ToolbarItemGroup` or `UIBarButtonItemGroup` rather than adding fixed spacing.

The system chooses a representation per context:

- Vertical placement uses the icon. Horizontal placement uses the icon or title, preferring the icon. Overflow uses both.
- An item with a title and no icon, or with a custom view, is not presented vertically. The automatic axis behavior treats image items as supporting both axes and text or custom-view items as horizontal only.
- `.horizontalOnly` hides the item when no horizontal bar is present. `.verticalPreferred` puts it in the vertical bar when both bars exist. Start with automatic behavior and opt in deliberately.
- Keyboard accessory bars stay attached to the keyboard.

## Space pressure

Items overflow from bottom to top by default. Set visibility priority on whole groups first, then on items inside a group. Keep frequent actions and status-bearing items, such as badged items, visible longest. Move any custom overflow menu into the system one and keep the ellipsis symbol for overflow.

When the tab bar and toolbar items share the vertical bar, the default compresses toolbar items first, which suits navigation-focused screens. Task-focused screens can prefer to keep toolbar items with `.prefersToolbarItems` (SwiftUI) or `.prefersBarItems` (UIKit).

## Edge and opt-out

`toolbarVerticalEdge` and `verticalBarEdge` report the system's preferred edge for the vertical bar even when no vertical bar is visible, and return `nil` or `.unspecified` only where the system never places one. They do not tell you whether a bar is showing right now. Read them rather than assuming the right side. The HIG says the bar stays aligned with the hardware and keeps its side in right-to-left languages, while the SwiftUI page says the edge depends on locale and device; read the value either way.

`toolbarVerticalBehavior(.disabled)` and a `preferredVerticalBarBehavior` of `.disabled` send bar content back to horizontal top and bottom bars. Apple limits this to screens better served by horizontal bars, such as a full-screen video player or a non-scrolling calculator-style layout, and asks you to keep the choice stable. To hide bars on a screen, use the visibility APIs instead. In SwiftUI the value resolves per container: a navigation stack uses its top view, a tab view its selected view, and a navigation split view its trailing-most column. In UIKit, call `setNeedsUpdateOfVerticalBarConfiguration()` after changing the preference. The HIG otherwise says not to override the default bar placement.

## Supplementary session

[Raise the bar](https://developer.apple.com/videos/play/tech-talks/111462/), reviewed 2026-09-09 and rechecked 2026-09-25:

- **2:00–3:09:** Bars managed by navigation containers participate; standalone UIKit bar instances do not. Navigation, toolbar, and tab controls share a region.
- **5:56–9:00:** Titles remain important in overflow even for symbol presentations. A text item carrying real information, such as a cart total, is better kept horizontal.
- **10:07:** Flexible spacers have zero height on the vertical axis; fixed spacers keep their minimum.
- **11:40–13:10:** The keyboard and Picture in Picture in open portrait compete for bar space; review compression, overflow, and priority together.
- **14:21:** Disable vertical bars only where the experience warrants it.

The action inventory and acceptance workflow are repository recommendations.
