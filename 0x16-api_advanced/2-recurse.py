#!/usr/bin/python3
"""
This module provides a recursive function to query the Reddit API
and return a list containing the titles of all hot articles for
a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store the titles of hot articles.
        after (str): The 'after' parameter for pagination.

    Returns:
        list: A list of titles of all hot articles, or None if the
              subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User-Agent"}
    params = {"after": after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        hot_list.extend([post.get('data', {}).get('title')
                        for post in data.get('children', [])])
        after = data.get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
