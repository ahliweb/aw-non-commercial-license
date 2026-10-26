# Semantic Versioning and Release Control for Legal Licenses

**Current canonical revision:** `3.0.0` in [VERSION](../VERSION) and [LICENSE.md](../LICENSE.md). **SemVer is a version-label policy**, not an assertion that contract rights are software APIs. See [SemVer 3.0.0 Specification](https://semver.org/spec/v3.0.0.html).

## MAJOR.MINOR.PATCH decision rule

| Change | Example | Rule |
|---|---|---|
| MAJOR | Add an operative legal covenant (Sharia-based Section 5), new restrictions, material rights, termination/interpretation clauses | Increase MAJOR: `1.0.0 → 3.0.0` |
| MINOR | New supplementary comparative analysis, non-binding translation, contract template checklist, adoption examples | Increase MINOR if publishing a repository release exclusively for documented compatible additions |
| PATCH | Broken link, editorial typo, citation formatting that cannot change interpretation | Increase PATCH if releasing a new repository edition |
| PRERELEASE | Proposed and not yet adopted legal text | Use `X.Y.Z-rc.N`; mark visibly draft and not yet canonical |
| BUILD | Content attestation / commit for an internal artifact | Optional `+metadata`; does not replace commit or file hash |

**Important nuance:** Even an apparent wording/typography correction could change a contract's interpretation. If reasonable readers or reviewers see a potential change to operative rights, classify **MAJOR**, not PATCH. Legal rights do not automatically upgrade when dependency or software versions change.

## Applicability and immutable history

1. Archive complete official license text in `licenses/AW-NC-X.Y.Z.md` whenever an edition is superseded.
2. NEVER overwrite historical license texts. The archived [AW-NC 1.0.0](../licenses/AW-NC-1.0.0.md) is byte-for-byte identical to the prior `LICENSE.md`; its original Git blob SHA is `207347b763b8dd8b7dcdcb3959c575c0fe4b1e25`.
3. Identify the applicable version in **each adopter software repository/release**; the central canonical text's latest version is not automatically imposed on old copies.
4. Keep commercial grants, third-party copyright and contributor permissions intact; no unilateral re-licensing of rights the licensor does not own.
5. Record the signed grant's version, content hash, applicable project/release/commit, issue of rights and effective date.

## Release procedure

1. Open a new legal-change issue; document reasons, risk, comparison and class (MAJOR/MINOR/PATCH).
2. For MAJOR legal changes, obtain approval by the relevant authorized rightsholder(s) and request IP lawyer + qualified fiqh muamalah review for Sharia language. Such a review is **not** implied by publication.
3. Update `LICENSE.md` for a legally operative release, `VERSION`, `CHANGELOG.md`, `README.md`, `NOTICE`, FAQ, adoption examples and translations. Archive prior text.
4. Run locally: `python3 scripts/validate_license.py` (no third-party dependency); inspect full diff and compare the archive's SHA with earlier published content.
5. After approved merge, create a **Git tag** `vX.Y.Z` pointing to the release commit, and optionally a GitHub Release with release notes, archival text hash and legal review status. A git tag is recommended but **not created by the validation script**.
6. Update SPDX/SBOM extracted-license identifiers to the selected license version. Do not use `LicenseRef-AW-NC-3.0.0` without including the full extracted license text.
7. Notify relevant adopting projects of optional future version adoption; never automatically migrate existing grants.

Suggested commands after appropriate approval:

```bash
python3 scripts/validate_license.py
git tag -a v3.0.0 -m "AW Non-Commercial License 3.0.0"
git push origin v3.0.0
```

Version publication, committing, tagging and legal approval are distinct actions. Review repository branches/tags to confirm each happened; never assume a tag exists solely because VERSION is updated.

## Islamic covenant and civil enforcement

Section 5 identifies the licensor's solemn accountability before Allah Jalla wa 'Ala as part of the **licensor's Islamic ethical undertaking** and includes mutual good-faith conduct obligations for all Licensees. The declaration does not make Allah a juridical party to a civil copyright contract, establish new religious sanctions or require creed from non-Muslims. Section 6 subjects enforcement to applicable law. [MUI Fatwa 1/2005](https://mui.or.id/baca/fatwa/perlindungan-haki-hak-kekayaan-intelektual) and [IIFA Resolution 43 (5/5)](https://iifa-aifi.org/en/54157.html) inform the religious ethics; neither specifically certifies the AW-NC text.

## Version acceptance gate

- [ ] Complete, coherent operative text; rights and limitations clearly distinguished.
- [ ] Reproducible archive of old legally operative license.
- [ ] Changelog, VERSION, README, NOTICE and examples aligned.
- [ ] Distinct legal, religious, and empirically researched claims.
- [ ] Rights-holder and contributor consent assessed.
- [ ] No retroactive terms or forced religious declaration.
- [ ] Independent legal/fiqh review status truthfully reported.
- [ ] Tested local validator succeeds; version tags only made after release approval.

## 3.0.0 legal-scope change

New Section 8 materially changes operative wording, so classify as MAJOR. The preceding edition [2.0.0](../licenses/AW-NC-2.0.0.md) is preserved byte-for-byte (original Git blob `c0aae42e0dd6f2da4827cb49ef62623e87ed879c`), as is [1.0.0](../licenses/AW-NC-1.0.0.md) (Git blob `207347b763b8dd8b7dcdcb3959c575c0fe4b1e25`). Do not assume `v3.0.0` git tag or GitHub Release exists until created following the authorized release gates.
