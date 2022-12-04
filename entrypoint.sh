#!/bin/bash

set -e

MESSAGE=$(python /main.py "$1" "$2" "$3")

# escape characters
# https://github.community/t5/GitHub-Actions/set-output-Truncates-Multiline-Strings/m-p/38372#M3322
MESSAGE="${MESSAGE//'%'/'%25'}"
MESSAGE="${MESSAGE//$'\n'/'%0A'}"
MESSAGE="${MESSAGE//$'\r'/'%0D'}"

echo "message=$MESSAGE" >> "$GITHUB_OUTPUT"
