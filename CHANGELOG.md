# Changelog

Version numbers follow [the repository-specific SemVer policy](docs/semantic-versioning.md). Legal texts are preserved with explicit prospective applicability.

## [Unreleased]

### Changed
- Renamed `LICENSE-MAP.md` to `COMPONENT-LICENSE-MAP.md` so GitHub detects only `LICENSE.md` as the repository license (no longer "licenses found"). Content unchanged; `LICENSE.md` and `VERSION` unchanged.

### Released
- Annotated tags `v2.0.0` and `v3.0.0` and GitHub Releases published; release records updated.

### Added (non-binding tooling and guidance; no change to the license text)
- `scripts/check_links.py`, `scripts/check_baseline.py`, `scripts/check_fixtures.py`, `scripts/check_all.sh` and a lightweight `checks.yml` workflow.
- Eight mixed-license fixtures with SPDX 2.3 SBOMs and expected review decisions (pending counsel review).
- `scripts/generate_sbom.py` (file-level SPDX 2.3 SBOM `sbom/awnc.spdx.json`, dependency scan: no third-party Python packages; one CI action, MIT), `scripts/release_tags.sh`.
- [Desk verification of Indonesian law and Sunni sources](docs/legal-sharia-verification.md) (not a legal opinion or fatwa; findings F1–F5 open).
- [SBOM and provenance guidance](docs/sbom-and-provenance.md). `VERSION` stays 3.0.0 because `LICENSE.md` is unchanged.

## [3.0.0] - 2026-10-26

### Changed — MAJOR legal-scope release
- Added operative Section 8: pre-existing licenses remain valid within their actual scope; AW-NC does not override them.
- New original development may be AW-NC **only if** independently licensable, owned/authorized, and expressly designated.
- Original GPL/AGPL/copyleft obligations remain in force for covered modifications/combined works; incompatible distribution is not authorized.
- Archived original AW-NC 2.0.0 byte-for-byte alongside 1.0.0.
- Added license mapping template, seven similar license comparisons, FAQ examples, and release integrity rules.
- Section 5 Islamic covenant and ordinary civil law safeguards retained.

### Migration
No prior 1.0.0 or 2.0.0 grant is changed retroactively. Products select 3.0.0 expressly through authorized copyright owners; third-party rights remain independent.

## [2.0.0] - 2026-10-26

### Changed (MAJOR: new operative contractual covenant)
- Canonical `LICENSE.md` now contains Section 5: mutual undertaking of good faith, truthfulness and honoring rights; solemn affirmation of the licensor's commitment before Allah Jalla wa 'Ala; equitable rights without religious coercion.
- Section 6 preserves applicable legal interpretation, statutory exceptions and third-party rights, without claiming religious penalties or Sharia certification.
- Section 7 makes version selection and non-retroactivity explicit: rights holders must expressly identify the edition applied to their software.
- The original 1.0 text is archived **byte-for-byte** in `licenses/AW-NC-1.0.0.md`.
- `VERSION`, examples, FAQs and adoption guidance now use the SemVer form and describe the new covenant.
- Added a local release validator and a versioned release policy.

### Migration
- This publication **does not** retroactively change licenses of earlier software releases, and is not an automatic change to independently licensed repositories.
- New adoption requires rightsholder authorization and clear version identification.
- Legal enforceability and specific fiqh questions still warrant independent expert review (see issue #2).

## [1.0.0] - 2026-03-23

### Added
- Initial release of AW Non-Commercial License 1.0
- README
- FAQ
- Commercial licensing guide
- Supporting documentation
