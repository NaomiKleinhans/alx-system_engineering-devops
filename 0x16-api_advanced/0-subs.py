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
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {
        'User-Agent': 'Custom User Agent'
    }
    
    # Construct the URL for the subreddit's about page
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    # Make the API request
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            
            # Extract the number of subscribers
            subscribers = data['data']['subscribers']
            
            return subscribers
        except (KeyError, ValueError):
            return 0  # Return 0 if there was an error parsing the response JSON
    else:
        return 0  # Return 0 if the API request was not successful
