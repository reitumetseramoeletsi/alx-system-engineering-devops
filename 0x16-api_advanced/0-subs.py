#!/usr/bin/python3
"""
return number of subreddit subscribers 
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """A function that takes subreddit as input"""
    headers = {'User-Agent': 'Hello'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
