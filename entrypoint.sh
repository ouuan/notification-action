#!/bin/bash

set -eu

message="$(python /main.py "$1" "$2" "$3")"
delimiter="$(tr -dc A-Za-z </dev/urandom | head -c 50)"

echo "message<<$delimiter
$message
$delimiter" >> "$GITHUB_OUTPUT"
