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

# # Not necessary for execution, but necessary for documentation.
# currentdir = os.path.dirname(os.path.realpath(__file__))    # boilerplate
# userinterface_dir = os.path.join(currentdir, "userinterface")

# sys.path.append(userinterface_dir)

from subpackage import example_classes
from userinterface import maya_ui_template


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


    # UI CREATION
    # ==========================================================================
    global myWin  # It is very necessary!

    try:
        myWin.close()
    except:
        pass

    myWin = maya_ui_template.ScriptName()
    myWin.show()


    # CREATING CLASS INSTANCES
    # ==========================================================================
    obj = example_classes.ExampleSubclass()
    print(obj.return_message())
    print(obj.greeter())





main()
