# License Comparison and Decision Guide

> Informational comparison updated 2026-10-26. The current binding text when expressly adopted is AW Non-Commercial License 2.0.0 in [LICENSE.md](../LICENSE.md); the unaltered 1.0/1.0.0 text is archived at [licenses/AW-NC-1.0.0.md](../licenses/AW-NC-1.0.0.md). This document neither adds rights nor amends the license. Obtain legal advice for a concrete transaction.

## AW Non-Commercial License 2.0.0 versus Aladdin Free Public License (AFPL)

**Versions:** AW-NC 2.0.0 compared principally with Aladdin Free Public License v8 (18 November 1999); the substantially similar relevant provisions of AFPL v9 (18 September 2000) are cited below. Do not confuse the text with GPL or AGPL.

| Topic | AW-NC 2.0.0 | Aladdin AFPL v8/v9 |
|---|---|---|
| License classification | Custom source-available; not OSI open source | Source-available; expressly not OSI open source |
| Learning and non-commercial research | Granted subject to conditions | Copying and modifications allowed subject to conditions |
| Internal commercial operation | Prior written permission where it supports revenue-generating business operations/service delivery (AW-NC section 1) | Functional use (running) is expressly unrestricted (AFPL section 2(b)) |
| Paid hosted/SaaS product | Prior written commercial permission (AW-NC section 1) | Merely running the program is outside license restrictions; distribution or incorporation into paid deliverables requires separate analysis |
| Paid consultancy or implementation | Prior written commercial permission (AW-NC section 1) | Paid distribution by a commercial organization is restricted, including payments indirectly tied to distribution (AFPL section 2(a)); pure running alone differs |
| Non-commercial modification/distribution | Permitted while retaining copyright and permission notice (AW-NC section 4) | Permitted under detailed source, notices, and downstream licensing obligations (AFPL section 2(c)) |
| Obligation to publish derivative source | No blanket reciprocal/source-publication obligation expressly stated by AW-NC | Corresponding source required **when distributing a covered Work**, not automatically from private operation (AFPL section 2(c)(iv)) |
| Mandatory derivative licensing | No express whole-work copyleft provision; do not remove AW-NC obligations from copies of the covered Software | Distributed covered Work as a whole must be licensed at no charge to third parties under AFPL (AFPL section 2(c)(ii)) |
| Trademarks | AW-NC section 3 expressly reserves rights | Consult separate applicable trademark rights |
| Commercial permission path | Explicit written permission request: commercial@ahliweb.com | Separate rights require authorization from the relevant rightsholder(s) |
| SPDX identification | Custom local reference LicenseRef-AW-NC-1.0; NOT an official SPDX-list identifier | Archived SPDX list associates Aladdin with AFPL v8; do not automatically use that identifier for v9: ScanCode catalog uses LicenseRef-scancode-afpl-9.0 |

**Do not infer** that every use of AFPL is freely monetizable: its section 2(a) covers indirect consideration connected with distribution. Nor infer that a SaaS provider never distributes software: inspect client-side bundles, containers, plug-ins, copies delivered to customers, and the exact agreement.

### Worked scenarios (preliminary, not legal permission)

| Scenario | AW-NC 2.0.0 | AFPL |
|---|---|---|
| Student forks software for private study | Normally within non-commercial grant | Permitted subject to terms |
| Nonprofit publishes free educational modification | Generally permitted if genuinely non-commercial; attribution retained | Permitted with section 2(c) distribution obligations |
| Company deploys revenue-supporting internal CRM | Written commercial permission required | Functional running is not restricted |
| Paid SaaS hosts program without delivering copies | Written commercial permission required | Running itself is not restricted; verify any actual distribution |
| Freelancer hands software to a paying customer | Written commercial permission required | Commercial distribution for direct/indirect payment is restricted |
| Community distributes modified source for free | Generally permitted if non-commercial; notices retained | Allowed, but AFPL derivative and source/notices requirements apply |
| Paid white-label installation delivered to client | Written commercial permission required | Normally restricted under paid-distribution rule |
| Commercial company researches program without delivering copies | Intent and role must be assessed against AW-NC's commercial-purpose definition; permission is the safe path for business operations | Running unrestricted; modification/copying/distribution remain governed by AFPL |
| Developer publishes a free compiled derivative | Non-commercial only, with AW-NC notices | Source and relevant build scripts required by AFPL section 2(c) |
| Vendor bundles licensed code with GPL/AGPL dependencies | Must separately honor every third-party license; AW-NC cannot override them | Same principle |

### AW-NC versus other licenses

- **MIT:** OSI-approved permissive license allowing commercial use; substantially different from AW-NC.
- **GPL / AGPL:** OSI-approved reciprocal licenses that allow commercial activity but impose their own obligations. AGPL includes network-interaction source obligations in the circumstances its terms specify.
- **No license:** publishing code without an affirmative license generally does not grant general reuse/modification/distribution rights.
- **AW-NC:** best suited to a public-source learning/evaluation channel alongside individually negotiated commercial rights; not an OSI open-source license.

### Practical choice

Prefer AW-NC when the policy objective is controlled commercial exploitation, including internal business use and paid hosted services. Prefer AFPL-like distribution logic only when commercial running should remain unrestricted and distribution-based reciprocity is a deliberate objective. A hybrid or stronger copyleft rule needs a separately drafted and reviewed future AW license; do not imply these protections already exist in AW-NC 2.0.0.

### Source hierarchy

1. [AW-NC official LICENSE](../LICENSE.md), sections 1–4.
2. [AFPL v8 primary text in SPDX historical archive](https://spdx.org/licenses/archive/archived_ll_v2.2/Aladdin.html), sections 2(a)–(c).
3. [AFPL v9 historical text catalogued by ScanCode](https://scancode-licensedb.aboutcode.org/afpl-9.0.html), sections 2(a)–(c).
4. [Open Source Definition](https://opensource.org/osd), especially criteria 1 and 6.
5. [Official evidence and research inventory](evidence-and-references.md).

**Interpretation boundary:** This is a comparative explanation, not legal advice. The commercial characterization of a specific activity is fact dependent.


## New AW-NC 2.0.0 contractual and Sharia accountability clause

- The substantive non-commercial boundary in Section 1 remains as it was in 1.0.0; the operative Section 5 now expressly obliges good-faith, truthful conduct and affirms the **licensor's** solemn responsibility before Allah Jalla wa 'Ala according to Ahlus Sunnah wal Jama'ah. Muslim licensees may voluntarily understand fulfillment of this legal commitment as amanah before Allah.
- AFPL does not contain this particular religious clause. This does **not** establish that AFPL contracts lack moral/religious duties for Muslims under Islamic teachings.
- AW-NC Section 5 preserves legal equality of users of every faith, forbids compulsory creed/oath, and does not claim automatic Sharia certification.
- AW-NC Sections 6–7 require ordinary applicable legal enforcement and explicit version selection; old 1.0.0 copies are not automatically relicensed.
- See [Indonesian article interpretation](akad-syari-id.md) and [SemVer policy](semantic-versioning.md).
