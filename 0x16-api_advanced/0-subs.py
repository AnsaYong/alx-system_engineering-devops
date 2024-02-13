#!/usr/bin/python3
"""This module provides a function that queries
the Reddit API.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number
    of subscribers for a given subreddit.

    Arguments:
        subreddit: the subreddit to be queried
    Returns:
        the number of subscribers for the given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'Custom User Agent'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0


if __name__ == "__main__":
    number_subscribers(sys.argv[1])
