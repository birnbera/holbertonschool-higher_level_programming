#!/usr/bin/python3
import traceback as tb


def safe_print_integer_err(value):
    ret = False
    try:
        print("{:d}".format(value))
        ret = True
    except (ValueError, TypeError) as message:
        tb.print_exception(Exception,
                           Exception(message),
                           None,
                           limit=0,
                           chain=False)
    finally:
        return ret
