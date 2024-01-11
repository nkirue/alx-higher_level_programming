#!/usr/bin/python3
""" Displays the value  found in the header of the response """
import sys
import urllib.request


if __name__ == "__main__":
    html = sys.argv[1]
    with urllib.request.urlopen(html) as response:
        val = response.headers.get('X-Request-Id')
        print(val)
