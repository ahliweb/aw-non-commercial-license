#!/usr/bin/env python3
"""Validate mixed-license fixtures (structure only; decisions are counsel hypotheses)."""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DECISIONS = {"allow-with-conditions", "needs-counsel-review", "block"}
COPYLEFT = ("GPL-", "AGPL-")  # strong copyleft; LGPL needs its own analysis


def main() -> int:
    errors: list[str] = []
    dirs = sorted(p for p in (ROOT / "fixtures/mixed-license").iterdir() if p.is_dir())
    if len(dirs) < 8:
        errors.append(f"Need at least 8 fixtures, found {len(dirs)}")
    seen_block = False
    for d in dirs:
        for name in ("README.md", "sbom.spdx.json", "expected-decision.json"):
            if not (d / name).is_file():
                errors.append(f"{d.name}: missing {name}")
        if errors and not (d / "sbom.spdx.json").is_file():
            continue
        sbom = json.loads((d / "sbom.spdx.json").read_text(encoding="utf-8"))
        exp = json.loads((d / "expected-decision.json").read_text(encoding="utf-8"))
        if not str(sbom.get("spdxVersion", "")).startswith("SPDX-2."):
            errors.append(f"{d.name}: bad spdxVersion")
        if exp.get("decision") not in DECISIONS:
            errors.append(f"{d.name}: invalid decision {exp.get('decision')!r}")
        if exp.get("requiresCounselReview") is not True or "PENDING" not in exp.get("counselStatus", ""):
            errors.append(f"{d.name}: must not claim counsel approval")
        extracted = {i["licenseId"]: i for i in sbom.get("hasExtractedLicensingInfos", [])}
        licenses = [p[k] for p in sbom.get("packages", []) for k in ("licenseConcluded", "licenseDeclared")]
        for lic in set(licenses):
            for token in lic.replace("(", " ").replace(")", " ").split():
                if token.startswith("LicenseRef-") and not extracted.get(token, {}).get("extractedText"):
                    errors.append(f"{d.name}: {token} lacks extracted license text")
        has_copyleft = any(t.startswith(COPYLEFT) for lic in licenses for t in lic.replace("(", " ").replace(")", " ").split())
        has_awnc = any("AW-NC" in lic for lic in licenses)
        if exp.get("decision") == "block":
            seen_block = True
            if has_awnc and has_copyleft and "gpl-lib" not in d.name and "agpl" not in d.name:
                errors.append(f"{d.name}: AW-NC mixed with copyleft must be explained")
        elif has_copyleft and not has_awnc:
            errors.append(f"{d.name}: copyleft-only fixture cannot be allowed")
        if exp.get("decision") != "needs-counsel-review" and has_copyleft and has_awnc:
            errors.append(f"{d.name}: copyleft + AW-NC coexistence requires counsel review")
    if not seen_block:
        errors.append("At least one blocking fixture is required")
    if errors:
        print("Fixture check FAILED:")
        print("\n".join("- " + e for e in errors))
        return 1
    print(f"{len(dirs)} fixtures validated (structure/SBOM text only).")
    print("Note: expected decisions are hypotheses pending qualified counsel review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
