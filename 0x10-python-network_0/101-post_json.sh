#!/bin/bash
#Script that sends a JSON POST request to a URL with the contents of a file in the body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1" 
