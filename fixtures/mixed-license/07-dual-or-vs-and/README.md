# Fixture 07-dual-or-vs-and

Genuine alternative dual licensing (OR) versus cumulative terms (AND)

> Illustrative scenario, not a real project and not legal advice. Expected decision is a **working decision accepted by the AhliWeb team, not independently reviewed by counsel**.

## Project tree

```text
vendor/dual-or
vendor/cumulative-and
```

## Copyright chain

Upstream authors

## Required notices

- Record the SPDX operator verbatim; never collapse AND into OR.
- For OR, document the elected license; for AND, satisfy all terms.

## Expected review decision: `allow-with-conditions`

OR gives a choice; AND is cumulative. SBOM must preserve the expression exactly.

Files: [sbom.spdx.json](sbom.spdx.json) · [expected-decision.json](expected-decision.json) · [COMPONENT-LICENSE-MAP](../../../COMPONENT-LICENSE-MAP.md)
