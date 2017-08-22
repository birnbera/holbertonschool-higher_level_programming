#!/usr/bin/python3
import traceback as tb


def safe_print_integer_err(value):
    ret = False
    try:
        print("{:d}".format(value))
        ret = True
    except:
        message = "Unknown format code 'd' " \
                  "for object of type "      \
                  "'{:s}'".format(value.__class__.__qualname__)
        tb.print_exception(Exception,
                           Exception(message),
                           None,
                           limit=0,
                           chain=False)
    finally:
        return ret
