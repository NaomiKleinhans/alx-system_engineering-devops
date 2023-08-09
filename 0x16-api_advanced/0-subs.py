#!/usr/bin/python3

"""
Module: 0-subs.py
"""

import requests

def number_of_subscribers(subreddit):
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