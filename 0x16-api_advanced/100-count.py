#!/usr/bin/python3
"""This module recursively counts and prints the occurrences of keywords in hot articles of a Reddit subreddit."""

import requests
import collections

def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively count and print the occurrences of keywords in hot articles of a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str, optional): The "after" parameter for pagination. Defaults to None.
        counts (collections.Counter, optional): A Counter object to store keyword counts. Defaults to None.

    Returns:
        None
    """
    if counts is None:
        counts = collections.Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10&after={after}"
    headers = {"User-Agent": "My Reddit API Client"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"].lower()  # Convert to lowercase for case-insensitive comparison
            for keyword in word_list:
                if title.find(keyword) != -1:
                    counts[keyword] += 1

        after = data["data"]["after"]

        if after:
            # If there are more pages, make a recursive call
            count_words(subreddit, word_list, after, counts)
        else:
            # Sort and print the results
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for keyword, count in sorted_counts:
                print(f"{keyword}: {count}")
    else:
        # If the subreddit is invalid or no posts match, print nothing
        return

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x.lower() for x in sys.argv[2].split()])
