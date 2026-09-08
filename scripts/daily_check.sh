#!/usr/bin/env bash
# LLM Wiki daily check wrapper
# Extracts YUQUE_API_KEY from ~/.bashrc (credential stays outside the wiki),
# runs `sync_yuque.py plan`, outputs JSON to stdout.
set -euo pipefail

cd "$(dirname "$0")/.."

KEY=$(grep -oP '(?<=^export YUQUE_API_KEY=).*' /home/easyvps/.bashrc | head -1)
if [ -z "${KEY:-}" ]; then
    echo '{"error": "YUQUE_API_KEY not found in ~/.bashrc"}' >&2
    exit 1
fi
export YUQUE_API_KEY="$KEY"

python3 scripts/sync_yuque.py plan 2>&1