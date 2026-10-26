# Evidence Register: Legal, Empirical, Standards and Islamic Jurisprudence

**Updated:** 2026-10-26 · **Status:** curated research bibliography, not certification or professional legal/fatwa opinion.

## Evidence discipline

Do not equate four different kinds of evidence: (1) binding legal/license text; (2) normative Islamic scripture and juristic institutional resolutions; (3) peer-reviewed empirical or theoretical research; and (4) voluntary technical standards. Empirical findings demonstrate observed risks or model incentives but do not prove a specific contract enforceable, Sharia-compliant, or economically successful.

| ID | Evidence type | Source | Verified finding / relevance | Limitation |
|---|---|---|---|---|
| L1 | Binding license text | [AW-NC LICENSE.md](../LICENSE.md), §§1–4 | Requires prior written permission for defined commercial purposes, including internal revenue-supporting business operations, SaaS and paid client services | Contract enforceability and scope require jurisdiction-specific legal analysis |
| L2 | Historical primary license | [AFPL v8 (SPDX archive)](https://spdx.org/licenses/archive/archived_ll_v2.2/Aladdin.html), §2(a)–(c) | Running expressly unrestricted; paid third-party distribution restricted; corresponding source and notices required for distributed derivative works | AFPL v8 must not be assumed identical to every release; compare actual source headers |
| L3 | License reference | [AFPL v9 (ScanCode)](https://scancode-licensedb.aboutcode.org/afpl-9.0.html) | Version date 18 September 2000; independently corroborates functional-use and distribution distinction | Catalog is a curated reproduction; actual application requires relevant work's license text |
| L4 | Policy authority | [OSI Open Source Definition](https://opensource.org/osd) | A license forbidding commercial fields of endeavor or commercial redistribution is not OSI-open-source | Policy classification is not a court's judgment |
| I1 | Islamic juristic institutional resolution | [International Islamic Fiqh Academy, Resolution 43 (5/5), 15 December 1988](https://iifa-aifi.org/en/54157.html) | Recognizes financial value of brands/creative works and Sharia protection of copyrights/patents | Normative juristic resolution, not empirical research or Indonesian statute |
| I2 | Indonesian Islamic institutional fatwa | [MUI Fatwa 1/MUNAS VII/MUI/5/2005, 28 July 2005 (official scan)](https://mui.or.id/storage/fatwa/537803ba9f7fdb09b3d6de005cf381df-lampiran.pdf), pp. 470–471 | Protectable intellectual property is a financial right; may be the object of mu'awadhah (commercial exchange) or tabarru' (non-commercial) agreements; unauthorized infringement described as injustice | Fatwa is a normative religious source, not automatically statutory law; it qualifies rights that are not contrary to Islamic law |
| I3 | Islamic scripture | Qur'an: Al-Ma'idah 5:1; An-Nisa 4:29, 4:58; Al-Anfal 8:27; Al-Baqarah 2:188, 2:282; Al-Isra 17:34; Az-Zalzalah 99:7–8 | Normative foundations for agreements, consent, amanah, protection of rights, documentation and accountability | Verse application requires sound tafsir and fiqh; 2:282 speaks directly to recorded debt transactions, not software licenses by name |
| ID1 | Indonesian statute | [UU No. 28 Tahun 2014 tentang Hak Cipta (official JDIH BPK)](https://peraturan.bpk.go.id/Details/38690/uu-no-28-tahun-2014) | Applicable national copyright framework, including protection of computer programs, economic rights and statutory limitations | Consult consolidated/current amendments and legal counsel; statute is distinct from a private license |
| P1 | Peer-reviewed empirical | Thomas Wolter, Ann Barcomb, Dirk Riehle, Nikolay Harutyunyan (2022), *Open Source License Inconsistencies on GitHub*, ACM TOSEM, [DOI 10.1145/3571852](https://doi.org/10.1145/3571852), [author institution summary](https://oss.cs.fau.de/2022/10/13/research-paper-open-source-license-inconsistencies-on-github/) | Sample of 1,000 GitHub repos; roughly half failed to fully declare licenses found in code; among incomplete declarations, ~10% were permissive/copyleft mismatches | Sample-specific, not a measured AW-NC infringement rate |
| P2 | Peer-reviewed empirical | Arunesh Mathur et al. (2012), *An Empirical Study of License Violations in Open Source Projects*, IEEE Software Engineering Workshop, [Microsoft Research record](https://www.microsoft.com/en-us/research/publication/empirical-study-license-violations-open-source-projects/) | Analyzed 1,423 projects and ~69 million nonblank LOC, identifying four validated violations in the analysis | Historical Google Code sample; does not estimate today's global violation prevalence |
| P3 | Peer-reviewed theoretical economics | Stefano Comino & Fabio M. Manenti (2011), *Dual licensing in open source software markets*, *Information Economics and Policy* 23(3–4), 234–242, [DOI 10.1016/j.infoecopol.2011.07.001](https://doi.org/10.1016/j.infoecopol.2011.07.001) | A model describes economic circumstances where dual-licensing can be sustainable and the role of license design | Model is not proof that AW-NC dual licensing will increase revenue |
| P4 | Peer-reviewed case-based research | Mikko Välimäki (2003), *Dual Licensing in Open Source Software Industry*, *Systèmes d'Information et Management* 8(1), 63–75, [journal record](https://aisel.aisnet.org/sim/vol8/iss1/4/) | Case studies of Sleepycat, MySQL and TrollTech illustrate legal/economic prerequisites | Historically bounded cases; those licenses differ from AW-NC |
| P5 | Peer-reviewed practical research | Juho Lindman et al. (2011), *Matching Open Source Software Licenses with Corresponding Business Models*, *IEEE Software* 28(4), 31–35, [DOI 10.1109/MS.2011.50](https://doi.org/10.1109/MS.2011.50) | Business-model choice and license selection should be aligned | Research concerns open-source license/business models; AW-NC is source-available, not OSS |
| S1 | International standard | [ISO/IEC 5230:2020 — OpenChain Specification](https://www.iso.org/standard/81039.html) | Benchmark for organizational open-source license compliance programs | It does not declare AW-NC OSI-approved or determine Sharia compliance |
| S2 | International standard | [ISO/IEC 5962:2021 — SPDX 2.2.1](https://www.iso.org/standard/81870.html) | Standardized software components and license metadata | Current standard revision status should be checked; a custom LicenseRef is not an SPDX license-list approval |

## Evidence-to-action traceability

| Engineering/control decision | Supporting evidence | Validation artifact |
|---|---|---|
| Inspect file-level and transitive dependency license claims, not only top-level LICENSE | P1, P2, S1 | Dependency SBOM, SPDX file-level annotations, exception log |
| Reserve business operations/SaaS permission in the public license | L1 | Legal review and explicit commercial license grant |
| Document signed commercial terms and scope | L1, I1, I2, ID1 | Signed agreement, version/hash, permission ledger |
| Adopt transparent, fair, mutually understood contracting | I2, I3 | Commercial rights matrix, consent record, dispute process |
| Offer distinct public/paid licensing with clear rights ownership | P3, P4, P5 | Contributor rights provenance and lawyer-reviewed commercial template |
| Avoid presenting guidance as newly enforceable conditions | L1, ID1 | Immutable 1.0 LICENSE, semantic future-version change control |

## What evidence does NOT show

- No study cited here proves that AW-NC prevents infringement or increases sales.
- A fatwa/resolution is a doctrinal authority, not empirical validation or a court ruling.
- ISO/IEC 27001, 27002, 27005, 27017, 27018, 27034, 27701, 22301, 20000-1 and 15408 may be relevant to security, privacy, continuity, service management or product assurance of deployments; **they are not software license compliance certifications**. Prioritize ISO/IEC 5230 and 5962 for license governance.
- A local SPDX token such as LicenseRef-AW-NC-1.0 needs its extracted text documented in SPDX metadata and is not an OSI/SPDX-list endorsement.

## Review cadence

Re-validate links, publication status, current Indonesian legislation, and license metadata at each future major license revision and annually. Escalate contested legal or fiqh determinations to qualified advisers.
