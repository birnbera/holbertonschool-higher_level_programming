#!/usr/bin/python3
"""Script that sends URL request and prints status code on error,
or the body on success."""

import urllib.error
import urllib.request
import sys

try:
    with urllib.request.urlopen(sys.argv[1]) as r:
        print(r.read().decode('utf8'))
except urllib.error.URLError as e:
    print('Error code: {}'.format(e.code))
