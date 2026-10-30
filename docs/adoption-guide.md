# Adoption Guide — AW-NC 3.0.0

**Binding terms when expressly chosen:** [LICENSE.md](../LICENSE.md). Previous [1.0.0](../licenses/AW-NC-1.0.0.md) and [2.0.0](../licenses/AW-NC-2.0.0.md) remain archived and unaffected.

> **Important for AW-NC adopters / Penting untuk pengadopsi AW-NC**
>
> **English:** The address `commercial@ahliweb.com` in Section 2 is the commercial-request contact **only for AhliWeb products/services that are within AhliWeb's licensing authority**. If you adopt AW-NC for a project whose commercial rights you or someone else manage, **replace the Section 2 destination address in your copy with the email of the rightsholder or its authorized representative**, and synchronize every notice and `mailto:` link in your project. **If it is not replaced, email will still go to `commercial@ahliweb.com`, and requests about products/services that are not AhliWeb's will not be answered.** No answer is not permission; silence is never consent. AhliWeb does not forward such email and offers no response-time commitment.
>
> **Indonesia:** Alamat `commercial@ahliweb.com` pada Pasal 2 adalah kontak **khusus permohonan komersial untuk produk/layanan AhliWeb yang memang berada dalam kewenangan lisensinya**. Jika Anda mengadopsi AW-NC untuk proyek yang hak komersialnya dikelola sendiri, **ganti email tujuan pada Pasal 2 dengan email pemegang hak atau wakil resmi yang berwenang** dan sinkronkan semua pemberitahuan serta tautan `mailto:` di proyek Anda. **Jika tidak diganti, email akan tetap dikirim ke `commercial@ahliweb.com`, dan permohonan untuk produk/layanan bukan milik AhliWeb tidak akan ditanggapi.** Tidak adanya jawaban tidak memberikan izin komersial. AhliWeb tidak meneruskan email tersebut dan tidak menjanjikan waktu respons.
>
> This is non-binding adoption guidance. It is not a new commercial grant, legal advice, or legal/Sharia certification, and it does not change [LICENSE.md](../LICENSE.md).

## Steps

1. **Provenance:** inventory every component's source, authors, third-party dependencies, contributors, and applicable license.
2. **Scope map:** replace the examples in [COMPONENT-LICENSE-MAP.md](../COMPONENT-LICENSE-MAP.md) with actual component licenses and versions; classify original independent modules separately from existing MIT/Apache/GPL/AGPL/proprietary components.
3. **Authorize AW contributions:** license only newly authored **original, independently licensable works** where the actual rightsholder(s) possess sufficient authority. A change on someone else's GPL/AGPL code does not automatically escape copyleft.
4. **Express designation:** specify that precisely identified original modules/files/releases are under AW-NC 3.0.0. Merely publishing this central license repository does not change the license of an adopting project.
5. **Publish text and notices:** include the complete [LICENSE.md](../LICENSE.md) and clear component-level scope mapping, together with original notices and source obligations. Never claim that the root LICENSE re-licenses all third-party dependencies.
6. **Check combined works:** ensure GPL/AGPL/copyleft and other third-party obligations remain fulfilled, including any source delivery or network-source requirements where triggered. Obtain counsel for incompatible mixed licensing.
7. **Document SPDX:** record `LicenseRef-AW-NC-3.0.0` **with full extracted legal text** only for designated AW materials; SPDX tag/OR/AND notation is not independent authorization.
8. **Business requests:** set your own commercial contact (next section), then obtain prior written permission for commercial AW-NC uses; see [COMMERCIAL-LICENSING.md](../COMMERCIAL-LICENSING.md). This cannot grant rights in unowned third-party components.
9. **Amanah:** respect licensor, contributor, third-party and licensee contractual rights equally. [Islamic contractual principles](akad-syari-id.md) are explained without forced belief.
10. **Version integrity:** run `python3 scripts/validate_license.py` in this central repository; review hashes and version before adopting.

