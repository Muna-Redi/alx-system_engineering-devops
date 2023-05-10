#!/usr/bin/python3
""" script querries the reddit API for subscribers of a given subreddit """

import json
import requests


def number_of_subscribers(subreddit):
    """ function returns the number of subscribers for a given subreddit """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {
        "User-Agent":
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101\
        Firefox/15.0.1"
    }
    response = (requests.get(url, headers=user_agent)).json()

    try:
        subscribers = response.requests.get("data").requests.get("subscribers")
    except Exception as e:
        subscribers = 0

    return subscribers
