# Sources and verification status

Reviewed on **2026-09-09**. The Apple Developer hub and the six session pages were retrieved directly. Session summaries and displayed code establish announcement evidence; they do not establish successful compilation or runtime behavior.

| Resource | Used for |
| --- | --- |
| [Get ready for iPhone Duo](https://developer.apple.com/iphone-duo/) | Toolchain/documentation release status. |
| [Apple unveils iPhone Duo](https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/) | Official product identity and announcement. |
| [Design for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111466/) | Design skill. |
| [Prepare your app for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111461/) | Readiness skill. |
| [Raise the bar with iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111462/) | Toolbar skill. |
| [Strike a pose with adaptive layouts on iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111463/) | Layout skill. |
| [Leverage multiple displays and scenes on iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111464/) | Scenes and hinge interactions skill. |
| [Build a great camera experience for iPhone Duo](https://developer.apple.com/videos/play/tech-talks/111465/) | Camera skill. |
| [Performing accessibility audits for your app](https://developer.apple.com/documentation/accessibility/performing-accessibility-audits-for-your-app) | Testing skill; automated audit limitations. |

## Interpreting the content

**Session evidence:** A behavior or symbol shown in a linked Apple session. Timestamps in skill references identify the relevant section.

**Repository recommendation:** Our engineering procedures, state-ownership checks, example scenarios, and reporting conventions. They are not Apple requirements.

**SDK verified:** Requires inspecting declarations in the actual selected SDK and building the affected target. No iOS 27.1 implementation in this repository currently carries this status.

**Runtime verified:** Requires executing the relevant scenario and retaining its result on the named runtime or physical device. Static review and compilation do not establish this status.

When sources change, update the affected skill, its verification date, and any tested compatibility claim together. Do not infer public API access from a consumer feature announcement.
