#!/usr/bin/python3

"""
Rerursive function: Return a list containing
the titles of all hot articles.
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {
            "after": after,
            "count": count,
            "limit": 100
            }
    response = requests.get(url, headers=headers,
                            params=params, allow_redirect=False)

    if (response.status_code) == 200:
        results = response.json().get("data")
        after = results.get("after")
        count += results.get("dist")
        for c in results.get("children"):
            hot_list.append(c.get("data").get("title"))
        if after is not None:
            return recurse(subreddit, hot_list, after, count)
        return hot_list
    else:
        return None
