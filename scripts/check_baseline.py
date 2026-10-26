#!/usr/bin/env python3
"""Fail when a canonical license text no longer matches its approved baseline."""
from __future__ import annotations

import hashlib
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]


def blob_sha(path: pathlib.Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> int:
    errors = []
    for line in (ROOT / "scripts/license-baseline.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        name, expected = line.split()
        actual = blob_sha(ROOT / name)
        if actual != expected:
            errors.append(f"{name}: {actual} != approved baseline {expected}")
    if errors:
        print("Unapproved license text mutation detected:")
        print("\n".join("- " + e for e in errors))
        return 1
    print("Canonical license texts match approved baselines.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
