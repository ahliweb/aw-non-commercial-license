#!/bin/sh
# Local-first release gate: run all checks. Exit non-zero on any failure.
set -e
cd "$(dirname "$0")/.."
python3 scripts/validate_license.py
python3 scripts/check_baseline.py
python3 scripts/check_links.py
python3 scripts/check_fixtures.py
python3 scripts/generate_sbom.py --check
