#!/usr/bin/python3
import traceback as tb


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as e:
        tb.print_exception(Exception, Exception(e), None)
        result = None
    return result
