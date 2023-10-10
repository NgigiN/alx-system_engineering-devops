#!/usr/bin/python3
""" A recursive function that queries the REddit API and contains
the hot articles for a given subreddit otherwise returns None. """

import requests


def recurse(subreddit, hot_list=[]):
    """ Function reucrsively queries a subreddit and returns the titles
    of all hot articles. """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        response = response.json()
        data = response.get("data")
        children = data.get("children")

        for child in children:
            hot_list.append(child.get("data").get("title"))
        after = data.get("after")
        if after is not None:
            recurse(subreddit, hot_list)
        return hot_list
    else:
        return None
