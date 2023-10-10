#!/usr/bin/python3
"""This module recursively retrieves the titles of all hot articles in a Reddit subreddit."""

import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively retrieve the titles of all hot articles in a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): A list to store the titles of hot articles. Defaults to an empty list.
        after (str, optional): The "after" parameter for pagination. Defaults to None.

    Returns:
        list: A list containing the titles of hot articles, or None if the subreddit is invalid or no results are found.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10&after={after}"
    headers = {"User-Agent": "My Reddit API Client"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        after = data["data"]["after"]

        if after:
            # If there are more pages, make a recursive call
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
