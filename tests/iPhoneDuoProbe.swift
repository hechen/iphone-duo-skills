import SwiftUI
import UIKit
import AVKit
import AVFoundation

// Type-check probe only. It proves that the selected SDK declares these symbols
// with these spellings for iOS 27.1. It does not run layout, camera, or accessory
// behavior. Run it with scripts/check-sdk.sh.

@available(iOS 27.1, *)
struct DuoArrangementProbe: View {
    @State private var showsScript = true
    @Environment(\.toolbarVerticalEdge) private var verticalEdge
    @Environment(\.overlayArrangementZIndex) private var zIndex

    var body: some View {
        NavigationStack {
            ArrangementView {
                Button("Pause", systemImage: "pause") { }
                    .opacity(zIndex == 0 ? 1 : 0.5)
            } secondary: {
                Color.black
            }
            .arrangementViewStyle(.overlay)
            .onHingeChange { _, newContext in
                _ = newContext.hinge?.angle
                _ = newContext.hinge?.status
            }
            .sceneAccessory {
                CameraCaptureAccessory(isEnabled: $showsScript) { Text("Capture status") }
                    .onAvailabilityChange { _ in }
            }
            .toolbar {
                ToolbarItem(placement: .topBarPinnedTrailing) {
                    Button("Done", systemImage: "checkmark") { }
                }
                ToolbarItem { Button("Save", systemImage: "square.and.arrow.down") { } }
                    .axisBehavior(.verticalPreferred)
                    .visibilityPriority(.high)
            }
            .toolbarVerticalCompressionBehavior(.prefersToolbarItems)
            .toolbarVerticalBehavior(.automatic)
            .frame(maxWidth: .infinity, alignment: verticalEdge == .trailing ? .trailing : .leading)
        }
    }
}

@available(iOS 27.1, *)
struct DuoSplitProbe: View {
    var body: some View {
        ArrangementView {
            Text("Now playing")
        } secondary: {
            Text("Lyrics")
        }
        .arrangementViewStyle(.split.axes(.horizontal))
    }
}

@available(iOS 27.1, *)
func activeDivisions(_ geometry: GeometryProxy) -> [ReservedRegion] {
    geometry.reservedRegions(kind: .division, options: .includeInactive, layoutDirectionBehavior: .mirrors)
        .filter(\.isActive)
}

@available(iOS 27.1, *)
@MainActor
func configureUIKitProbe(_ view: UIView) -> UIArrangementViewController {
    _ = view.reservedRegions(kind: .occlusion).filter(\.isActive)
    _ = view.reservedRegions(kind: .division, options: .includeInactive).map(\.margins)
    _ = view.traitCollection.verticalBarEdge
    view.addInteraction(UIHingeInteraction { _, update in
        _ = update.hinge?.angle
        _ = update.hinge?.status
    })
    let controller = UIArrangementViewController()
    controller.setViewController(UIViewController(), for: .primary)
    controller.setViewController(UIViewController(), for: .secondary)
    controller.updateArrangement(.split.axes(.horizontal))
    _ = controller.state(for: .secondary)?.zIndex
    let item = UIBarButtonItem(title: "Save", image: UIImage(systemName: "square.and.arrow.down"),
                               primaryAction: nil, menu: nil)
    item.axisBehavior = .verticalPreferred
    controller.navigationItem.rightBarButtonItem = item
    controller.navigationItem.verticalBarCompressionBehavior = .prefersBarItems
    return controller
}

@available(iOS 27.1, *)
final class DuoPlayerViewController: UIViewController {
    // A full-screen player is one of the cases Apple names for disabling the vertical bar.
    override var preferredVerticalBarBehavior: UIVerticalBarBehavior { .disabled }

    func preferenceChanged() {
        setNeedsUpdateOfVerticalBarConfiguration()
    }
}

@available(iOS 27.1, *)
final class DuoCaptureViewController: UIViewController {
    private var registration: UISceneAccessoryRegistration?

    override func viewDidLoad() {
        super.viewDidLoad()
        let configuration = UISceneConfiguration()
        let accessory = UISceneAccessory.cameraCapture(sceneConfiguration: configuration)
        registration = registerSceneAccessory(accessory)
        registration?.isEnabled = true
        _ = registration?.isAvailable
        _ = UISceneSession.Role.windowCameraCaptureAccessory
    }

    func stopOffering() {
        if let registration { unregisterSceneAccessory(registration) }
    }
}

@available(iOS 27.1, *)
@MainActor
func newWindowAction() -> UIWindowScene.ActivationAction {
    UIWindowScene.ActivationAction { _ in
        UIWindowScene.ActivationConfiguration(userActivity: NSUserActivity(activityType: "example.open"))
    }
}

@available(iOS 27.1, *)
@MainActor
func cameraDirectionProbe(_ preview: UIView) -> AVCaptureDeviceDirectionCoordinator {
    let coordinator = AVCaptureDeviceDirectionCoordinator(
        view: preview,
        deviceTypes: [.builtInOuterUltraWideCamera, .builtInInnerUltraWideCamera, .builtInDualWideCamera]
    ) { directions in
        let forward: [AVCaptureDeviceDescriptor] = directions.forwardFacingDeviceDescriptors
        _ = forward.first?.uniqueID
        _ = directions.backwardFacingDeviceDescriptors
    }
    _ = coordinator.deviceDirections.forwardFacingDeviceDescriptors
    return coordinator
}
