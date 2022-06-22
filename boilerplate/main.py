#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""Entry point of this script/app.

This is the file to run from Autodesk Maya. It is advisable to create a shelf
button to run this app from there.

Example:
    How a shelf button can be written::

        # -*- coding: utf-8 -*-
        u'''Maya shelf button for this app to run.

        This is a (Maya) shelf button example to make this code run without conflict
        with the Sphinx's sphinx-apidoc tool.
        '''

        import sys

        module_path = 'E:\\\\cloud\\\\Backup\\\\Libraries\\\\scripts\\\\maya\\\\Boilerplate\\\\boilerplate'

        # Includes the module path in sys.path if it is not already there:
        for path in sys.path:
            if path == module_path:
                break
        else:
            sys.path.insert(0, module_path)

        import main
        reload(main)

Last modified in 2022-06-22

Python version 2.7.11 (Maya 2020)

If unit tests are in place, this is how they can be run::

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


import databaseobject.connection_db as connection_db


def get_subdir_full_paths(current_dir):

    # Will store the full paths of the immediate subdirectories
    # https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory
    subdir_full_paths = []
    subdir_names = next(os.walk(current_dir))[1]
    for directory in subdir_names:
        subdir_full_paths.append(os.path.join(current_dir, directory))

    return subdir_full_paths


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

    # Clear the terminal window.
    os.system('cls' if os.name == 'nt' else 'clear')

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

    # CONNECTING TO A DATABASE
    # ==========================================================================
    database = connection_db.ConnectionDB('localhost', 'webuser', 'secretpassword', 'chain_gang')
    result = database.query("""SELECT * from bicycles""")
    print(result)


main()
