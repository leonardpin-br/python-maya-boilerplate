#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""Entry point of the script/app.

This is the file to run.

Last modified in 2022-06-20

Python version 2.7.11 (Maya 2020)

Example:
    Running unittests::

        $ python -m unittest discover

References:
    `sphinx-apidoc ignoring some modules/packages`_

    `Coverage.py`_

    `Configuration reference`_

    `Test Code Coverage`_

.. _sphinx-apidoc ignoring some modules/packages:
   https://chadrick-kwag.net/sphinx-apidoc-ignoring-some-modules-packages/
.. _Coverage.py:
   https://coverage.readthedocs.io/en/6.3.2/#coverage-py
.. _Configuration reference:
   https://coverage.readthedocs.io/en/6.3.2/config.html#configuration-reference
.. _Test Code Coverage:
   https://cpske.github.io/ISP/testing/code-coverage

"""

import os
import sys


def get_subdir_full_paths(current_dir):

    # Will store the full paths of the immediate subdirectories
    # https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory
    subdir_full_paths = []
    subdir_names = next(os.walk(current_dir))[1]
    for directory in subdir_names:
        subdir_full_paths.append(os.path.join(current_dir, directory))

    return subdir_full_paths


# Not necessary for execution, but necessary for documentation.
current_dir = os.path.dirname(os.path.realpath(__file__))    # boilerplate
subdir_full_paths = get_subdir_full_paths(current_dir)

for subdir in subdir_full_paths:
    print(subdir)

print("\n=====================================================================")

# for path in sys.path:
#     for subdir in subdir_full_paths:
#         if subdir == path:
#             continue
#         sys.path.append(subdir)

# for path in sys.path:
#     print(path)

# userinterface_dir = os.path.join(currentdir, "userinterface")
# sys.path.append(userinterface_dir)
# databaseobject_dir = os.path.join(current_dir, "databaseobject")
# print(databaseobject_dir)
# sys.path.append(databaseobject_dir)

# # Se o caminho não faz parte do path:
# for path in sys.path:
#     if path == databaseobject_dir:
#         break
# else:
#     sys.path.insert(0, databaseobject_dir)

# from subpackage import example_classes
# from userinterface import maya_ui_template
# from databaseobject import connection_db


def print_sys_path():
    u"""Print every path in sys.path.

    Returns:
        bool: The returned value is always True.
    """
    for path in sys.path:
        print(path)

    return True


def untested_function():
    u"""The only reason this function exists is to not be tested.

    This function will appear, in the coverage HTML report, as an untested
    line of code.

    Returns:
        bool: The value is only an example and will not be used.
    """
    return False


def main():
    u"""The main function to execute the entire project/application.
    """

    # # Clear the terminal window.
    # os.system('cls' if os.name == 'nt' else 'clear')

    # # UI CREATION
    # # ==========================================================================
    # global myWin  # It is very necessary!

    # try:
    #     myWin.close()
    # except:
    #     pass

    # myWin = maya_ui_template.ScriptName()
    # myWin.show()

    # # CREATING CLASS INSTANCES
    # # ==========================================================================
    # obj = example_classes.ExampleSubclass()
    # print(obj.return_message())
    # print(obj.greeter())

    # CREATING MYSQL CONNECTION
    # ==========================================================================


main()
