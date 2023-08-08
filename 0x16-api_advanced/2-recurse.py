#!/usr/bin/python3

"""
Module: 2-recurse.py
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store the titles of hot articles.
        after (str): Token for pagination.

    Returns:
        list: List containing titles of hot articles, or None if no results are found.
    """
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'Custom User Agent'
    }
    
    # Construct the URL for the subreddit's hot posts with pagination
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    if after:
        url += f'&after={after}'
    
    # Make the API request
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            
            # Extract the list of posts
            posts = data['data']['children']
            
            # Append titles of hot articles to the hot_list
            for post in posts:
                title = post['data']['title']
                hot_list.append(title)
            
            # Check for pagination
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        except (KeyError, ValueError):
            return None  # Return None if there was an error parsing the response JSON
    else:
        return None  # Return None if the API request was not successful

# Test the function
subreddit_name = 'python'
hot_articles = recurse(subreddit_name)
if hot_articles:
    for idx, title in enumerate(hot_articles, start=1):
        print(f"{idx}. {title}")
else:
    print(f"No results found for subreddit r/{subreddit_name}.")
