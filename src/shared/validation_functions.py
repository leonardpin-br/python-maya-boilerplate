# -*- coding: utf-8 -*-
u"""Usefull validation functions available to other packages in this project.

"""

__all__ = [
    'in_list',
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
    'has_length',
    'has_inclusion_of',
    'has_exclusion_of',
    'has_string',
    'has_valid_email_format'
]
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__link__ = u"https://www.leonardopinheiro.net"

import re


# Utility functions (used by the validation functions)
# ==============================================================================

def in_list(needle, haystack):
    u"""Checks if a value exists in a list.

    Args:
        needle (Any): The searched value.
        haystack (list): The list.

    Returns:
        bool: Returns True if needle is found in the list, False otherwise.

    References:
        `in_array`_

        `How to check if an element exists in a Python array (Equivalent of PHP in_array)?`_

    .. _in_array:
       https://www.php.net/manual/en/function.in-array.php
    .. _How to check if an element exists in a Python array (Equivalent of PHP in_array)?:
       https://stackoverflow.com/a/14743170
    """

    if needle in haystack:
        return True

    return False


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


def has_length(value, options):
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

            shared.has_length('abcd', {"min": 3, "max": 5})

    References:
        `Dictionary with some mandatory keys as function input`_

    .. _Dictionary with some mandatory keys as function input:
       https://stackoverflow.com/a/21014868
    """

    if "min" in options and not has_length_greater_than(value, options['min'] - 1):
        return False
    elif "max" in options and not has_length_less_than(value, options['max'] + 1):
        return False
    elif "exact" in options and not has_length_exactly(value, options['exact']):
        return False
    else:
        return True


def has_inclusion_of(value, set):
    u"""Validate inclusion in a set.

    Args:
        value (Any): The value to be searched in the set.
        set (list[Any]): The list to search in.

    Returns:
        bool: True if found. False otherwise.

    Example:
        Calling this function::

            shared.has_inclusion_of(5, [1, 3, 5, 7, 9])
    """

    return in_list(value, set)


def has_exclusion_of(value, set):
    u"""Validate exclusion from a set.

    Args:
        value (Any): The value to search in the set.
        set (list[Any]): The list to search for the value

    Returns:
        bool: True if not in the list. False otherwise.

    Example:
        Calling this function::

            shared.has_exclusion_of(12, [1, 3, 5, 7, 9])
    """

    return not in_list(value, set)


def has_string(value, required_string):
    u"""Validate inclusion of character(s).

    find returns the starting index of the substring or -1.

    Args:
        value (str): The bigger string.
        required_string (str): The substring.

    Returns:
        bool: True if found. False otherwise.

    Example:
        Calling this function::

            shared.has_string('nobody@nowhere.com', '.com')

    References:
        `Methods to check if a python string contains a substring`_

    .. _Methods to check if a python string contains a substring:
       https://flexiple.com/python-string-contains/#section32
    """

    if value.find(required_string) != -1:
        return True
    else:
        return False


def has_valid_email_format(value):
    r"""Validate correct format for email addresses.

    ``Format: [chars]@[chars].[2+ letters]``

    Example:
        Original regex (from the course). Not used here::

            pat = '/\A[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\Z/i'

    Args:
        value (str): The string to be matched against the regular expression.

    Returns:
        bool: True if the string has valid format. False otherwise.

    Example:
        Calling this function::

            shared.has_valid_email_format("popular_website15@comPany.com")

    References:
        `Python program to validate email address`_

    .. _Python program to validate email address:
       https://www.tutorialspoint.com/python-program-to-validate-email-address
    """

    # Original regex (from the course):
    # pat = '/\A[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\Z/i'
    # Regex from the reference:
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat, value):
        return True
    return False
