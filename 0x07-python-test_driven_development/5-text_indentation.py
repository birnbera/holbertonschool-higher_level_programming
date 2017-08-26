#!/usr/bin/python3
"""Module containing function to print strings by line

Contains no directly executable code. Should be imported
as a module.
"""


def text_indentation(text):
    """Function to print text double-spaced, using `.?:` as
    line separators.

    Args:
        text (str): String to print

    Returns: None.

    Raises:
        TypeError: If `text` not a string.
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    seps = '.:?'
    table = str.maketrans({k: k+'\n' for k in seps})
    for s in text.translate(table).split('\n'):
        if s:
            print(s.strip(), end='\n\n')
