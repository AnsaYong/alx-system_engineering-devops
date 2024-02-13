#!/usr/bin/python3
"""This module provides a function that queries
the Reddit API.
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number
    of subscribers for a given subreddit.

    Arguments:
        subreddit: the subreddit to be queried
    Returns:
        the number of subscribers for the given subreddit, if
        they eist, 0 otherwise
    """
    url = f"http://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'Abot'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
