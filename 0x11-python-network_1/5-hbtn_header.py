#!/usr/bin/python3
"""  displays the value of the variable X-Request-Id in the resp. header """
import requests
import sys

if __name__ == "__main__":
    ur = sys.argv[1]
    response = requests.get(ur)
    print(response.headers.get('X-Request-Id'))
