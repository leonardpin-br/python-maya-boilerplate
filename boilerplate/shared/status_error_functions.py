# -*- coding: utf-8 -*-
u"""Usefull functions to deal with errors.

"""

__all__ = [
    'display_errors',
]
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__link__ = u"https://www.leonardopinheiro.net"


def display_errors(errors):
    u"""Combines all the error messages in the errors list into one string.

    Args:
        errors (list[str]): The errors list.

    Returns:
        str: A string containing all the errors in the errors list.
    """

    output = ''
    if errors:
        output += "Please fix the following errors:\n"
        output += "--------------------------------\n"
        for error in errors:
            output += "    " + error + "\n"
    return output



