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
    delims = '.:?'
    if type(text) is not str:
        raise TypeError('text must be a string')
    for c in delims:
        text = str(c + '\n\n').join(s.strip() for s in text.split(c))
    print(text, end='')
    if len(text) > 0 and text[-1] in delims:
        print('\n')
