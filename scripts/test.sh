#!/usr/bin/env sh
set -eu

echo "==> Pytest"
uv run pytest -q --maxfail=1