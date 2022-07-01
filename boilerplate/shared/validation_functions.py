# -*- coding: utf-8 -*-
u"""Usefull validation functions available to other packages in this project.

"""

__all__ = [
    'is_set'
]
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__link__ = u"https://www.leonardopinheiro.net"


def is_set(*args):
    """Mimics loosely the behaviour of the PHP function isset().

    Args:
        *args: Variable length argument list.

    Returns:
        bool: True if the variable(s) is(are) set. False otherwise.

    References:

        `Determine if variable is defined in Python [duplicate]`_

    .. _Determine if variable is defined in Python [duplicate]:
       https://stackoverflow.com/a/1592578

    """

    for variable in args:
        try:
            variable
        except NameError:
            return False
        else:
            return True