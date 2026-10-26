# Semantic Versioning Policy for the AW-NC Legal License

**Canonical version:** `3.0.0` ([VERSION](../VERSION)). Based on the [Semantic Versioning specification **2.0.0**](https://semver.org/spec/v2.0.0.html), adapted as a **labeling and release-management convention for license documents**. Semantic compatibility of software APIs does not determine the enforceability or compatibility of legal agreements.

## Classification

| Bump | When to use | Example |
|---|---|---|
| **MAJOR** | Changes to operative rights, restrictions, duties, licensing scope, termination, interpretation or legal covenants | `1.0.0 → 2.0.0` (Islamic covenant); `2.0.0 → 3.0.0` (third-party license preservation and new development scope) |
| **MINOR** | New **non-binding** guidance, research, examples, translations or adoption processes without change to operative legal grants | `3.0.0 → 3.1.0` if a compatible documentation release is intentionally published |
| **PATCH** | Correction of broken links, typos or metadata **only if** contract meaning is unchanged | `3.0.0 → 3.0.1` |
| **PRE-RELEASE** | Proposed legally operative changes still undergoing review | `4.0.0-rc.1`, prominently marked **draft** rather than a grant |

When an edit could reasonably alter scope or interpretation, err toward a MAJOR version and require an independent copyright lawyer's assessment. Do not reclassify a substantive legal modification as PATCH merely to reduce apparent migration burden.

## Preservation of existing grants

1. Published, previously adopted legal editions cannot be retroactively modified by changing a central GitHub repository. Software copyright holders must **expressly select** the edition for each identified software release or component.
2. [AW-NC 1.0.0](../licenses/AW-NC-1.0.0.md) stays byte-for-byte identical to the original historical LICENSE blob `207347b763b8dd8b7dcdcb3959c575c0fe4b1e25`.
3. [AW-NC 2.0.0](../licenses/AW-NC-2.0.0.md) stays byte-for-byte identical to original LICENSE blob `c0aae42e0dd6f2da4827cb49ef62623e87ed879c`.
4. [AW-NC 3.0.0](../LICENSE.md) uses §8 to protect other third-party licenses and scopes original enhancements expressly designated by an authorized holder. This does not erase copyright ownership, third-party licenses, GPL/AGPL copyleft or any already valid grants.
5. Track an actual [component license manifest](../COMPONENT-LICENSE-MAP.md) for every adopting project. Rights-holder selection, copyright ownership, SPDX extracted text and corresponding source obligations must be independently verifiable.

## Release procedure

1. Document the proposed change, legal impact and affected copies in a GitHub issue.
2. Obtain authorization from the appropriate copyright holders. For materially operative clauses, request competent IP counsel review. For the Islamic covenant, consult qualified fiqh muamalah scholars if making specific juristic claims. Publication alone is not external review or certification.
3. Archive the previous complete license **unaltered** and update [LICENSE.md](../LICENSE.md), [VERSION](../VERSION), [CHANGELOG](../CHANGELOG.md), README, FAQ, NOTICE, examples, evidence, and [release record](../releases/3.0.0.md).
4. Run `python3 scripts/validate_license.py` from repository root and attach its output and release SHA to the approval record. The script detects version/archive consistency, not license enforceability or derivative-work compatibility.
5. After approval/merge, create an annotated Git tag `v3.0.0` on the **verified** release commit and optionally publish a GitHub Release with approval status and checksums. A VERSION file does not create a Git tag.
6. Notify adopter repositories of optional prospective adoption; **do not bulk rewrite** old LICENSE files without legitimate copyright authority.
7. Keep complete signed commercial grants outside public GitHub when confidential, with version, scope and hash evidence.

Suggested manual commands **only after approved release and local verification**:

```bash
python3 scripts/validate_license.py
git tag -a v3.0.0 -m "AW Non-Commercial License 3.0.0"
git push origin v3.0.0
```

## Islamic accountability and civil interpretation

Section 5 expresses the licensor's solemn commitment before Allah Jalla wa 'Ala, while ordinary contractual restrictions, lawful civil remedies and equal rights apply regardless of a Licensee's religion. Section 8 additionally treats other authors' and contributors' rights as an amanah; it does not force a belief or invalidate pre-existing license grants.

**Review status:** publishing this document is not a legal opinion, Sharia certification, or proof that arbitrary GPL/AGPL combinations are licensable as AW-NC.
