#!/usr/bin/python3
"""
    A request for the top ten hot posts
"""
import requests


def top_ten(subreddit):
    """ A function to get top hot posts

    Args:
        subreddit (string): A subreddit queried
    """
    web = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'MyAPI/0.1'}
    main = requests.get(web,
                        headers=headers,
                        allow_redirects=False)
    if (main.status_code == 404):
        print(None)
    else:
        for post in main.json()['data']['children']:
            print(post['data']['title'])
