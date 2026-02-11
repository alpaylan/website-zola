#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 scripts/generate_citations.py
zola build
