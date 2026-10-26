# SBOM, Provenance and Automated Checks

Guidance for adopters and maintainers of AW-NC 3.0.0. Aligned with [ISO/IEC 5230](https://www.iso.org/standard/81039.html) (OpenChain) and [ISO/IEC 5962](https://www.iso.org/standard/81870.html) (SPDX). Automated checks here detect **structural** problems only; they do **not** prove legal compatibility, enforceability or Sharia compliance.

## Local-first checks

Run from the repository root (no dependencies beyond Python 3):

```sh
scripts/check_all.sh
```

| Script | Detects |
|---|---|
| [validate_license.py](../scripts/validate_license.py) | VERSION/CHANGELOG/clause consistency; immutable 1.0.0 and 2.0.0 archives |
| [check_baseline.py](../scripts/check_baseline.py) | Any change to `LICENSE.md` or archives versus [license-baseline.txt](../scripts/license-baseline.txt) |
| [generate_sbom.py](../scripts/generate_sbom.py) `--check` | Stale `sbom/awnc.spdx.json`; any third-party Python import or unreviewed CI action |
| [check_links.py](../scripts/check_links.py) | Broken relative Markdown links and anchors |
| [check_fixtures.py](../scripts/check_fixtures.py) | Fixture structure, missing extracted license text, copyleft + AW-NC coexistence not flagged for counsel |

The [GitHub workflow](../.github/workflows/checks.yml) runs the same script on pull requests (one short job, read-only permissions).

### Approved change to a canonical license text

1. Open an issue; obtain authorized rightsholder approval and, for operative clauses, counsel review.
2. Bump VERSION per the [SemVer policy](semantic-versioning.md); archive the previous text unaltered.
3. Update `scripts/license-baseline.txt` in the **same** reviewed pull request and state the approver in the PR.

## Custom license in an SPDX SBOM

AW-NC is **not** on the SPDX License List. Use a custom `LicenseRef-` identifier and embed the full text:

```json
{
  "licenseDeclared": "LicenseRef-AW-NC-3.0.0",
  "hasExtractedLicensingInfos": [
    {"licenseId": "LicenseRef-AW-NC-3.0.0", "name": "AW-NC-3.0.0",
     "extractedText": "<full text of LICENSE.md>"}
  ]
}
```

Never label it SPDX-approved. Fixtures use a placeholder text; real SBOMs must embed the complete text.

## File-level provenance for adopter repositories

For every file or component record: source URL and version/SHA, copyright holders, original license and text, modification history, authorship or contributor grant (CLA/DCO), AW-NC designation by an authorized holder, linkage/combination analysis, and approver/date. Use [COMPONENT-LICENSE-MAP.md](../COMPONENT-LICENSE-MAP.md) as the schema and `SPDX-License-Identifier` headers per [the example header](../examples/example-project-license-header.txt). Keep signed commercial grants private.

## Fixtures

Eight scenarios in [fixtures/mixed-license](../fixtures/mixed-license): permissive + original, modified GPL-3.0, modified AGPL-3.0 network service, GPL aggregation, proprietary SDK, unverified contributions, `OR` vs `AND`, and coexisting historic editions. Each has a project tree, SPDX 2.3 SBOM, notices, copyright chain and an expected decision. **Decisions are working hypotheses; independent IP counsel (including Indonesian and cross-border review) has not yet reviewed them.** The repository's own examples serve as the demonstration adopter tree for link and header checks.

## Exceptions and remediation

An exception (for example a failing link to a withdrawn source) needs an issue naming the check, reason, owner and expiry; it is closed by fixing the source or removing the claim. A `block` decision is never overridden by a script: remediate (remove, replace, obtain written rights) and re-review. Review links and cited law routinely before each release.

## Sharia amanah versus enforceability

Honoring others' rights is an ethical and contractual commitment under [Section 5](../LICENSE.md); whether any term is legally enforceable is decided by applicable law (for Indonesia, e.g. [UU 28/2014](https://peraturan.bpk.go.id/Details/38690/uu-no-28-tahun-2014)) and courts. See [islamic-contractual-ethics.md](islamic-contractual-ethics.md). No fiqh certification is claimed.

## References

- Wolter et al. (2022), [DOI 10.1145/3571852](https://doi.org/10.1145/3571852)
- [GNU GPL FAQ](https://www.gnu.org/licenses/gpl-faq.html), [SPDX license expressions](https://github.com/spdx/using/blob/main/docs/license-id-in-source.md)
