#!/usr/bin/python3
"""
Recursive function
"""
import requests
import sys
after = None
count_dic = []


def count_words(subreddit, word_list):
    """The recursing function"""
    global after
    global count_dic
    headers = {'User-Agent': 'Hello'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)
