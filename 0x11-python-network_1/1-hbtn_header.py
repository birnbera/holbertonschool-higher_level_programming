#!/usr/bin/python3
"""Script to make a request to a url passed on the command line"""

if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.error import URLError
    from sys import argv

    try:
        with urlopen(argv[1]) as r:
            print(r.getheader('X-Request-Id', ''))
    except (URLError, IndexError) as e:
        print(e)
