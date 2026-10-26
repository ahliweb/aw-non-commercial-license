# License Compliance and Version Governance

**Status:** operational guidance; not an amendment to AW-NC 1.0.

## Controls based on ISO/IEC 5230 and SPDX ISO/IEC 5962

1. **Inventory:** identify direct/transitive software dependencies, bundled assets, snippets, AI-generated or imported contributions, and their file-level notices. Do not assume a root LICENSE governs all included components.
2. **Record:** create an SPDX-compatible SBOM with package/component names, versions, hashes, license declarations and observed licenses, copyright holders and links to original sources. For AW-NC document extracted license text with local LicenseRef-AW-NC-1.0; do not label it as an officially listed SPDX license.
3. **Review:** have a designated license officer validate MIT/Apache/GPL/AGPL/AFPL/other obligations, conflicts, exceptions, and source disclosure requirements before release.
4. **Approve:** maintain signed grants for SaaS, internal commercial operations, customer work, white-label/redistribution and sublicensing as permitted. Record decision, approver, effective interval and version.
5. **Contributions:** verify copyright ownership and contributor authorization; publishing an AW-NC work does not automatically allow unilateral commercial re-licensing of third-party contributions.
6. **Release gate:** block releases with unknown or incompatible license obligations, unapproved commercial usage, missing notices, unresolved rights ownership, or unverified attribution.
7. **Evidence retention:** save SBOM, notice bundles, grant register, signed approvals, release SHA, policy decision, and remedial actions in access-controlled storage.

## Risk register

| Risk | Impact | Mitigation / verification |
|---|---|---|
| Undeclared transitive AGPL/GPL or incompatible dependency | High | Dependency tree + file-level SPDX audit and qualified legal review |
| Commercial use without explicit grant | High | Prior written authorization and permissions registry |
| Contributor lacks re-licensing rights | High | Provenance attestations and contributor approval |
| User misunderstands non-commercial boundary | High | Clear FAQ and scenario examples, no false blanket assurances |
| User thinks Sharia statement is part of binding LICENSE | Medium | Label explanatory document expressly non-binding |
| Claimed Sharia or ISO certification without independent assessment | High | Avoid certification claims and require independent assessments |
| Mismatched version/SBOM identifier | Medium | Release tags/SHAs, stored extracted license text, review |
| Overseas enforcement assumptions | High | Local counsel and jurisdiction-specific contract schedule |

## Future license edition: proposed only

Consider a **reviewed AW-NC 1.1 or 2.0** with a formal change proposal before altering legally operative terms. Recommended candidate clauses, subject to lawyer/fiqh examination:

- Precise definitions: software, derivative work, internal commercial use, hosted service/SaaS, trial, PoC, indirect revenue, redistribution and sublicensing.
- Express evaluation/trial permission and whether corporate non-production testing is allowed.
- Rights and restrictions for white-label, reseller, marketplace, bundled services, API access and hosted operations.
- Termination, cure, reinstatement, survival, notices and dispute handling.
- Rights in derivative works, attribution, available code and trade names.
- Choice of law, severability, liability, third-party dependencies and contribution provenance.
- Plain-language cross-cultural ethical note separate from binding legal obligations.

**Migration rule:** Existing 1.0 grants do not change retroactively merely because explanatory documentation changes. Publish a new complete license version, release notes, change comparison, rights-holder approval and transition policy when adopted. A new license may require authorization from other copyright holders for their parts.

## Engineering acceptance checklist

- [ ] Official LICENSE.md content unchanged by documentation-only edits.
- [ ] Comparison cites exact AFPL v8/v9 sections and distinguishes running from paid distribution.
- [ ] README clearly marks source-available/non-OSI.
- [ ] Islamic ethics explicitly states independent supplementary nature.
- [ ] Each scientific claim links to identifiable paper/DOI and reports sample limits.
- [ ] National legal and fiqh institutional citations are dated and attributable.
- [ ] Commercial permission path never suggests silence or fee alone equals authorization.
- [ ] Relevant docs are linked, reviewed, and included in release notes.

**Related standards:** ISO/IEC 27001/27002, 27005, 27017, 27018, 27034, 27701, 22301, 20000-1, and 15408 can inform security, privacy, continuity, service quality, and product-assurance programs; they do **not** replace software license due diligence and are not claims of compliance here.

See [evidence register](evidence-and-references.md) and [commercial agreement framework](commercial-license-agreement-framework.md).
