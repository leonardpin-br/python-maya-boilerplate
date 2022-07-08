# -*- coding: utf-8 -*-
u"""Usefull validation functions available to other packages in this project.

"""

__all__ = [
    'is_none',
    'is_set',
    'list_equals',
    'trim',
    # ----------
    'is_blank',
    'has_presence',
    'has_length_greater_than',
    'has_length_less_than',
    'has_length_exactly',
    'has_length'
]
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__link__ = u"https://www.leonardopinheiro.net"


# Utility functions (used by the validation functions)
# ==============================================================================


def is_none(variable):
    u"""Mimics loosely the behavior of the PHP function is_null().

    Finds whether a variable is None.

    Args:
        variable (Any): The variable being evaluated.

    Returns:
        bool: Returns True if value is None, False otherwise.
    """
    if variable is None:
        return True

    return False


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


def trim(value):
    u"""Mimics loosely the behaiour of the PHP trim() function.

    Args:
        value (str): The string to be trimmed.

    Returns:
        str: The trimmed string
    """
    return value.strip()

# Validation functions
# ==============================================================================


def is_blank(value):
    u"""Checks if the given string is empty.

    Validate data presence.
    Uses ``trim()`` so empty spaces don't count.
    Uses ``trim(value) == ""`` to avoid empty strings.

    Args:
        value (str): The string to be checked.

    Returns:
        bool: True if the string is empty. False otherwise.

    Example:
        How to call this function::

            shared.is_blank("")
    """
    return not is_set(value) or trim(value) == ""


def has_presence(value):
    u"""Validate data presence. Reverse of isBlank().

    Args:
        value (str): The string to be checked.

    Returns:
        bool: True if it has presence. False otherwise.

    Example:
        Calling this function::

            shared.hasPresence('abcd')
    """
    return not is_blank(value)


def has_length_greater_than(value, min):
    u"""Validate string length. Spaces count towards length. Use ``trim()`` if
    spaces should not count.

    Args:
        value (str): The string to be verified.
        min (int): The minimun number to compare the string with.

    Returns:
        bool: True if the string is greater. False otherwise.

    Example:
        Calling this function::

            shared.has_length_greater_than('abcd', 3)
    """
    length = len(value)
    return length > min


def has_length_less_than(value, max):
    u"""Validate string length. Spaces count towards length. Use ``trim()`` if
    spaces should not count.

    Args:
        value (str): The string to be verified.
        max (int): The maximun number to compare the string with.

    Returns:
        bool: True if the string is smaller. False otherwise.

    Example:
        Calling this function::

            shared.has_length_less_than('abcd', 5)
    """
    length = len(value)
    return length < max


def has_length_exactly(value, exact):
    u"""Validate string length. Spaces count towards length. Use ``trim()`` if
    spaces should not count.

    Args:
        value (str): The string to be verified.
        exact (int): The exact number that should be the string's length.

    Returns:
        bool: True if the string has that length. False otherwise.

    Example:
        Calling this function::

            shared.has_length_exactly('abcd', 4)
    """
    length = len(value)
    return length == exact


def has_length(value, options={'min': 0, 'max': 0, 'exact': 0}):
    u"""Validate string length. Combines functions greater_than, less_than and
    exactly. Spaces count towards length. Use ``trim()`` if spaces should not
    count.

    Args:
        value (str): The string to be verified.
        options (dict[min, max, exact]): Dictionary with properties to check the string length.

    Returns:
        bool: True if the string has that length. False otherwise.

    Example:
        Calling this function::

            shared.has_length('abcd', {"min": 1, "max": 5, "exact": 4})

    References:
        `Dictionary with some mandatory keys as function input`_

    .. _Dictionary with some mandatory keys as function input:
       https://stackoverflow.com/a/21014868
    """
    # length = len(value)
    # return length == exact
    print(options['min'])
    print(options['max'])
    print(options['exact'])
