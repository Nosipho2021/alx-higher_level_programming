#!/usr/bin/python3
"""
Module to access to the GitHub API and uses the information
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def main(argv):
    """
    Takes your GitHub credentials (username and password) and
    uses the GitHub API to display your id.
    """
    user = argv[1]
    password = argv[2]
    try:
        response = requests.get('https://api.github.com/user',
                                auth=HTTPBasicAuth(user, password))
        response.raise_for_status()  # Raise an exception for HTTP errors
        profile_info = response.json()
        print(profile_info['id'])
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
    except KeyError:
        print('Unable to retrieve user ID.')
    except Exception as err:
        print(f"An unexpected error occurred: {err}")


if __name__ == "__main__":
    main(argv)
