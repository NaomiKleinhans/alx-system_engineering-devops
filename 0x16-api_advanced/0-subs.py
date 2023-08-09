#!/usr/bin/python3
"""Module for task 0"""
import requests


def number_of_subscribers(subreddit):
    if subreddit is None or type(subreddit) is not str:
        return 0

    base_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced_project'}
    r = requests.get(base_url, headers=headers, allow_redirects=False).json()

    if r.get('data') is None:
        return 0

    subscribers = r.get('data').get('subscribers')
    return subscribers