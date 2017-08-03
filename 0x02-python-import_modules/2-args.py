#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    nargs = len(sys.argv) - 1
    print("{:d} {:s}{:s}".format(nargs,
                                 "argument" if nargs == 1 else "arguments",
                                 "." if nargs == 0 else ":"))
    for i, arg in enumerate(sys.argv[1:]):
        print("{:d}: {:s}".format(i + 1, arg))
