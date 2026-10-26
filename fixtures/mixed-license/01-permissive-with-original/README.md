# Fixture 01-permissive-with-original

MIT and Apache-2.0 dependencies alongside original AW-owned code

> Illustrative scenario, not a real project and not legal advice. Expected decision is a **working hypothesis pending qualified IP counsel review**.

## Project tree

```text
src/aw-module (AW original)
vendor/mit-lib
vendor/apache-lib
```

## Copyright chain

AW Ltd (aw-module); upstream authors (vendor/*)

## Required notices

- Retain MIT copyright/permission notice and Apache-2.0 LICENSE/NOTICE.
- AW-NC applies only to src/aw-module.

## Expected review decision: `allow-with-conditions`

Permissive licenses are preserved in scope; AW-NC covers only designated original code. Confirm AW sole authorship (DCO/assignment) first.

Files: [sbom.spdx.json](sbom.spdx.json) · [expected-decision.json](expected-decision.json) · [COMPONENT-LICENSE-MAP](../../../COMPONENT-LICENSE-MAP.md)
