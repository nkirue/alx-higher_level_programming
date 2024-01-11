#!/usr/bin/python3
"""
Module description goes here.
"""

import urllib.request

def fetch_status(url):
    """
    Fetches the status from the given URL using the urllib package.

    Args:
    - url (str): The URL to fetch the status from.

    Returns:
    - str: The body of the response.
    """
    with urllib.request.urlopen(url) as response:
        body = response.read()
        return body.decode('utf-8')

if __name__ == "__main__":
    # Example usage
    url = 'https://alx-intranet.hbtn.io/status'
    response_body = fetch_status(url)
    print("Body response:")
    print("\t- type:", type(response_body))
    print("\t- content:", response_body)
