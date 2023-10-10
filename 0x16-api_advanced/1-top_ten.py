#!/usr/bin/python3
"""This module retrieves and prints the titles of the first 10 hot posts in a Reddit subreddit."""

import requests

def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts in a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "My Reddit API Client"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        
        for post in posts:
            title = post["data"]["title"]
            print(title)
    else:
        print(None)

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
