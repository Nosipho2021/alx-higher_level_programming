#!/usr/bin/python3
"""
Module to access to the GitHub API and uses the information
"""
import requests
import sys


def list_commits(repository, owner):
    """
    Function that list 10 commits (from the most recent to oldest)
    of the repository.The first argument will be the repository name
    and the second argument will be the owner name
    """

    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    params = {'per_page': 10}
    headers = {'Authorization': '
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'}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: Unable to fetch commit.")


if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]
    list_commits(repository, owner)
