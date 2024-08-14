#!/usr/bin/python3
"""
This module provides a recursive function to query the Reddit API,
parse the titles of all hot articles, and print a sorted count of
given keywords.
"""

import requests


def count_words(subreddit, word_list, hot_list=[], after=""):
    """
    Recursively queries the Reddit API, parses the titles of all hot
    articles, and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count in the hot articles.
        hot_list (list): A list to store the titles of hot articles.
        after (str): The 'after' parameter for pagination.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User-Agent"}
    params = {"after": after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        hot_list.extend([post.get('data', {}).get('title').lower()
                        for post in data.get('children', [])])
        after = data.get('after')
        if after:
            return count_words(subreddit, word_list, hot_list, after)

        word_count = {word.lower(): 0 for word in word_list}
        for title in hot_list:
            for word in word_list:
                word_count[word.lower()] += title.split().count(word.lower())

        sorted_count = sorted(word_count.items(),
                              key=lambda kv: (-kv[1], kv[0]))

        for word, count in sorted_count:
            if count > 0:
                print(f"{word}: {count}")
    else:
        return None
