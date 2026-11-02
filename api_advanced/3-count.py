#!/usr/bin/python3
"""Recursively count keywords in the titles of a subreddit's hot posts."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of the given keywords in all hot post titles."""
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) alu-api/1.0"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return

    data = response.json().get("data")
    for post in data.get("children"):
        title_words = post.get("data").get("title").lower().split()
        for word in counts:
            counts[word] += title_words.count(word)

    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    lowered = [word.lower() for word in word_list]
    results = []
    for word in counts:
        total = counts[word] * lowered.count(word)
        if total > 0:
            results.append((word, total))
    for word, total in sorted(results, key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, total))
