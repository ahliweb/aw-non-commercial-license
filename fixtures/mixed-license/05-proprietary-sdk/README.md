# Fixture 05-proprietary-sdk

Proprietary SDK/EULA bundled with an AW-NC feature

> Illustrative scenario, not a real project and not legal advice. Expected decision is a **working decision accepted by the AhliWeb team, not independently reviewed by counsel**.

## Project tree

```text
third_party/vendor-sdk (EULA)
src/aw-feature
```

## Copyright chain

SDK vendor; AW (aw-feature)

## Required notices

- A paid AW license does not sublicense the SDK; the SDK EULA governs it.
- Verify EULA permits redistribution/bundling before release.

## Expected review decision: `allow-with-conditions`

AW-NC cannot grant rights in the SDK. Release blocked until EULA redistribution rights are evidenced.

Files: [sbom.spdx.json](sbom.spdx.json) · [expected-decision.json](expected-decision.json) · [COMPONENT-LICENSE-MAP](../../../COMPONENT-LICENSE-MAP.md)
