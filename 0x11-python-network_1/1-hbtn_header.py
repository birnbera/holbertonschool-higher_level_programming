#!/usr/bin/python3
"""Script to make a request to a url passed on the command line"""

import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as r:
    print(r.getheader('X-Request-Id', ''))
