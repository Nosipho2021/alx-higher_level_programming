#!/usr/bin/python3
# This script takes a URL as input, sends a POST request to the URL using curl,
# with specified parameters, and displays the body of the response.

# Check if the number of arguments is exactly 1
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL from the command line argument
url="$1"

# Send a POST request to the URL with specified parameters and display the body of the response
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$url"
