#!/usr/bin/env python3
"""Dependency-free consistency validation for versioned AW-NC legal texts."""
from __future__ import annotations

import hashlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
LEGACY_SHA = "207347b763b8dd8b7dcdcb3959c575c0fe4b1e25"
PREVIOUS_SHA = "c0aae42e0dd6f2da4827cb49ef62623e87ed879c"


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def main() -> int:
    errors: list[str] = []
    version = read("VERSION").strip()
    if not re.fullmatch(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?", version):
        errors.append(f"Invalid SemVer version: {version!r}")
    license_text = read("LICENSE.md")
    for path in ("README.md", "NOTICE", "CHANGELOG.md"):
        if version not in read(path):
            errors.append(f"{path} does not mention VERSION {version}")
    if f"# AW Non-Commercial License {version}" not in license_text:
        errors.append("LICENSE.md heading does not match VERSION")
    if f"## [{version}]" not in read("CHANGELOG.md"):
        errors.append("Current version missing from CHANGELOG.md")
    major = int(version.split(".", 1)[0]) if version and version[0].isdigit() else 0
    if major >= 2:
        for clause in (
            "## 5. CONTRACTUAL COVENANT, AMANAH, AND SHARIA-ALIGNED COMMITMENT",
            "Allah Jalla wa 'Ala",
            "No Licensee is required",
            "## 6. APPLICABLE LAW, THIRD-PARTY RIGHTS, AND INTERPRETATION",
            "## 7. VERSION SCOPE AND NON-RETROACTIVITY",
        ):
            if clause not in license_text:
                errors.append(f"Missing operative clause: {clause}")
    legacy_bytes = (ROOT / "licenses/AW-NC-1.0.0.md").read_bytes()
    git_sha = hashlib.sha1(b"blob " + str(len(legacy_bytes)).encode() + b"\0" + legacy_bytes).hexdigest()
    if git_sha != LEGACY_SHA:
        errors.append(f"Archived 1.0.0 bytes changed: {git_sha} != {LEGACY_SHA}")
    if major >= 3:
        for clause in (
            "## 8. COEXISTING LICENSES AND SCOPE OF NEW DEVELOPMENTS",
            "not automatically AW-NC",
            "Pre-Existing Material",
            "AW-NC Covered Material",
        ):
            if clause not in license_text:
                errors.append(f"Missing operative Section 8 term: {clause}")
        previous_bytes = (ROOT / "licenses/AW-NC-2.0.0.md").read_bytes()
        previous_sha = hashlib.sha1(b"blob " + str(len(previous_bytes)).encode() + b"\0" + previous_bytes).hexdigest()
        if previous_sha != PREVIOUS_SHA:
            errors.append(f"Archived 2.0.0 changed: {previous_sha} != {PREVIOUS_SHA}")
        if "LicenseRef-AW-NC-3.0.0" not in read("COMPONENT-LICENSE-MAP.md"):
            errors.append("Component license map missing version")
    if not read("docs/akad-syari-id.md").strip():
        errors.append("Missing Indonesian explanation")
    if errors:
        print("AW-NC validation FAILED:")
        for err in errors:
            print("- " + err)
        return 1
    print(f"AW-NC {version}: version, clauses, changelog and immutable 1.0.0 and 2.0.0 archives verified.")
    print("Note: technical checks DO NOT establish legal enforceability or Sharia certification.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
