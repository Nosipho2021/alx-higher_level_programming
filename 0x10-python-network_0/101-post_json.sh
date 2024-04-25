#!/usr/bin/python3
#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument,
# with the contents of a file passed as the second argument in the body of the request,
# and displays the body of the response.

# Check if the number of arguments is not equal to 2
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
fi

# Store the URL and JSON file name from the command line arguments
url="$1"
json_file="$2"

# Check if the JSON file exists
if [ ! -f "$json_file" ]; then
    echo "Error: JSON file '$json_file' not found."
    exit 1
fi

# Use curl to send a POST request with the contents of the JSON file in the body and display the body of the response
curl -s -X POST -d "@$json_file" -H "Content-Type: application/json" "$url"

