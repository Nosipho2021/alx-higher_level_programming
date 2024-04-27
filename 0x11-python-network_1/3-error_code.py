#!/usr/bin/python3
"""
Takes in a URL, sends request and displays the body of the response.
"""

import urllib.request
import urllib.error
import sys


def fetch_url_body(url):
    """
    Fetches the body of the response from the given URL.
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            return body
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    url = sys.argv[1]
    response_body = fetch_url_body(url)
    if response_body:
        print(response_body)
