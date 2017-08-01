#!/usr/bin/python3
for a in range(25, -1, -1):
    print("{:s}".format(chr(a + ord('a')) if a % 2 else chr(a + ord('A'))),
          end="")
