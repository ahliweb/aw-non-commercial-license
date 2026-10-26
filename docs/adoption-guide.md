# Adoption Guide — AW-NC 3.0.0

**Binding terms when expressly chosen:** [LICENSE.md](../LICENSE.md). Previous [1.0.0](../licenses/AW-NC-1.0.0.md) and [2.0.0](../licenses/AW-NC-2.0.0.md) remain archived and unaffected.

## Steps

1. **Provenance:** inventory every component's source, authors, third-party dependencies, contributors, and applicable license.
2. **Scope map:** replace the examples in [LICENSE-MAP.md](../LICENSE-MAP.md) with actual component licenses and versions; classify original independent modules separately from existing MIT/Apache/GPL/AGPL/proprietary components.
3. **Authorize AW contributions:** license only newly authored **original, independently licensable works** where the actual rightsholder(s) possess sufficient authority. A change on someone else's GPL/AGPL code does not automatically escape copyleft.
4. **Express designation:** specify that precisely identified original modules/files/releases are under AW-NC 3.0.0. Merely publishing this central license repository does not change the license of an adopting project.
5. **Publish text and notices:** include the complete [LICENSE.md](../LICENSE.md) and clear component-level scope mapping, together with original notices and source obligations. Never claim that the root LICENSE re-licenses all third-party dependencies.
6. **Check combined works:** ensure GPL/AGPL/copyleft and other third-party obligations remain fulfilled, including any source delivery or network-source requirements where triggered. Obtain counsel for incompatible mixed licensing.
7. **Document SPDX:** record `LicenseRef-AW-NC-3.0.0` **with full extracted legal text** only for designated AW materials; SPDX tag/OR/AND notation is not independent authorization.
8. **Business requests:** obtain prior written permission for commercial AW-NC uses through [COMMERCIAL-LICENSING.md](../COMMERCIAL-LICENSING.md). This cannot grant rights in unowned third-party components.
9. **Amanah:** respect licensor, contributor, third-party and licensee contractual rights equally. [Islamic contractual principles](akad-syari-id.md) are explained without forced belief.
10. **Version integrity:** run `python3 scripts/validate_license.py` in this central repository; review hashes and version before adopting.

## README template

```markdown
# License

The original modules explicitly identified in LICENSE-MAP.md are licensed
under AW Non-Commercial License 3.0.0 where validly designated by their owner.
Pre-existing third-party components remain under their own applicable licenses.
New modifications are not automatically AW-NC.

Commercial authorization for AW-NC code: commercial@ahliweb.com
Full text: https://github.com/ahliweb/awnc/blob/main/LICENSE.md
```

This is a documented source-available, **non-OSI** license. No external Sharia certification or automatic legal compatibility with a particular GPL/AGPL distribution is asserted.
