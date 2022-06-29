# -*- coding: utf-8 -*-
u"""Usefull functions available to other packages in this project.

"""

__all__ = [
    'get_subdir_full_paths',
    'print_sys_path',
    'print_error_message'
]
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__link__ = u"https://www.leonardopinheiro.net"

import os
import sys
import inspect


def get_subdir_full_paths(current_dir):
    u"""Will store the full paths of the immediate subdirectories.

    Args:
        current_dir (str): The directory's full path to get a list of
            subdirectories.

    Returns:
        list[str]: A list with the full paths of the immediate directories.

    Example:
        How to call this function::

            dir_path = os.path.dirname(os.path.realpath(__file__))

            result = shared.get_subdir_full_paths(dir_path)

    References:

        `Getting a list of all subdirectories in the current directory`_

        `Find the current directory and file's directory [duplicate]`_

    .. _Getting a list of all subdirectories in the current directory:
       https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory
    .. _Find the current directory and file's directory [duplicate]:
       https://stackoverflow.com/a/5137509

    """

    subdir_full_paths = []
    subdir_names = next(os.walk(current_dir))[1]
    for directory in subdir_names:
        subdir_full_paths.append(os.path.join(current_dir, directory))

    return subdir_full_paths


def print_sys_path():
    u"""Prints every path in ``sys.path``.

    """
    for path in sys.path:
        print(path)


def print_error_message(error_message):
    u"""Prints a formatted (and easy to read in the console) error message.

    Args:
        error_message (Union[str, Error]): A string to be printed or an instance
            of Error.

    References:

        `7.1.3.2. Format examples`_

        `Getting the caller function name inside another function in Python? [duplicate]`_

    .. _7.1.3.2. Format examples:
       https://python.readthedocs.io/en/v2.7.2/library/string.html#format-examples
    .. _Getting the caller function name inside another function in Python? [duplicate]:
       https://stackoverflow.com/a/900404
    """

    # Stores the caller function of this function.
    try:
        caller_function = inspect.stack()[1][3] # Python 2.7
    except:
        caller_function = inspect.stack()[1].function # Python 3.5+

    print("\n\n================================================================================================\n")
    print("Error:")
    print('{caller_function}(): {error_message}'.format(caller_function=caller_function, error_message=error_message))
    print("")
    print("================================================================================================\n\n")