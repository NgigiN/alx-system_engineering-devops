#!/usr/bin/python3
""" A recursive function that queries the Reddit API
 and returns a list containing the titles of all hot
 articles for a given subreddit. if no results are found,
return None. """

import requests


def recurse(subreddit, hot_list=[]):
    """ Function that queries the Reddit API """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?"
    headers = {"User-Agent": "Frocuts"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            hot_list.append(post['data']['title'])

        return hot_list
    else:
        return None
