#!/usr/bin/env sh
set -eu

echo "==> Ruff lint fix"
uv run ruff check . --fix

echo "==> Ruff format"
uv run ruff format .

echo "==> Mypy type check"
uv run mypy .