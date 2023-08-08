#!/usr/bin/python3

"""
Module: 3-count_words.py
"""

import requests
import re

def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses titles of hot articles, and prints a sorted count of keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str): Token for pagination.
        word_count (dict): Dictionary to store the count of keywords.

    Returns:
        None
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
            
            # Process titles for keyword count
            for post in posts:
                title = post['data']['title'].lower()
                
                for word in word_list:
                    # Use regex to match whole words only (not substrings)
                    pattern = fr'\b{re.escape(word)}\b'
                    matches = re.findall(pattern, title)
                    
                    if matches:
                        count = len(matches)
                        if word in word_count:
                            word_count[word] += count
                        else:
                            word_count[word] = count
            
            # Check for pagination
            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, after, word_count)
            else:
                sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_count:
                    print(f"{word}: {count}")
        except (KeyError, ValueError):
            print("None")  # Print None if there was an error parsing the response JSON
    else:
        print("None")  # Print None if the API request was not successful

# Test the function
subreddit_name = 'python'
keywords = ['python', 'javascript', 'java']
count_words(subreddit_name, keywords)
