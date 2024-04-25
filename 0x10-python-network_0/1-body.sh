#!/usr/bin/python3
# This script takes a URL as input, sends a GET request to the URL using curl,
# and displays the body of the response if the status code is 200

# Check if the number of arguments is exactly 1
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL from the command line argument
url="$1"

# Send a GET request to the URL using curl and store the response
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

# Check if the response status code is 200 (OK)
if [ "$response" -eq 200 ]; then
    # If the status code is 200, display the body of the response
    curl -s "$url"
else
    # If the status code is not 200, display an error message
    echo "Error: Status code $response"
fi
