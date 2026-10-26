# Fixture 02-modified-gpl3

Modified GPL-3.0 code inside the same copyrightable work

> Illustrative scenario, not a real project and not legal advice. Expected decision is a **working decision accepted by the AhliWeb team, not independently reviewed by counsel**.

## Project tree

```text
vendor/gpl-lib (modified by AW)
src/aw-patch (derived from gpl-lib)
```

## Copyright chain

Upstream GPL authors; AW (modifications, GPL-3.0-only forced)

## Required notices

- Modifications of GPL code must remain GPL-3.0 on distribution.
- AW-NC non-commercial restriction would be an additional restriction (GPL-3.0 s.10) and is not authorized.

## Expected review decision: `block`

BLOCK distribution under AW-NC for derivative parts. Section 8 does not override GPL obligations.

Files: [sbom.spdx.json](sbom.spdx.json) · [expected-decision.json](expected-decision.json) · [COMPONENT-LICENSE-MAP](../../../COMPONENT-LICENSE-MAP.md)
