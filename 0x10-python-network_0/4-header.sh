#!/bin/bash
#script that sends a GET request with a header and displays the body of the response
curl -s -H "X-School-User-Id" "$1"
