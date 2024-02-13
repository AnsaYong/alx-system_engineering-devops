#!/usr/bin/python3
"""This module provides a function that
recursively queries the Reddit API.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to retrieve all hot
    articles for a given subreddit.

    Args:
        subreddit (str): The subreddit for which to retrieve hot articles.
        hot_list (list): A list to store the titles of the hot articles
                        (default=[]).
        after (str): A token for pagination (default=None).

    Returns:
        list: A list containing the titles of all hot articles for the given
        subreddit, or None if no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"
    headers = {
        'User-Agent': 'UAgent'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        if not posts:
            return hot_list
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        return recurse(subreddit, hot_list, after)
    else:
        return None
