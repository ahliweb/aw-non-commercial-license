# Fixture 08-historic-versions-coexist

Historic AW-NC 1.0.0/2.0.0 code coexisting with 3.0.0 components

> Illustrative scenario, not a real project and not legal advice. Expected decision is a **working hypothesis pending qualified IP counsel review**.

## Project tree

```text
legacy/ (AW-NC 1.0.0 release)
modules/v2 (AW-NC 2.0.0)
src/new (AW-NC 3.0.0)
```

## Copyright chain

AW (all); contributor grants must be checked per edition

## Required notices

- Preserve the edition text next to each component (licenses/AW-NC-*.md).
- Do not relicense another author's contribution to a newer edition without authority.

## Expected review decision: `allow-with-conditions`

Each edition applies prospectively to its own scope; per-file edition identification is required.

Files: [sbom.spdx.json](sbom.spdx.json) · [expected-decision.json](expected-decision.json) · [LICENSE-MAP](../../../LICENSE-MAP.md)
