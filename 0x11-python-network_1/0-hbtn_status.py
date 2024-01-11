!/usr/bin/python3
""" Fetches the status from the given URL using the urllib package """
import urllib.request


if __name__ == '__main__':
    url = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(url) as response:
        print("Body response:")
        htm = response.read()
        print("\t- type:", type(htm))
        print("\t- content:", htm)
        print("\t- utf8 content:", htm.decode('utf-8'))
