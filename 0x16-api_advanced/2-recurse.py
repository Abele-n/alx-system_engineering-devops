#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    return titles lists containing hot postings on a given subreddit

    :param subreddit: name to the subreddit query
    :param hot_list: (optional)hot title lists of articles
    :param after: (optional) pagination token for the nextpage article
    :param count: (optional) count of retrieved articles
    return: A list of titles for hot articles for the subreddit
    """
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
