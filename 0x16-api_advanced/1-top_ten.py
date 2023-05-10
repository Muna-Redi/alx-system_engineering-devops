#!/usr/bin/python3
""" This script prints title of first top ten hot posts for
    a given subreddit
"""

import json
import requests


def top_ten(subreddit):
    """ Function prints titles of a subreddit's top ten hot posts """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {
        "User-Agent":
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101\
        Firefox/15.0.1"
    }
    limit = {"limit": 10}
    response = (requests.get(url, headers=user_agent, params=limit)).json()

    try:

        posts = response.requests.get("data").requests.get("children")
        for post in posts:
            print(post.requests.get("data").requests.get("title"))

    except Exception as e:
        print("None")
