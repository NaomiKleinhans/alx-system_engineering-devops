#!/usr/bin/python3
"""
Module: 0-subs.py
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if invalid.
    """
    headers = {
        'User-Agent': 'Custom User Agent'
    }

    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        except (KeyError, ValueError):
            return 0
    else:
        return 0

subreddit_name = "python"
subscribers = number_of_subscribers(subreddit_name)
print(f"Subscribers of /r/{subreddit_name}: {subscribers}")
