#!/usr/bin/env bash
# Type-check tests/iPhoneDuoProbe.swift against the selected Xcode's iOS SDKs.
# Requires macOS with an Xcode whose iOS SDK declares the iPhone Duo APIs (27.1 or later).
# A higher version number alone does not prove Duo support, so this fails loudly
# when the declarations are missing instead of skipping them.
set -euo pipefail

skillset_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
probe="$skillset_root/tests/iPhoneDuoProbe.swift"

xcodebuild -version
for skillset_spec in 'iphoneos arm64-apple-ios27.1' 'iphonesimulator arm64-apple-ios27.1-simulator'; do
  read -r skillset_sdk skillset_target <<< "$skillset_spec"
  skillset_sdk_path="$(xcrun --sdk "$skillset_sdk" --show-sdk-path)"
  printf 'SDK: %s %s (%s)\n' "$skillset_sdk" \
    "$(xcrun --sdk "$skillset_sdk" --show-sdk-version)" \
    "$(xcrun --sdk "$skillset_sdk" --show-sdk-build-version)"
  xcrun swiftc -typecheck -sdk "$skillset_sdk_path" -target "$skillset_target" "$probe"
  printf 'Type-check passed: %s\n' "$skillset_target"
done
