# Adoption Guide — AW Non-Commercial License 2.0.0

The canonical [LICENSE.md](../LICENSE.md) is version **2.0.0**. [Historical v1.0.0](../licenses/AW-NC-1.0.0.md) remains available and must not be overwritten or automatically upgraded.

## Adoption steps

1. Verify your organization is an authorized copyright holder for all code to be covered, including contributors and bundled third-party components.
2. Explicitly decide to license **your project or specific release** under `AW Non-Commercial License 2.0.0`. Updating this central repository alone does not relicense your existing releases.
3. Copy the complete official [LICENSE.md](../LICENSE.md) *verbatim* into your repository as `LICENSE.md` or `LICENSE`; do not remove Section 5 or other provisions and still claim the unmodified official license name.
4. Add the precise version and URL to your README and, if you create an SPDX SBOM, include `LicenseRef-AW-NC-2.0.0` **with extracted license text**. This is NOT an official SPDX-listed identifier.
5. Preserve copyright and notices on redistributed copies, and record the source commit and hash of the selected license text.
6. Explain the practical meaning of Section 5 with [Indonesian explanation](akad-syari-id.md) and [Islamic ethics guide](islamic-contractual-ethics.md), without religious coercion or Sharia-certification claims.
7. For business operations, SaaS, reseller or paid work, obtain prior written consent from relevant copyright holders. See [Commercial Licensing](../COMMERCIAL-LICENSING.md).
8. Run `python3 scripts/validate_license.py` in the central license repository to verify version and historical archive consistency.

## Suggested project README snippet

```markdown
This project/release is licensed under **AW Non-Commercial License 2.0.0**.
Non-commercial use is permitted subject to its conditions; commercial use requires prior written authorization.
The license contains a mutual commitment to honest performance and the licensor's
Islamic ethical accountability declaration without requiring any Licensee's religious profession.
Full license: https://github.com/ahliweb/aw-non-commercial-license/blob/main/LICENSE.md
Commercial inquiries: commercial@ahliweb.com
```

## Selection remains explicit

Existing users of AW-NC 1.0.0 retain the scope of grants applicable to the earlier Software version/copies under the original terms, subject to applicable law and independently executed agreements. Version 2.0.0 applies prospectively only where designated by an authorized rightsholder.
