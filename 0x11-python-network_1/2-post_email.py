#!/usr/bin/python3
"""displays the body of the response (decoded in utf-8)"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    ur = sys.argv[1]
    val = {"email": sys.argv[2]}
    dat = urllib.parse.urlencode(val).encode("ascii")

    request = urllib.request.Request(ur, dat)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
