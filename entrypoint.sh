#!/bin/bash

# not using $(python /main.py "$1" "$2") because it exit with code 0 when error occurrs
set -eo pipefail
python /main.py "$1" "$2" | xargs -I MESSAGE echo "::set-output name=message::MESSAGE"
