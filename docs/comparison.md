# AW-NC 3.0.0 and Comparable Source-Available Licenses

**Reviewed:** 2026-10-26 · **Canonical AW-NC:** [LICENSE.md](../LICENSE.md) (only where expressly designated by a rights holder). Earlier editions are [1.0.0](../licenses/AW-NC-1.0.0.md) and [2.0.0](../licenses/AW-NC-2.0.0.md). The interpretation below is based on each linked license text, not on independently tested judicial rulings.

## Seven license approaches plus an open-source baseline

| License | Business internal use | SaaS / hosted service | Paid distribution and adaptations | Distinguishing rule |
|---|---|---|---|---|
| **[AW Non-Commercial 3.0.0](../LICENSE.md)** | Written permission required for revenue-supporting commercial use | Paid SaaS requires prior written authorization | Noncommercial use/modification/distribution allowed as specified; Section 8 preserves original third-party license scope | Solemn Islamic covenant (§5); only expressly designated rights-held new additions under AW-NC (§8) |
| **[Aladdin AFPL](https://spdx.org/licenses/Aladdin.html)** | Functional running is expressly unrestricted by §2(b) | Running alone is not prohibited, but any paid delivery/distribution must be analyzed | Paid commercial distribution restricted (§2(a)); distributed covered modifications entail detailed source/notice conditions (§2(c)) | Primarily controls compensated distribution, not revenue-supporting internal operation |
| **[PolyForm Noncommercial 1.0.0](https://polyformproject.org/licenses/noncommercial/1.0.0)** | Noncommercial purposes, including specifically identified institutional/charitable/government uses | Depends on permitted purposes | Allows changes/distribution within permitted purpose, with notices, patent terms and cure | Standardized restrictions and expressly permitted organization categories not expressly in AW-NC |
| **[Business Source License 1.1](https://mariadb.com/bsl11/)** | Non-production allowed; production may depend on Additional Use Grant | Depends on specific use grant | Work transitions to specified Change License at applicable Change Date (within four years for a release) | Automatic time-delayed change absent from AW-NC |
| **[Commons Clause v1.0](https://commonsclause.com/)** added to another license | Commercial internal operation generally permitted by the clause itself | Restricts defined **Sell** where value substantially derives from covered software; value-added applications may be permitted | Base license rights survive subject to sale limitation | Commercial restriction narrower than AW-NC internal-use prohibition, but it is an additional condition on a named base license |
| **[SSPL 1.0](https://www.mongodb.com/legal/licensing/server-side-public-license)** | Commercial running permitted subject to conditions | Section 13 may require source availability for all software enabling covered functionality offered as service | Strong service-related reciprocity rather than AW-NC permission model | Hosted service source obligations, not a simple noncommercial prohibition |
| **[Elastic License 2.0](https://www.elastic.co/licensing/elastic-license/)** | General internal company use permitted | Restricts third-party hosted/managed access to substantial functionality | Use/modify/distribute generally allowed with license-key and notice safeguards | Narrower managed-service restriction, broader business use |
| **[MIT](https://opensource.org/license/mit)** (OSI-approved comparison) | Permitted | Permitted | Permissive subject to notices | Genuine open source, unlike AW-NC and the restrictive source-available examples |

**Historical caution:** AFPL had multiple editions; identify the actual AFPL text attached to the installed software. [SPDX Aladdin](https://spdx.org/licenses/Aladdin.html) and [MIT Ghostscript archive](https://web.mit.edu/ghostscript/www/Public.htm) are not assertions that modern Ghostscript is presently under AFPL. **Commons Clause caution:** official [FAQ](https://commonsclause.com/) discusses value-added SaaS as potentially permitted; do not treat every commercial derivative as automatically prohibited.

## Preserving license boundaries

AW-NC §8 does **not** change MIT/Apache/GPL/AGPL/proprietary license rights where they are applicable. A new AW-owned module may be independently licensed AW-NC **only if legally separable/independently licensable and expressly designated by the rights holder**. A change to GPL/AGPL code cannot automatically be declared exclusively AW-NC. A legally combined work may trigger copyleft duties; the mere existence of several LICENSE files does not authorize an incompatible combination.

**SPDX:** `OR` represents a **genuine authorized alternative** for the same material; `AND` denotes jointly applicable requirements where correctly determined. Different component licenses within one project are not necessarily dual licensing. Record [LICENSE-MAP](../LICENSE-MAP.md), SPDX/SBOM and original licenses.

## Ten practical cases

| Situation | Analysis |
|---|---|
| Student studies AW-only source | Noncommercial grant can apply |
| Company operates revenue-generating AW-only CRM | AW commercial authorization needed |
| Company runs historical AFPL program internally | AFPL running unrestricted, other obligations still apply |
| Government/public-health user under PolyForm Noncommercial | Named organizational exception may apply, unlike automatic AW-NC treatment |
| BSL project used in production | Read project-specific Additional Use Grant and Change Date |
| Elastic ELv2 near-complete managed service | Hosted substantial functionality may be restricted |
| MIT library plus new original AW UI | MIT license/notices remain; AW UI may use AW-NC on authorized express designation |
| Modifications to GPL code | Derivative/copyleft duties remain, even if changes are new |
| AGPL server with integrated AW proprietary extension | Network/combined work analysis required; conflicting distribution not authorized |
| White-label software sold with third-party SDK | AW commercial grant cannot sublicense third-party SDK; third-party EULA remains |

## Evidence and policy

- [OSI Open Source Definition](https://opensource.org/osd): commercial-use freedom is necessary for OSI open-source designation.
- [GNU GPL FAQ](https://www.gnu.org/licenses/gpl-faq.html): combined works vs aggregation and GPL copyleft considerations; guidance is not a court ruling.
- [SPDX license expressions](https://github.com/spdx/using/blob/main/docs/license-id-in-source.md): multiple license expressions and legal provenance.
- [Wolter et al. (2022), DOI 10.1145/3571852](https://doi.org/10.1145/3571852): scholarly empirical investigation of GitHub license inconsistencies; motivates component-level inventory but does not establish legal compatibility.
- [Xu et al., LiDetector (2022 preprint)](https://arxiv.org/abs/2204.10502): study of license incompatibility tooling, not an AW-NC judicial opinion.
- [UU No. 28/2014 tentang Hak Cipta](https://peraturan.bpk.go.id/Details/38690/uu-no-28-tahun-2014) and [Islamic IIFA intellectual property resolution](https://iifa-aifi.org/en/54157.html): distinct statutory and religious normative authorities.

**Important:** Neither §8 nor this comparison promises AW-NC and GPL/AGPL can be combined commercially or distributed together without reviewing actual architecture, license texts, rights and activity.

Each practical case above is modeled in the [mixed-license fixtures](../fixtures/mixed-license) (expected decisions pending counsel review).
