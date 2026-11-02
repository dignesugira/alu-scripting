#!/usr/bin/python3
"""Query the Reddit API for the number of subscribers of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total subscribers of a subreddit, or 0 if invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alu-api-advanced/1.0 (by dignesugira)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get("data").get("subscribers")
