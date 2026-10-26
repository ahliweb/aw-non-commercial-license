#!/usr/bin/env python3
"""Generate/verify a file-level SPDX 2.3 SBOM and dependency inventory for this repository.

Usage: generate_sbom.py [--check]   (--check fails if sbom/awnc.spdx.json is stale)
Scans: every tracked file (SHA-1/SHA-256), Python imports (stdlib vs third-party) and
GitHub Actions `uses:` references. It reports declared licenses only; it does not
establish legal compatibility.
"""
from __future__ import annotations

import ast
import hashlib
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "sbom/awnc.spdx.json"
# Third-party Actions used by workflows, with upstream license verified from each repository.
ACTION_LICENSES = {"actions/checkout": "MIT"}
LEGAL = {"LICENSE.md": "LicenseRef-AW-NC-3.0.0", "licenses/AW-NC-1.0.0.md": "LicenseRef-AW-NC-1.0.0",
         "licenses/AW-NC-2.0.0.md": "LicenseRef-AW-NC-2.0.0"}


def tracked() -> list[str]:
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return sorted(f for f in out.splitlines() if not f.startswith("sbom/"))


def scan() -> dict:
    third_party: set[str] = set()
    for f in tracked():
        if f.endswith(".py"):
            for node in ast.walk(ast.parse((ROOT / f).read_text(encoding="utf-8"))):
                names = [a.name for a in node.names] if isinstance(node, ast.Import) else \
                        [node.module or ""] if isinstance(node, ast.ImportFrom) and node.level == 0 else []
                third_party |= {n.split(".")[0] for n in names if n and n.split(".")[0] not in sys.stdlib_module_names}
    actions = set()
    for f in tracked():
        if f.startswith(".github/workflows/"):
            actions |= set(re.findall(r"uses:\s*([\w.-]+/[\w.-]+)@", (ROOT / f).read_text(encoding="utf-8")))
    return {"python_third_party": sorted(third_party), "actions": sorted(actions)}


def build() -> dict:
    s = scan()
    unknown = [a for a in s["actions"] if a not in ACTION_LICENSES]
    if s["python_third_party"] or unknown:
        raise SystemExit(f"Unreviewed dependencies: python={s['python_third_party']} actions={unknown}")
    files = []
    for i, f in enumerate(tracked(), 1):
        data = (ROOT / f).read_bytes()
        files.append({"SPDXID": f"SPDXRef-File-{i}", "fileName": "./" + f,
                      "checksums": [{"algorithm": "SHA1", "checksumValue": hashlib.sha1(data).hexdigest()},
                                    {"algorithm": "SHA256", "checksumValue": hashlib.sha256(data).hexdigest()}],
                      "licenseConcluded": LEGAL.get(f, "NOASSERTION"), "copyrightText": "NOASSERTION"})
    extracted = [{"licenseId": lid, "name": lid.removeprefix("LicenseRef-"),
                  "extractedText": (ROOT / path).read_text(encoding="utf-8"),
                  "comment": "Custom license, not on the SPDX License List"} for path, lid in LEGAL.items()]
    pkgs = [{"SPDXID": "SPDXRef-awnc", "name": "awnc", "downloadLocation": "https://github.com/ahliweb/awnc",
             "filesAnalyzed": True, "licenseConcluded": "NOASSERTION", "licenseDeclared": "LicenseRef-AW-NC-3.0.0",
             "licenseInfoFromFiles": ["NOASSERTION"], "copyrightText": "NOASSERTION",
             "comment": "Repository content (license texts, docs, scripts). Declared edition per LICENSE.md."}]
    rels = [{"spdxElementId": "SPDXRef-DOCUMENT", "relationshipType": "DESCRIBES", "relatedSpdxElement": "SPDXRef-awnc"}]
    for n, a in enumerate(s["actions"], 1):
        pkgs.append({"SPDXID": f"SPDXRef-action-{n}", "name": a, "downloadLocation": f"https://github.com/{a}",
                     "filesAnalyzed": False, "licenseConcluded": ACTION_LICENSES[a], "licenseDeclared": ACTION_LICENSES[a],
                     "copyrightText": "NOASSERTION", "comment": "CI build-time dependency; not distributed"})
        rels.append({"spdxElementId": "SPDXRef-awnc", "relationshipType": "DEPENDS_ON", "relatedSpdxElement": f"SPDXRef-action-{n}"})
    rels += [{"spdxElementId": "SPDXRef-awnc", "relationshipType": "CONTAINS", "relatedSpdxElement": x["SPDXID"]} for x in files]
    return {"spdxVersion": "SPDX-2.3", "dataLicense": "CC0-1.0", "SPDXID": "SPDXRef-DOCUMENT", "name": "awnc",
            "documentNamespace": "https://github.com/ahliweb/awnc/sbom/awnc",
            "creationInfo": {"created": "2026-01-01T00:00:00Z", "creators": ["Tool: scripts/generate_sbom.py"]},
            "packages": pkgs, "files": files, "relationships": rels, "hasExtractedLicensingInfos": extracted}


def main() -> int:
    text = json.dumps(build(), indent=2, ensure_ascii=False) + "\n"
    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            print("sbom/awnc.spdx.json is stale; run scripts/generate_sbom.py and commit.")
            return 1
        print("SBOM current; scan: no third-party Python dependencies; Actions reviewed.")
        return 0
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(text, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)}: {scan()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
