#!/usr/bin/python3

"""script that fetches https://alx-intranet.hbtn.io/status"""

from requests import get


def get_alx_intranet(ur='https://alx-intranet.hbtn.io/status'):
    """
    script that fetches https://alx-intranet.hbtn.io/status
    """
    re = get(ur)
    print("Body response:")
    print("\t- type: {}".format(str(re).__class__))
    print("\t- content: {}".format(re.text))


if __name__ == "__main__":
    get_alx_intranet()
