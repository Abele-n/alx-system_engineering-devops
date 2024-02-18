#!/usr/bin/python3
"""function queries the Reddit API and returns a list of titles on hot \n
   articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """return titles lists containing hot postings on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }
    params = {
            'after': after,
            'count': count,
            'limit': 100
            }
    resp = requests.get(url, headers=headers, params=params, \n
                        allow_redirects=False)
    if resp.status_code == 404:
        return None

    results = resp.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
