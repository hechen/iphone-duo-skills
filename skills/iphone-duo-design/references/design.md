# Design evidence

## Written documentation — start here

Checked 2026-09-25:

- [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo): the primary HIG page, published 2026-09-09. Read the section relevant to the screen under review.
- [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) and [Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios): general guidance that still applies; iPhone Duo is still an iPhone.
- [Apple Design Resources](https://developer.apple.com/design/resources/): official templates, margins, and safe areas. Follow their usage terms rather than redistributing them with the skill.

## What the HIG says

- **Anatomy.** The outer display is compact width and the inner display regular width. The outer front camera sits in a corner and is always visible; the inner camera is hidden behind the display until it is active, when the interface moves aside.
- **Poses.** People hold the device like a book, set it down, or stand it on an edge. Use size classes so the layout adapts, instead of designing a layout per pose.
- **Consistency.** Keep functionality and element state the same on both displays. Keep the information hierarchy, and show an extra level on the inner display only when it suits the content.
- **Folding.** Many system components move around the fold on their own. Prefer containers that adapt automatically; in grids, prefer an even number of columns. Avoid extreme layout changes as people fold the device, and move only what must move.
- **Arrangements.** Consider one when the layout already resembles it. Keep navigation outside arrangement views.
- **Vertical controls.** Account for the asymmetric space bars create, keep controls' relative positions similar across poses, keep controls near the content they affect, and generally keep the default bar placement. Interfaces that need no bars, such as a non-scrolling immersive screen, can span the full width as long as nothing collides with the Dynamic Island or status bar.
- **Games.** A game may lock to portrait or landscape but should fill the screen in every pose. Prefer changing the aspect ratio over letterboxing; if padding is unavoidable, fill it with artwork.

## Supplementary session

[Design for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111466/), reviewed 2026-09-09:

- **0:28–3:42:** Plan for changing available space rather than an independent interface for every physical pose. Compact and regular size classes guide adaptation.
- **5:07:** Edge controls share space with system elements and can overflow; wide controls need a suitable representation.
- **6:33:** Safe-area alignment protects ordinary foreground content. An immersive background can use different alignment from text and controls.
- **7:34:** Expanded layouts can reveal more hierarchy or related content.
- **8:36:** System sheets vary between displays and move around the fold.
- **9:28:** System components help keep interactive elements away from the fold. Continuously scrolling content is treated differently.

These are design observations, not exact point dimensions or API declarations. The continuity mapping, review format, and acceptance workflow in the skill are repository recommendations.
