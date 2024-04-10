#!/usr/bin/python3
"""function that queries Reddit API and returns the number of subscribers."""


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and returns number of subscribers to the subreddit.
    """
    import requests

    subr_info = requests.get("https://www.reddit.com/r/{}/about.json"
                             .format(subreddit),
                             headers={"User-Agent": "My-User-Agent"},
                             allow_redirects=False)
    if subr_info.status_code == 404:
        return 0

    return subr_info.json().get("data").get("subscribers")
