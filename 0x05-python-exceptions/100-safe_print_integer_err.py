#!/usr/bin/python3
import traceback as tb


def safe_print_integer_err(value):
    ret = False
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        message = "Unknown format code 'd' " \
        "for object of type '{:s}'".format(value.__class__.__name__)
        tb.print_exception(Exception,
                           Exception(message),
                           None,
                           limit=0,
                           chain=False)
    else:
        ret = True
    finally:
        return ret