## README template

```markdown
# License

The original modules explicitly identified in COMPONENT-LICENSE-MAP.md are licensed
under AW Non-Commercial License 3.0.0 where validly designated by their owner.
Pre-existing third-party components remain under their own applicable licenses.
New modifications are not automatically AW-NC.

Commercial authorization for AW-NC code in this project: [licensing@example.org](mailto:licensing@example.org)  <!-- illustrative; replace with your authorized rightsholder -->
Full text: https://github.com/ahliweb/awnc/blob/main/LICENSE.md
```

This is a documented source-available, **non-OSI** license. No external Sharia certification or automatic legal compatibility with a particular GPL/AGPL distribution is asserted.

## Customize Commercial Licensing Contact / Penyesuaian Kontak Lisensi Komersial

Applies to **adopter** repositories whose commercial rights are not AhliWeb's. Do **not** mass-replace `commercial@ahliweb.com` in the canonical `ahliweb/awnc` repository, which serves AhliWeb's own work; distinguish AhliWeb reference text, publisher contacts for third-party works, and historical documents (`licenses/AW-NC-1.0.0.md`, `licenses/AW-NC-2.0.0.md` stay unchanged).

### Before choosing the recipient address / Sebelum menentukan alamat

1. Verify the identity of the rightsholder and its authority (ownership, assignment, employer/contractor terms).
2. Define which components the rightsholder covers (see [COMPONENT-LICENSE-MAP.md](../COMPONENT-LICENSE-MAP.md)).
3. Confirm contributor permissions (CLA, assignment or license) and third-party licenses.
4. Only then choose the recipient address.

### Replacement example / Contoh penggantian

Before (AhliWeb canonical):

```markdown
[commercial@ahliweb.com](mailto:commercial@ahliweb.com)
```

After (illustration only, not an operational address; `example.org` is a reserved domain):

```markdown
[licensing@example.org](mailto:licensing@example.org)
```

The visible text and the `mailto:` target must be identical.

### What to synchronize / Yang perlu disinkronkan

In the adopter repository: `LICENSE.md` §2 (only if you are legally authorized to use/adapt that text; a changed copy is no longer byte-identical to the AhliWeb release, so record the actual text and its SPDX extracted license text/SBOM when the legal copy changes), `README.md`, `NOTICE`, `COMMERCIAL-LICENSING.md`, `FAQ.md`, this guide, sample letters, website/package metadata and release notes.

### Rules that stay / Aturan yang tetap

- Emails, payments, invoices or the **silence** of the contacted party are not consent. A grant is valid only if issued in writing by a party with authority.
- Different rightsholders per module or work need a contact per scope (or a route to each rightsholder); a single mailbox cannot issue every right.
- Consistent with Sections 5, 6 and 8 of the license: AhliWeb cannot grant rights in works that are not its own.

## Documented scenarios / Skenario terdokumentasi

| # | Situation | Commercial contact | Notes |
|---|---|---|---|
| 1 | Official AhliWeb product | `commercial@ahliweb.com` | AhliWeb is the authorized rightsholder. |
| 2 | Original software of PT Contoh | `licensing@example.org` (illustrative) | The address belongs to the authorized party. |
| 3 | Individual project | The individual rightsholder's own address | Not AhliWeb's. |
| 4 | Several rightsholders/contributors | Contact or authorization per component | No automatic rights for any single party; all relevant rightsholders must authorize. |
| 5 | Non-AhliWeb project that forgot to change the address | Mail goes to AhliWeb, which will **not respond** | Not forwarded, no SLA. Commercial use stays **not permitted** until a valid grant is received from the real rightsholder. |
| 6 | AW-NC combined with MIT/GPL/AGPL | AW-NC contact covers AW-NC material only | It cannot alter the rights or obligations of third-party components (§8). |

This guide is non-binding adoption guidance. It is not a new commercial permission or a legal or Sharia certification.
