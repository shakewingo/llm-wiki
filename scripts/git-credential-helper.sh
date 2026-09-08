#!/usr/bin/env bash
# Minimal git credential helper for github.com pushes using the token
# stored in gh CLI's hosts.yml. Never echoes/logs the token elsewhere.
set -euo pipefail

action="${1:-get}"
if [ "$action" != "get" ]; then
    exit 0
fi

TOKEN=$(grep -m1 "oauth_token:" /home/easyvps/.config/gh/hosts.yml | awk '{print $2}')
echo "protocol=https"
echo "host=github.com"
echo "username=shakewingo"
echo "password=${TOKEN}"