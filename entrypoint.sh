#!/bin/bash

set -eu

message="$(python /main.py "$EVENT_NAME" "$EVENT_JSON" "$FORMAT")"
delimiter="$(tr -dc A-Za-z </dev/urandom | head -c 50)"

echo "message<<$delimiter
$message
$delimiter" >> "$GITHUB_OUTPUT"
