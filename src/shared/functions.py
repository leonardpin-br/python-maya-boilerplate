# -*- coding: utf-8 -*-
u"""Usefull functions available to other packages in this project.

"""

__all__ = [
    'add_site_packages_to_sys_path',
    'constant',
    'get_subdir_full_paths',
    'number_format',
    'password_hash',
    'password_verify',
    'print_error_message',
    'print_sys_path'
]
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__link__ = u"https://www.leonardopinheiro.net"

import os
import sys
import inspect
import locale


def add_site_packages_to_sys_path(path_to_module, venv_folder_name='py27env'):
    u"""Adds the site-packages folder to sys.path.

    Args:
        path_to_module (str): The full path to the module calling this function.
        venv_folder_name (str, optional): The virtual environment's folder name.
            Defaults to 'py27env'.

    Example:
        How to call this function::

            import shared
            shared.add_site_packages_to_sys_path(__file__)

            # The package inside <project_root>/py27env/Lib/site-packages folder.
            import mysql.connector
    """

    # It is necessary to add 'site-packages' to sys.path to find mysql.connector
    current_dir = os.path.dirname(os.path.realpath(path_to_module))
    root_dir = os.path.dirname(os.path.dirname(current_dir))
    path_to_package = os.path.join(
        root_dir, venv_folder_name, 'Lib', 'site-packages')

    for path in sys.path:
        if path == path_to_package:
            break
    else:
        sys.path.append(path_to_package)


def constant(f):
    u"""Decorator that allows the behaviour of constants in other languages.

    Args:
        f (Any): The variable to be treated as constant by this decorator.

    References:
        `How do I create a constant in Python?`_

    .. _How do I create a constant in Python?:
       https://stackoverflow.com/a/2688086

    """

    def fset(self, value):
        print_error_message("Constants shoud not receive a new value.")
        raise TypeError

    def fget(self):
        return f()
    return property(fget, fset)


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


def number_format(num, places=0):
    u"""Mimics the PHP function number_format().

    Args:
        num (int | float): An int or a float number to be formatted with the
            given number of decimal places.
        places (int, optional): The number of decimal places. Defaults to 0.

    Returns:
        str: A formatted string.

    References:
        `How to convert php number_format() function to python`_

    .. _How to convert php number_format() function to python:
       https://stackoverflow.com/a/56748295

    """

    return locale.format_string("%.*f", (places, num), True)


# add_site_packages_to_sys_path(__file__)
# Maya cannot load the .pyd file from BCrypt.
# <project_root>/py27env/Lib/site-packages/bcrypt/_bcrypt.pyd
# But, outside of Maya, the line below works OK.
# import bcrypt


def password_hash(password):
    u"""Creates a password hash, using BCrypt.

    This function works fine outside of Autodesk Maya. But, that program
    cannot load the .pyd file from BCrypt::

        <project_root>/py27env/Lib/site-packages/bcrypt/_bcrypt.pyd

    Args:
        password (str): The password to be hashed.

    Returns:
        str: The hashed password.

    References:
        `Hashing Passwords in Python with BCrypt`_

    .. _Hashing Passwords in Python with BCrypt:
       https://stackabuse.com/hashing-passwords-in-python-with-bcrypt/
    """

    # # Convert the password to the array of bytes first (see reference).
    # bytePwd = password.encode('utf-8')

    # # Generate salt.
    # mySalt = bcrypt.gensalt()

    # # Hash password.
    # hash = bcrypt.hashpw(bytePwd, mySalt)

    # return hash

    pass


def password_verify(password, hash_from_database):
    u"""Verifies the given password against the one stored in the database.

    Args:
        password (str): The given password (from the object in memory).
        hash_from_database (str): The hash stored in the database.

    Returns:
        bool: True if they match. False otherwise.

    References:
        `Hashing Passwords in Python with BCrypt`_

        `bcrypt.checkpw returns TypeError: Unicode-objects must be encoded before checking`_

    .. _Hashing Passwords in Python with BCrypt:
       https://stackabuse.com/hashing-passwords-in-python-with-bcrypt/
    .. _bcrypt.checkpw returns TypeError\: Unicode-objects must be encoded before checking:
       https://stackoverflow.com/a/40578384
    """

    # encoded_password = password.encode('utf8')
    # encoded_hash = hash_from_database.encode('utf8')

    # result = bcrypt.checkpw(encoded_password, encoded_hash)

    # return result

    pass


def print_error_message(error_message):
    u"""Prints a formatted (and easy to read in the console) error message.

    Args:
        error_message (str | Error): A string to be printed or an instance
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
        caller_function = inspect.stack()[1][3]  # Python 2.7
    except:
        caller_function = inspect.stack()[1].function  # Python 3.5+

    print("\n\n================================================================================================\n")
    print("Error:")
    print('{caller_function}(): {error_message}'.format(
        caller_function=caller_function, error_message=error_message))
    print("")
    print("================================================================================================\n\n")


def print_sys_path():
    u"""Prints every path in ``sys.path``.

    """
    for path in sys.path:
        print(path)
