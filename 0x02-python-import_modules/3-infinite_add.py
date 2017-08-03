#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    tot = 0
    for arg in sys.argv[1:]:
        tot += int(arg)
    print("{:d}".format(tot))
