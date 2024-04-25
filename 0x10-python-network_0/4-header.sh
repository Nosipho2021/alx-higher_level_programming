#!/usr/bin/python3
# This script takes a URL as input, sends a GET request to the URL using curl,
# and displays the body of the response. It also includes a custom header X-School-User-Id with the value 98.

# Check if the number of arguments is exactly 1
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL from the command line argument
url="$1"

# Use curl to send a GET request to the URL with custom header X-School-User-Id and display the body of the response
curl -s -H "X-School-User-Id: 98" "$urli"
