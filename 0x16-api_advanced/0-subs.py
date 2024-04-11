#!/usr/bin/python3
"""
0-subs.py
"""

import requests


def number_of_subscribers(subreddit: str):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    req = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers={"User-Agent": "Custom"})
    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    return 0
