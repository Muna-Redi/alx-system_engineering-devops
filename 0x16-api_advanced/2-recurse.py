#!/usr/bin/python3
""" This script prints title of first top ten hot posts for
    a given subreddit recursively
"""

import json
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """ Function prints titles of a subreddit's top ten hot posts """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {
        "User-Agent":
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101\
        Firefox/15.0.1"
    }
    param = {"after": after}
    response = requests.get(url, headers=user_agent, params=param,
                            allow_redirects=False)
    if response.status_code == 200:
        new_page = response.json().get("data").get("after")

        if new_page is not None:
            after = new_page
            recurse(subreddit, hot_list[])
        posts = response.json().get("data").get("children")

        for post in posts:
            hot_list.append(post.get("data").get("title"))
            return hot_list

    else:
        return None
