# -*- coding: utf-8 -*-
u"""Usefull validation functions available to other packages in this project.

"""

__all__ = [
    'is_set',
    'list_equals'
]
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__link__ = u"https://www.leonardopinheiro.net"

# Utility functions (used by the validation functions)
# ==============================================================================


def is_set(*args):
    u"""Mimics loosely the behavior of the PHP function isset().

    Determine if a variable is declared and is different than None.

    Args:
        *args: Variable length argument list.

    Returns:
        (bool | None): Returns True if variable exists and is not None. False otherwise.

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


def list_equals(first_list, second_list):
    u"""Compare two lists (arrays).

    Args:
        first_list (list): The first list (array).
        second_list (list): The second list (array).

    Returns:
        bool: True if they are equal. False otherwise.

    References:
        `How to compare two lists in python?`_

    .. _How to compare two lists in python?:
       https://stackoverflow.com/a/3726365

    """

    if first_list == second_list:
        return True

    return False

# Validation functions
# ==============================================================================
