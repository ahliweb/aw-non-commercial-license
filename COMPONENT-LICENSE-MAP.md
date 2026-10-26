# COMPONENT-LICENSE-MAP: Component-Level Scope and Provenance (TEMPLATE)

This is **only an illustrative template**, not an audit or real component inventory. Populate accurately for every adopting software project. See [AW-NC 3.0.0 §8](LICENSE.md#8-coexisting-licenses-and-scope-of-new-developments).

## Rules

- Preserve each original valid license within its actual legal scope. The original grant does not disappear just because AW-NC files coexist in the same software repository.
- AW-NC covers only new **original and independently licensable contributions expressly designated by an authorized owner**. Newer modifications to third-party code are **not automatically AW-NC**.
- Analyze actual derivative/combined works and GPL/AGPL/copyleft; file locations, paths and separate deploys are not themselves determinative.
- Keep notices, patent terms, corresponding source offers, relevant EULAs and contributor permission evidence.

| Illustrative component (not real) | Origin / rightsholder | License | AW-NC scope | Obligations |
|---|---|---|---|---|
| `vendor/example-mit/` | Example external author | MIT | None | Retain MIT attribution |
| `vendor/example-apache/` | Example external author | Apache-2.0 | None | Retain Apache NOTICE and applicable patent terms |
| `vendor/example-gpl/` | Example external author | GPL-3.0-only | None | Confirm source/copyleft obligations for actual combination |
| `src/example-original-aw-module/` | Example verified AW copyright | LicenseRef-AW-NC-3.0.0 | Only if owner authorizes and expressly designates | Track commercial rights and scope |
| `contrib/unverified/` | Rights not verified | UNKNOWN | Not presumed | Hold release and clarify ownership |

## Required real evidence

Record a component ID, source/repository URL, file paths, version/tag/SHA, copyright owners, original license and license text, dependencies, modification history, authorship/contributor grants, linked/combined-work determination, patent and notice requirements, license expression, commercial rights, exception approval, approver and review date. Store sensitive commercial agreements privately.

## Example SPDX tags (not an actual grant)

```text
SPDX-License-Identifier: MIT
SPDX-License-Identifier: LicenseRef-AW-NC-3.0.0
SPDX-License-Identifier: MIT OR LicenseRef-AW-NC-3.0.0
SPDX-License-Identifier: MIT AND LicenseRef-AW-NC-3.0.0
```

The `OR` example requires actual authorization offering alternatives **for the same work**; `AND` denotes legitimately cumulative licensing obligations. Having an MIT file plus an AW file does **not** automatically create dual-license choice for the entire product. Custom SPDX LicenseRefs must supply full extracted text; no SPDX or OSI approval is implied.

## Acceptance checklist

- [ ] Third-party code inventories and original licenses verified
- [ ] Corresponding notices and source offers preserved where required
- [ ] Original AW-owned code expressly scoped as AW-NC
- [ ] Contributor rights and commercial grants verified
- [ ] GPL/AGPL derivative/combined work assessment recorded
- [ ] Incompatible combinations withheld from release until resolved
- [ ] SBOM and license mapping attached to release record

[Source comparison](docs/comparison.md) · [Compliance guidance](docs/license-compliance-governance.md) · [SPDX license syntax](https://github.com/spdx/using/blob/main/docs/license-id-in-source.md).
