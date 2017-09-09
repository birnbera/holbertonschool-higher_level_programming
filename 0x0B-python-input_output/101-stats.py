#!/usr/bin/python3
"""101-stats.py is a program that reads IP logs from stdin and
prints metrics every ten lines or until EOF or Ctrl-C.

IP logs are formatted as in:
    <IPv4> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

Example usage:

    ~$ ./101-generator.py | ./101-stats.py
     File size: 5213
     200: 2
     401: 1
     403: 2
     404: 1
     405: 1
     500: 3
     File size: 11320
     200: 3
     301: 2
     400: 1
     401: 2
     403: 3
     404: 4
     405: 2
     500: 3
     File size: 16305
     200: 3
     301: 3
     400: 4
     401: 2
     403: 5
     404: 5
     405: 4
     500: 4
     ^CFile size: 17146
     200: 4
     301: 3
     400: 4
     401: 2
     403: 6
     404: 6
     405: 4
     500: 4
     Traceback (most recent call last):
       File "./101-stats.py", line 15, in <module>
     Traceback (most recent call last):
       File "./101-generator.py", line 8, in <module>
         for line in sys.stdin:
     KeyboardInterrupt
         sleep(random.random())
     KeyboardInterrupt
"""


def print_dict_sorted_nonzero(status_codes):
    """Subroutine to print status codes with nonzero value in
    numericalorder.

    Args:
        status_codes (dict): dictionary of status codes and the
            number of times each one has been returned.
    """
    sorted_keys = sorted(status_codes.keys())
    print('\n'.join(["{:d}: {:d}".format(k, status_codes[k])
                     for k in sorted_keys if status_codes[k] != 0]))

if __name__ == "__main__":
    import sys

    try:
        total = 0
        status_codes = \
            {code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
        for n, line in enumerate(sys.stdin, 1):
            words = line.split()
            total += int(words[-1])
            status_codes[int(words[-2])] += 1
            if n % 10 == 0:
                print("File size: {:d}".format(total))
                print_dict_sorted_nonzero(status_codes)
    finally:
        print("File size: {:d}".format(total))
        print_dict_sorted_nonzero(status_codes)
