# Fixture 04-gpl-aggregation

Separate program aggregated with GPL software (aggregation vs combined work)

> Illustrative scenario, not a real project and not legal advice. Expected decision is a **working hypothesis pending qualified IP counsel review**.

## Project tree

```text
bin/gpl-tool (unmodified)
bin/aw-tool (communicates via CLI/pipes)
```

## Copyright chain

Upstream GPL authors; AW (aw-tool)

## Required notices

- Provide GPL text and Corresponding Source for gpl-tool.
- Document why aw-tool is a separate work (GPL FAQ 'mere aggregation').

## Expected review decision: `needs-counsel-review`

Genuine aggregation may keep AW-NC for aw-tool; shared address space, intimate data structures or static linking make it a combined work (see fixture 02). Separate directories are not determinative.

Files: [sbom.spdx.json](sbom.spdx.json) · [expected-decision.json](expected-decision.json) · [LICENSE-MAP](../../../LICENSE-MAP.md)
