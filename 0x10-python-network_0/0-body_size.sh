#!/bin/bash

# This script sends a request to a URL and displays the size of the response

URL=$1

SIZE=$(curl -s -o /dev/null -w "%{size_download}" $URL)

echo "Response body size: $SIZE bytes"
