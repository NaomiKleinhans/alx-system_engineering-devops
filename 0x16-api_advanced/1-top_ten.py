#!/usr/bin/python3

"""
Module: 1-top_ten.py
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
    """
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'Custom User Agent'
    }
    
    # Construct the URL for the subreddit's hot posts
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    
    # Make the API request
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            
            # Extract the list of posts
            posts = data['data']['children']
            
            # Print the titles of the first 10 hot posts
            for post in posts:
                title = post['data']['title']
                print(title)
        except (KeyError, ValueError):
            print("None")  # Print None if there was an error parsing the response JSON
    else:
        print("None")  # Print None if the API request was not successful

# Test the function
subreddit_name = 'python'
top_ten(subreddit_name)
