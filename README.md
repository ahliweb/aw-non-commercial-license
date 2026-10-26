# AW Non-Commercial License 3.0.0

**Current canonical license:** [LICENSE.md](LICENSE.md) · **Version:** [VERSION](VERSION) · **Prior historical licenses:** [1.0.0](licenses/AW-NC-1.0.0.md) and [2.0.0](licenses/AW-NC-2.0.0.md).

AW-NC is a custom **source-available license, NOT OSI-approved open source**. Noncommercial use, copying, modification and redistribution of properly identified AW-NC Covered Material are subject to its terms. Commercial use (including paid SaaS, consulting, or revenue-supporting business operations) requires prior written authorization: **commercial@ahliweb.com**.

## New in 3.0.0 — Existing licenses are respected

**[Section 8](LICENSE.md#8-coexisting-licenses-and-scope-of-new-developments)** preserves pre-existing MIT, Apache, GPL, AGPL, proprietary, or other licenses **within their actual legal scope**. An AW-NC repository may contain multiple components with distinct rights; AW-NC does not relicense third-party code automatically.

AW-NC applies to an independently licensable **new original enhancement only when** its authorized copyright holder(s) expressly license the identified work as AW-NC. New modifications of existing GPL/AGPL or other third-party material remain subject to applicable source/reciprocal rights. No incompatible combined distribution becomes legal simply because AW-NC coexists in the same repository.

- [LICENSE-MAP.md](LICENSE-MAP.md): template to document per-component owners/licenses and SPDX expressions
- [Similar licenses comparison](docs/comparison.md): AFPL, PolyForm, BSL, Commons Clause, SSPL, Elastic and MIT
- [License governance](docs/license-compliance-governance.md): provenance, attribution, copyleft compatibility
- [SBOM and provenance checks](docs/sbom-and-provenance.md): local scripts, SPDX LicenseRef example, mixed-license fixtures

## Islamic covenant (retained)

**Section 5** affirms the licensor's solemn contractual amanah and accountability before **Allah Jalla wa 'Ala**, according to Ahlus Sunnah wal Jama'ah with the understanding of the Salaf. Upholding valid rights of other authors and contributors is also an amanah. The license requires no religious oath, conversion or religious court and does not replace national civil law. Neither legal nor Sharia certification is claimed. [Akad explanation in Indonesian](docs/akad-syari-id.md).

## Semantic Versioning and history

[SemVer policy](docs/semantic-versioning.md) uses MAJOR for legal changes, MINOR for non-binding guidance, and PATCH for strictly non-substantive corrections. Current 3.0.0 introduces substantive license-scope Section 8. [CHANGELOG](CHANGELOG.md). The prior complete 1.0.0 and 2.0.0 texts remain immutable and earlier software grants are not retroactively replaced.

`LicenseRef-AW-NC-3.0.0` is a *custom SPDX reference* requiring extracted license text, not an OSI/SPDX License List approval. Software projects must explicitly select a version and have rights-holder authority.

## Primary documents

- [LICENSE.md](LICENSE.md) — complete current legal text where adopted
- [LICENSE-MAP.md](LICENSE-MAP.md) — mixed-license component tracking template
- [docs/comparison.md](docs/comparison.md) — similar licenses, risks and scenarios
- [docs/evidence-and-references.md](docs/evidence-and-references.md) — scholarly, statutory and juristic source register
- [docs/akad-syari-id.md](docs/akad-syari-id.md) — Islamic contractual ethics and respecting other rightsholders
- [docs/adoption-guide.md](docs/adoption-guide.md) — adopting the license
- [docs/semantic-versioning.md](docs/semantic-versioning.md) — version policy
- [COMMERCIAL-LICENSING.md](COMMERCIAL-LICENSING.md) — how to request a commercial grant
- [releases/3.0.0.md](releases/3.0.0.md) — release record / pending independent expert approvals

Verify locally: `python3 scripts/validate_license.py`. This checks version consistency and unchanged history, not the legal validity of a combined work.
