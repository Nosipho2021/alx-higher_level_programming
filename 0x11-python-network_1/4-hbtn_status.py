#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the requests package.
"""

import requests


def fetch_status():
    """
    Fetches the status from https://alx-intranet.hbtn.io/status.
    """
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    body = fetch_status()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
