#!/usr/bin/env python3
"""Check relative Markdown links and #anchors. Does not prove legal correctness."""
from __future__ import annotations

import pathlib
import re
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$")


def slug(text: str) -> str:
    text = re.sub(r"[`*_]|\[([^\]]*)\]\([^)]*\)", r"\1", text).lower()
    return re.sub(r"\s", "-", re.sub(r"[^\w\s-]", "", text))


def anchors(path: pathlib.Path) -> set[str]:
    return {slug(m.group(1)) for line in path.read_text(encoding="utf-8").splitlines() if (m := HEADING.match(line))}


def main() -> int:
    errors: list[str] = []
    for md in sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts):
        in_fence = False
        for no, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
            if in_fence:
                continue
            for target in LINK.findall(line):
                if re.match(r"[a-z][a-z0-9+.-]*:", target) or target.startswith("//"):
                    continue
                raw, _, frag = target.partition("#")
                dest = md if not raw else (md.parent / urllib.parse.unquote(raw)).resolve()
                rel = f"{md.relative_to(ROOT)}:{no}"
                if not dest.exists():
                    errors.append(f"{rel}: missing file {target}")
                elif frag and dest.suffix == ".md" and slug(urllib.parse.unquote(frag)) not in anchors(dest):
                    errors.append(f"{rel}: missing anchor {target}")
    if errors:
        print("Link check FAILED:")
        print("\n".join("- " + e for e in errors))
        return 1
    print("Relative Markdown links and anchors resolve.")
    print("Note: link checks DO NOT establish legal compatibility.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
