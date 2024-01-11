#!/usr/bin/python3
"""  displays the body of the response (decoded in utf-8). """
import urllib.request
import sys


if __name__ == '__main__':
    re = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(re) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
