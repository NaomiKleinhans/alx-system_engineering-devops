#!/usr/bin/python3
"""
A function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is given, the function should return 0
"""

import requests

def number_of_subscribers(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    base_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': '0x16-api_advanced_project'}
    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
    else:
        return 0

subreddit_name = "python"
subscribers = number_of_subscribers(subreddit_name)
print(f"Subscribers of /r/{subreddit_name}: {subscribers}")
