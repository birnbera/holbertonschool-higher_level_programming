#!/usr/bin/python3
def magic_string():
    magic_string.i = getattr(magic_string, 'i', -1) + 1
    return 'Holberton' + ', Holberton'*magic_string.i
