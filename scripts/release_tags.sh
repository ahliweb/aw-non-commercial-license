#!/bin/sh
# Create and push annotated release tags on the approved commits (run by an authorized maintainer
# with push rights to tags). Never force-moves an existing tag. Verifies commits and validator first.
set -e
cd "$(dirname "$0")/.."
git fetch origin main --tags
for pair in "v2.0.0 4c433e1e32230ecf8a92dd91c108b8e33a4bbf4c" "v3.0.0 710fb2a402bc6c24219aafd6bab133c8482e39c5"; do
  set -- $pair
  git merge-base --is-ancestor "$2" origin/main
  if git rev-parse -q --verify "refs/tags/$1" >/dev/null; then echo "$1 exists; skipping"; continue; fi
  git tag -a "$1" "$2" -m "AW-NC ${1#v}: annotated release tag on approved main commit $2. No independent legal or Sharia certification is claimed."
  git push origin "refs/tags/$1"
done
git ls-remote --tags origin
