#!/usr/bin/python3
""" A recursive function that queries the Reddit API
 and returns a list containing the titles of all hot
 articles for a given subreddit. if no results are found,
return None. """

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """ Function that queries the Reddit API """
    global after
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Frocuts"}

    response = requests.get(url, headers=headers,
                            allow_redirects=False, params={'after': after},)

    if response.status_code == 200:
        for get_data in response.json().get("data").get("children"):
            data = get_data.get("data")
            title = data.get("title")
            hot_list.append(title)
        after = response.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list)

    else:
        return None
