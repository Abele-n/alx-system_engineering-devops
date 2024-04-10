#!/usr/bin/python3
"""function that queries Reddit API and returns the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API.

    returns number of subscribers to the subreddit.
    """
    subr_info = requests.get("https://www.reddit.com/r/{}/about.json"
                             .format(subreddit),
                             headers={"User-Agent": "My-User-Agent"},
                             allow_redirects=False)
    if subr_info.status_code >= 300:
        return 0, "nonexisting Subreddit"

    result = subr_info.json().get("data").get("subscribers", 0)
    return result, "existing Subreddit"
