#!/usr/bin/env bash
# Display the size of an HTTP request body

curl --silent \
     --output /dev/null \
     --write-out '%{size_download}\n' \
     "$1"
