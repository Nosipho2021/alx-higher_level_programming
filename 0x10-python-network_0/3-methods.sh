#!/usr/bin/python3
# This script takes a URL as input, sends a request to the URL using curl,
# and displays all HTTP methods accepted by the server

# Check if the number of arguments is exactly 1
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL from the command line argument
url="$1"

# Use curl to send a request to the URL and display the allowed methods
curl -sI "$url" | grep -i allow | cut -d' ' -f2-
