#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":

    """fetches https://alx-intranet.hbtn.io/status"""
    url = 'https://alx-intranet.hbtn.io/status'
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as reply:
            response = reply.read()
            response_html = response.decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(response)))
        print("\t- content: {}".format(response))
        print("\t- utf8 content: {}".format(response_html))

    except urllib.error.URLError as e:
        print(e.reason)
