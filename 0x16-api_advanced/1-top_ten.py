#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """top 10 hottests posts on a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }
    paramts = {
            "limit": 10
            }
    resp = requests.get(url, headers=headers, paramts=paramts, \n
                        allow_redirects=False)
    if resp.status_code == 404:
        print("None")
        return
    results = resp.json().get("data")
    [print(m.get("data").get("title")) for m in results.get("children")]
