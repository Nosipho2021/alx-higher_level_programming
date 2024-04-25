#!/usr/bin/python3
# This script takes a URL as input, sends a request to that URL using curl,
# and displays the size of the body of the response in bytes

# Check if the number of arguments is exactly 1
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL from the command line argument
url="$1"

# Use curl to send a request to the URL and store the response body in a variable
response=$(curl -s "$url")

# Display the size of the response body in bytes
echo "Body size: ${#response} bytes"

