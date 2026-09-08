#!/usr/bin/env bash
# LLM Wiki daily check wrapper
# 1. Extracts YUQUE_API_KEY from ~/.bashrc (credential stays outside the wiki).
# 2. Runs `sync_yuque.py plan` and prints the JSON plan to stdout.
# 3. If there are local git changes not yet pushed (e.g. from an approved
#    update applied earlier in the session), commits and pushes them to
#    the private GitHub repo shakewingo/llm-wiki.
#
# This script NEVER applies wiki content changes on its own — it only
# reports the sync plan and syncs already-committed/staged local changes
# to the remote. Content updates always require explicit user approval
# performed interactively (editing pages, running wiki_tools.py, then
# `sync_yuque.py acknowledge`).
set -euo pipefail

cd "$(dirname "$0")/.."

KEY=$(grep -oP '(?<=^export YUQUE_API_KEY=).*' /home/easyvps/.bashrc | head -1)
if [ -z "${KEY:-}" ]; then
    echo '{"error": "YUQUE_API_KEY not found in ~/.bashrc"}' >&2
    exit 1
fi
export YUQUE_API_KEY="$KEY"

echo "=== sync plan ==="
python3 scripts/sync_yuque.py plan

echo "=== git sync ==="
if [ -n "$(git status --porcelain)" ]; then
    git add -A
    git commit -m "chore: daily wiki sync $(date -u +%Y-%m-%dT%H:%M:%SZ)" >/dev/null
    git push origin main 2>/dev/null
    echo "pushed: local changes committed and pushed to origin/main"
else
    # Still push in case a prior commit exists locally but wasn't pushed.
    LOCAL=$(git rev-parse main)
    REMOTE=$(git rev-parse origin/main 2>/dev/null || echo "")
    if [ "$LOCAL" != "$REMOTE" ]; then
        git push origin main 2>/dev/null
        echo "pushed: local main was ahead of origin/main"
    else
        echo "no-op: no local changes, nothing to push"
    fi
fi