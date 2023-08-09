#!/usr/bin/python3
"""Module for task 3"""
import requests

def count_words(subreddit, word_list):
    if not word_list:
        return
    
    headers = {
        'User-Agent': 'Custom User Agent'
    }

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            articles = data['data']['children']

            word_count = {}
            for article in articles:
                title = article['data']['title'].lower()
                for word in word_list:
                    if word in title:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1
            
            sorted_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
            
            for word, count in sorted_count:
                print(f"{word}: {count}")
        except KeyError:
            pass

    else:
        return

    count_words(subreddit, word_list)