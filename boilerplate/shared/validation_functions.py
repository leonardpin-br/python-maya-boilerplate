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
    """Mimics loosely the behavior of the PHP function isset().

    Determine if a variable is declared and is different than None.

    Args:
        *args: Variable length argument list.

    Returns:
        bool: Returns True if variable exists and is not None. False otherwise.

    References:
        `Determine if variable is defined in Python [duplicate]`_

        `not None test in Python [duplicate]`_

        `Null in Python: What is None in Python`_

    .. _Determine if variable is defined in Python [duplicate]:
       https://stackoverflow.com/a/1592578
    .. _not None test in Python [duplicate]:
       https://stackoverflow.com/a/3965129
    .. _Null in Python\: What is None in Python:
       https://appdividend.com/2022/07/01/python-null/

    """

    for variable in args:
        try:
            variable

        # The variable was NOT defined.
        except NameError:
            return False

        # The variable was defined!
        else:

            # Checks if the variable is None.
            if variable is None:
                return False

            else:
                return True