#!/bin/bash

# This script sends a request to a URL and displays the size of the response

URL=$1
curl -s URL | wc -c
