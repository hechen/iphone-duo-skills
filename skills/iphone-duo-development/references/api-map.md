# iPhone Duo API map

Checked 2026-09-25 against Apple's documentation and the iOS 27.1 SDK (24A94403) in Xcode 27.1 (27A9269). Pages marked beta can still change; recheck the declaration in the SDK you build with.

**Probe** means the symbol is type-checked by this repository's [SDK probe](https://github.com/hechen/iphone-duo-skills/blob/main/tests/iPhoneDuoProbe.swift) for `arm64-apple-ios27.1` and the matching simulator target. A type-check proves spelling and availability only; it does not run the behavior. **Docs** means the symbol was checked in Apple's documentation but is not in the probe.

Start with Apple's [Preparing your app for iPhone Duo](https://developer.apple.com/documentation/technologyoverviews/preparing-your-app-for-iphone-duo) and the [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo) HIG page.

## Layout and reserved regions (`iphone-duo-layout`)

| SwiftUI | UIKit | Since | Check |
| --- | --- | --- | --- |
| [`GeometryProxy.reservedRegions(kind:options:layoutDirectionBehavior:)`](https://developer.apple.com/documentation/swiftui/geometryproxy/reservedregions(kind:options:layoutdirectionbehavior:)) | [`UIView.reservedRegions(kind:options:)`](https://developer.apple.com/documentation/uikit/uiview/reservedregions(kind:options:)) | iOS 27.1 | Probe |
| [`ReservedRegion`](https://developer.apple.com/documentation/swiftui/reservedregion) (`kind`, `frame`, `margins`, `isActive`) | [`UIView.ReservedRegion`](https://developer.apple.com/documentation/uikit/uiview/reservedregion) | iOS 27.1 | Probe |
| `ReservedRegion.QueryOptions.includeInactive` | `UIView.ReservedRegion.QueryOptions.includeInactive` | iOS 27.1 | Probe |
| [`ArrangementView`](https://developer.apple.com/documentation/swiftui/arrangementview) with [`arrangementViewStyle(_:)`](https://developer.apple.com/documentation/swiftui/view/arrangementviewstyle(_:)) `.split` / `.overlay` and `axes(_:)` | [`UIArrangementViewController`](https://developer.apple.com/documentation/uikit/uiarrangementviewcontroller) with `updateArrangement(_:)`, `setViewController(_:for:)`, `state(for:)` | iOS 27.1 | Probe |
| [`EnvironmentValues.overlayArrangementZIndex`](https://developer.apple.com/documentation/swiftui/environmentvalues/overlayarrangementzindex) | `UIArrangementViewController.ViewState.zIndex` | iOS 27.1 | Probe |

## Bars on the vertical axis (`iphone-duo-toolbars`)

| SwiftUI | UIKit | Since | Check |
| --- | --- | --- | --- |
| [`axisBehavior(_:)`](https://developer.apple.com/documentation/swiftui/toolbarcontent/axisbehavior(_:)) with [`ToolbarItemAxisBehavior`](https://developer.apple.com/documentation/swiftui/toolbaritemaxisbehavior) | [`UIBarButtonItem.axisBehavior`](https://developer.apple.com/documentation/uikit/uibarbuttonitem/axisbehavior-swift.property) | iOS 27.1 | Probe |
| [`toolbarVerticalEdge`](https://developer.apple.com/documentation/swiftui/environmentvalues/toolbarverticaledge) | [`UITraitCollection.verticalBarEdge`](https://developer.apple.com/documentation/uikit/uitraitcollection/verticalbaredge) | iOS 27.1 | Probe |
| [`toolbarVerticalBehavior(_:)`](https://developer.apple.com/documentation/swiftui/view/toolbarverticalbehavior(_:)) | [`preferredVerticalBarBehavior`](https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredverticalbarbehavior) and [`setNeedsUpdateOfVerticalBarConfiguration()`](https://developer.apple.com/documentation/uikit/uiviewcontroller/setneedsupdateofverticalbarconfiguration()) | iOS 27.1 | Probe |
| [`toolbarVerticalCompressionBehavior(_:)`](https://developer.apple.com/documentation/swiftui/view/toolbarverticalcompressionbehavior(_:)) | [`UINavigationItem.verticalBarCompressionBehavior`](https://developer.apple.com/documentation/uikit/uinavigationitem/verticalbarcompressionbehavior) | iOS 27.1 | Probe |
| [`topBarPinnedTrailing`](https://developer.apple.com/documentation/swiftui/toolbaritemplacement/topbarpinnedtrailing) | [`pinnedTrailingGroup`](https://developer.apple.com/documentation/uikit/uinavigationitem/pinnedtrailinggroup) | iOS 27.0 / 16.0 | Probe / Docs |
| [`visibilityPriority(_:)`](https://developer.apple.com/documentation/swiftui/toolbarcontent/visibilitypriority(_:)) | [`UIBarButtonItem.visibilityPriority`](https://developer.apple.com/documentation/uikit/uibarbuttonitem/visibilitypriority) | iOS 27.0 | Probe / Docs |
| [`ToolbarOverflowMenu`](https://developer.apple.com/documentation/swiftui/toolbaroverflowmenu) | [`additionalOverflowItems`](https://developer.apple.com/documentation/uikit/uinavigationitem/additionaloverflowitems) | iOS 27.0 / 16.0 | Docs |
| [`presentationPlacement(_:)`](https://developer.apple.com/documentation/swiftui/view/presentationplacement(_:)) | [`UISheetPresentationController.preferredPlacement`](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/preferredplacement) | iOS 27.0 | Docs |

## Scenes, hinge, and accessories (`iphone-duo-scenes`)

| SwiftUI | UIKit | Since | Check |
| --- | --- | --- | --- |
| [`onHingeChange(isEnabled:_:)`](https://developer.apple.com/documentation/swiftui/view/onhingechange(isenabled:_:)) with [`DeviceHingeContext`](https://developer.apple.com/documentation/swiftui/devicehingecontext) | [`UIHingeInteraction`](https://developer.apple.com/documentation/uikit/uihingeinteraction) | iOS 27.1 | Probe |
| [`sceneAccessory(content:)`](https://developer.apple.com/documentation/swiftui/view/sceneaccessory(content:)) with [`CameraCaptureAccessory`](https://developer.apple.com/documentation/swiftui/cameracaptureaccessory) | [`UISceneAccessory`](https://developer.apple.com/documentation/uikit/uisceneaccessory) `cameraCapture(sceneConfiguration:)` and [`registerSceneAccessory(_:)`](https://developer.apple.com/documentation/uikit/uiviewcontroller/registersceneaccessory(_:)) | iOS 27.1 for camera capture | Probe |
| [`onAvailabilityChange(perform:)`](https://developer.apple.com/documentation/swiftui/sceneaccessorycontent/onavailabilitychange(perform:)), `CameraCaptureAccessory(isEnabled:content:)` | [`UISceneAccessoryRegistration`](https://developer.apple.com/documentation/uikit/uisceneaccessoryregistration) `isAvailable`, `isEnabled` | iOS 27.0 | Probe |
| — | [`UISceneSession.Role.windowCameraCaptureAccessory`](https://developer.apple.com/documentation/uikit/uiscenesession/role-swift.struct/windowcameracaptureaccessory) | iOS 27.1 | Probe |
| [`ExternalNonInteractiveAccessory`](https://developer.apple.com/documentation/swiftui/externalnoninteractiveaccessory) | — | iOS 27.0 | Docs |
| — | [`UIWindowScene.ActivationAction`](https://developer.apple.com/documentation/uikit/uiwindowscene/activationaction) | iOS 15.0 | Probe |

## Camera (`iphone-duo-camera`)

| API | Since | Check |
| --- | --- | --- |
| [`AVCaptureDeviceDirectionCoordinator`](https://developer.apple.com/documentation/avkit/avcapturedevicedirectioncoordinator) (AVKit), `AVCaptureDeviceDirectionMap`, `AVCaptureDeviceDescriptor` | iOS 27.1 | Probe |
| [`builtInOuterUltraWideCamera`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtinouterultrawidecamera), [`builtInInnerUltraWideCamera`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtininnerultrawidecamera) | iOS 27.1 | Probe |
| [`AVCaptureDevice.RotationCoordinator`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator) | iOS 17.0 | Docs |
| [`activePrimaryConstituent`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/activeprimaryconstituent), [`automaticallyAdjustsVideoMirroring`](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/automaticallyadjustsvideomirroring) | Earlier releases | Docs |
| [`dynamicAspectRatio`](https://developer.apple.com/documentation/avfoundation/avcapturedevice/dynamicaspectratio), [`isCameraSensorOrientationCompensationEnabled`](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/iscamerasensororientationcompensationenabled) | iOS 26.0 | Docs |

## Platform exclusions

The iOS 27.1 SDK marks the camera-capture accessory unavailable on Mac Catalyst. Xcode 27.1 beta also reports compile errors for other 27.1-only APIs in Catalyst builds. Guard Duo code with `#if !targetEnvironment(macCatalyst)` where the app builds for Catalyst, and read each declaration's platform list before sharing code with other platforms.
