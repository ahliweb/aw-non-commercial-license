# Commercial Licensing Agreement Framework (non-binding checklist)

This is a preparation checklist, **not an executable grant of commercial rights, not a substitute for a signed contract, and not an amendment to [AW-NC 3.0.0](../LICENSE.md)**. No commercial use is authorized until the copyright holder grants prior written permission. See [COMMERCIAL-LICENSING.md](../COMMERCIAL-LICENSING.md).

## Parties, rights and commercial scope

Record in the proposed agreement:

1. **Parties / authority** — licensor legal identity, company registration, authorized signatories, licensee; verify all contributors' copyright grants and third-party code permissions.
2. **Identified Software** — repository, component, release/tag, exact commit SHA, included/excluded modules, source code vs binaries and documentation.
3. **Permitted activity** — named use cases: internal revenue-supporting use; customer-facing SaaS; managed hosting; paid implementation, integration, consulting/support; resale or white-label; distribution and sublicensing; affiliates and contractors.
4. **Boundaries** — named legal entities, customer segments, countries, number of deployments/tenants, users, API consumers and hosting providers where negotiated.
5. **Exclusivity and intellectual property** — default assumption should NOT imply transfer of copyright, trademark rights, exclusivity, or ownership of derivative work without express documented terms.
6. **Fees and consideration** — currency, amount, milestones, payment method, taxes/withholding, invoices, payment window and refunds. Minimize material uncertainty.
7. **Duration and termination** — commencement, expiry/renewal, material breach, opportunity to cure, treatment of backups and post-termination customer data.
8. **Attribution and marks** — notices, trademarks, whitelabel scope, marketing statements and permissions.
9. **Source, derivatives and contributions** — modifications, improvement license, CLA/DCO requirements where relevant; ensure real provenance and no conflicting third-party obligations.
10. **Security, privacy and continuity** — warranties (if any), privacy/data protection responsibilities, disclosures, incidents, audit logs, backup/export/exit terms; these are independent of copyright permission.
11. **Disputes** — applicable law, forum, consultation/mediation, notices, authorized communications; do not assume a choice-of-law clause will always be enforceable.
12. **Acceptance and auditability** — signatures, attached license version, agreed schedule, change control, immutable evidence and retrieval/access limits.

## Islamic contractual ethics (supplementary, not religious coercion)

For parties voluntarily pursuing Sharia-aligned arrangements, request independent qualified fiqh review of:

- **al-wafa' bil-'uqud / al-'ahd:** honor agreed and lawful conditions (Qur'an 5:1; 17:34).
- **al-taradi / sidq:** informed mutual consent and truthfulness (4:29).
- **amanah / 'adl:** entrusted rights and fair dispute resolution (4:58; 8:27).
- **ma'qud 'alaih:** clearly identify the licensed property and permitted benefits; MUI 2005 explicitly recognizes intellectual property as an object of mu'awadhah and tabarru' contracts.
- **'iwad / uncertainty:** specify charges and deliverables to prevent material ambiguity, misleading claims or unjust enrichment.
- **tabarru' vs commercial mu'awadhah:** do not disguise a paid commercial arrangement as charitable, educational or noncommercial use.
- **islah / restitution:** document a fair breach-resolution process, accounting and corrective action; distinguish civil remedies from individual religious judgment.

**Do not** claim Sharia certification, an official fatwa approving AW-NC, or that all disputed forms of intangible rights are unanimously treated identically by scholars. Preserve equal legal clarity for Muslim and non-Muslim counterparties. Qur'anic and juristic support is explained in [Islamic contractual ethics](islamic-contractual-ethics.md) and [evidence register](evidence-and-references.md).

## Suggested permission ledger (internal only)

| Field | Required evidence |
|---|---|
| grant_id | Unique approval identifier |
| software_ref | Repo and exact license/version/commit |
| rights_holder | Verified rightsholder(s) |
| licensee | Registered organization and approved affiliates |
| allowed_uses | Explicit SaaS, internal, support, resale, distribution etc. |
| exclusions | Restricted fields, code and branding |
| start/end | ISO-8601 timestamps and renewal |
| contract_ref | Signed immutable document and hash |
| third_party_review | SBOM/license exceptions |
| review_owner | Approver and reassessment date |

Access-control and privacy controls apply to ledger fields containing personal or confidential information.

## Five sample transactions to negotiate explicitly

1. A customer installs AW-powered CRM solely inside its revenue-generating company.
2. A partner hosts multi-tenant AW-powered subscription services for several clients.
3. A freelance developer modifies AW code as a paid implementation project.
4. A reseller distributes a white-label build with separate brand privileges.
5. An educational institution conducts free research but plans a later paid commercialization phase.

Each case needs its own written scope; neither a purchase invoice nor repository visibility is automatically the required license grant.

## AW-NC 3.0.0 legal applicability and amanah

If parties expressly select AW-NC 3.0.0, [Section 5](../LICENSE.md) is an operative license clause concerning reciprocal good-faith conduct and the licensor's solemn Islamic commitment. This checklist does not itself add conditions. Ensure the executed commercial agreement distinguishes legally enforceable duties from religiously motivated ethical declarations; do not compel creed or faith, and preserve existing third-party rights and lawful civil forums.

Old agreements, previously published AW-NC 1.0.0 code and contributions remain subject to their own applicable grants, absent valid changes by authorized parties.


## Third-party rights schedule

Specify exactly which AW-owned original enhancements are covered by a commercial grant; maintain a separate third-party materials appendix under [COMPONENT-LICENSE-MAP.md](../COMPONENT-LICENSE-MAP.md). Do not claim rights over third-party code, contributions, MIT/Apache notices, GPL/AGPL source obligations, or licensed SDKs. An AW commercial payment cannot cure a conflicting copyleft obligation.
