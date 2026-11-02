#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
venv="$root/.venv"

[ -d "$venv" ] || "${PYTHON:-python3}" -m venv "$venv" 2>/dev/null || "${PYTHON:-python}" -m venv "$venv"
if [ -x "$venv/bin/python" ]; then bin="$venv/bin"; else bin="$venv/Scripts"; fi
"$bin/python" -m pip install --quiet --disable-pip-version-check -r "$root/requirements-gen.txt"

cd "$root"
PATH="$bin:$PATH" "$bin/openapi-python-client" generate \
  --path openapi/openapi.json \
  --config openapi-python-client.yaml \
  --meta none \
  --output-path src/larynth/generated \
  --overwrite

find src/larynth/generated -type f \( -name '*.py' -o -name '*.typed' \) -exec sed -i 's/\r$//' {} +
rm -rf src/larynth/generated/.ruff_cache
