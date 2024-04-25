#!/usr/bin/python3
# This script sends a request to a URL passed as an argument using curl,
# and displays only the status code of the response.

# Check if the number of arguments is exactly 1
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL from the command line argument
url="$1"

# Use curl to send a request to the URL and store the response headers in a variable
response_headers=$(curl -s -I "$url")

# Extract the status code from the response headers and display it
echo "$response_headers" | head -n 1 | cut -d' ' -f2
