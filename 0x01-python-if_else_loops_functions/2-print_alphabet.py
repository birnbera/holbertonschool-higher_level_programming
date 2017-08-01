#!/usr/bin/python3
i = 0
while i < 26:
    print("{:s}".format(chr(i + ord('a'))), end="")
    i += 1
