# Desk Verification: Indonesian Law and Ahlus Sunnah wal Jama'ah Sources (2026-10-26)

**Status: documentary source check, NOT a legal opinion, fatwa or certification.** It was performed by an AI-assisted review of primary texts. It does **not** replace (a) an Indonesian advokat/konsultan HKI, or (b) a qualified muamalah scholar/institution (for example MUI's Dewan Syariah Nasional, Majelis Tarjih, or LBM NU). Those reviews remain open in [issues #2 and #8](https://github.com/ahliweb/awnc/issues).

Ringkasan (ID): teks lisensi dicocokkan dengan UU 28/2014 dan Fatwa MUI 1/MUNAS VII/2005. Tidak ditemukan pertentangan nyata pada sumber yang diperiksa, tetapi ada empat celah yang perlu ditinjau konsultan (lihat "Findings"). Tidak ada sertifikasi hukum atau syariah.

## A. Indonesian law (primary sources)

| # | Provision | Verified content | Source and method | AW-NC 3.0.0 check |
|---|---|---|---|---|
| 1 | UU 28/2014 Art. 40(1)(s) | Computer programs are protected works | [JDIH BPK](https://peraturan.bpk.go.id/Details/38690/uu-no-28-tahun-2014) (official; blocked to automated fetch), [pasal.id](https://pasal.id/peraturan/uu/uu-no-28-tahun-2014/pasal-40) (secondary; text garbled) | Software is within scope; confirm wording on the official PDF |
| 2 | Art. 80(1) | Unless agreed otherwise, the holder may license by **written agreement** | [pasal.id Art. 80](https://pasal.id/peraturan/uu/uu-no-28-tahun-2014/pasal-80) (secondary, OCR errors) | Public license text accepted by conduct: whether it satisfies "written agreement" needs counsel |
| 3 | Art. 80(2) | License runs for a **definite term**, not beyond the copyright term | same | **Gap:** LICENSE.md states no term |
| 4 | Art. 80(3)-(5) | Royalty is due unless agreed otherwise; amount per custom and fairness (keadilan) | same | Non-commercial use is free by agreement (permitted by "kecuali diperjanjikan lain"); commercial fees are by separate grant, to be fair and transparent per [framework](commercial-license-agreement-framework.md) |
| 5 | Art. 82 | Licenses must not harm Indonesia's economy, contradict statutes, or strip the creator of all rights | [pasal.id Art. 82](https://pasal.id/peraturan/uu/uu-no-28-tahun-2014/pasal-82) (secondary) | Non-exclusive grant; creator keeps rights; §6 preserves statutory exceptions. No conflict found |
| 6 | Art. 83; PP 36/2018 | A license not recorded with the Minister has no legal effect against third parties | [pasal.id Art. 83](https://pasal.id/peraturan/uu/uu-no-28-tahun-2014/pasal-83); [PP 36/2018](https://peraturan.go.id/files/pp36-2018bt.pdf) | AW-NC is not recorded; effect against third parties is limited (see F3) |

Article text from pasal.id is a secondary transcription and must be compared with the official BPK/Kemenkum text before any citation in a legal document.

## B. Islamic sources (Ahlus Sunnah wal Jama'ah)

Method: the classical Sunni principle that the default in *mu'amalat* is permissibility unless a clear prohibition exists, with the conditions of a contract binding unless they make the lawful unlawful or the unlawful lawful. Institutional, not individual, authorities are cited.

| # | Source | Verified content | AW-NC check |
|---|---|---|---|
| 1 | [QS. Al-Ma'idah 5:1](https://quran.com/5/1) | Fulfil contracts | §5 reciprocal good faith consistent |
| 2 | [QS. An-Nisa 4:29](https://quran.com/4/29) | No consuming property wrongfully; trade by mutual consent | Fees only by written, informed consent; no coercion (§5) |
| 3 | Hadith "al-muslimuna 'ala shurutihim illa shartan harrama halalan aw ahalla haraman" (Sunan at-Tirmidhi 1352; graded hasan sahih by at-Tirmidhi, per [secondary note](https://hadithanswers.com/a-narration-regarding-conditions-in-trade/)) | Conditions bind unless they contradict the Sharia | Terms must not require anything unlawful. Takhrij beyond at-Tirmidhi's grading was **not** independently verified; Abu Dawud 3594 could not be confirmed here and is not cited |
| 4 | [Fatwa MUI No. 1/MUNAS VII/MUI/5/2005, 28 July 2005](https://mui.or.id/storage/fatwa/537803ba9f7fdb09b3d6de005cf381df-lampiran.pdf), "Kedua: Ketentuan Hukum", read from the official PDF | (1) HKI is a *huquq maliyyah* protected like property; (2) protected only if not contrary to Islamic law; (4) unauthorised use, copying or piracy of another's HKI is *kezaliman* and *haram* | Supports licensing, honouring rights and the Section 8 rule against overriding others' licenses. The fatwa's item (3) on mu'awadhah/tabarru' agreements is garbled in text extraction and is relied on only through the existing register entry I2 |
| 5 | [IIFA Resolution 43 (5/5)](https://iifa-aifi.org/en/54157.html) | Recognises financial value and protection of copyrights/trademarks | Same direction as 4 |

Not claimed: any ruling that §5 (a solemn undertaking before Allah) is a valid *yamin*/contractual term, or on the permissibility of the commercial-fee structure. Those need a qualified scholar.

## C. Findings (for counsel and scholars)

1. **F1 Term (Art. 80(2)).** LICENSE.md states no term or termination. Counsel should advise whether a "for the duration of the copyright" statement is needed. Changing it is a MAJOR version change and was **not** made.
2. **F2 Written agreement (Art. 80(1)).** Assess whether public-license acceptance by use meets the written-agreement requirement for Indonesian licensees.
3. **F3 Recording (Art. 83).** Without recording under PP 36/2018, effect against third parties is limited; decide whether commercial grants should be recorded.
4. **F4 Language and forum.** The text is in English; Indonesian-law contracts may require Indonesian language (UU 24/2009 Art. 31 and Perpres 63/2019 for agreements involving Indonesian parties). Not verified here; counsel should confirm. [docs/akad-syari-id.md](akad-syari-id.md) is explanatory, not the operative text.
5. **F5 Enforceability of §5.** Religious language creates ethical and, where the law allows, civil-law obligations only; the text already disclaims worldly religious penalties.

## D. Conclusion

No provision of AW-NC 3.0.0 was found to conflict with the checked statutory articles, the MUI fatwa or the cited scriptural principles. Findings F1–F5 are open questions for qualified reviewers. Do not describe AW-NC as "Sharia certified" or "legally approved".
