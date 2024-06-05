#!/usr/bin/python3

"""
Return the number of subscribes
"""

import requests


def recurse(subreddit, hot_list=[]):

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)

    if (response.status_code) == 200:
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
