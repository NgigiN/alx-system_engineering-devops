#!/usr/bin/python3
""" Function that queries the Reddit API and prints the titles of
first 10 hot posts of a given subreddit. """

import requests

def top_ten(subreddit):
    """ Function that queries for the top 10 titles of a subreddit"""

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    headers = {'User-Agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            print(post['data']['title'])

    else:
        print("None")
