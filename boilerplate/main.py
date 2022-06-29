#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""Entry point of this script/app.

Last modified in 2022-06-29

Python version 2.7.11 (Autodesk Maya 2018 and 2020)

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

Note:
    If unit tests are in place, this is how they can be run::

        $ python -m unittest discover

Important:
    Sphinx (and its packages) **MUST** be installed in the virtual environment
    in order to avoid import errors.

    Having multiple Python versions on the machine and Sphinx installed in one
    of them, leads to confusion and hard to track bugs.

Note:
    How to generate the requirements.txt::

        $ pip freeze > requirements.txt

    How to install packages from requirements.txt::

        $ pip install -r requirements.txt

Note:
    To exclude certain modules from being documented, it is necessary to pass
    them as arguments to ``sphinx-apidoc``::

        sphinx-apidoc --force -o ./docs/sphinx/source ./boilerplate ./boilerplate/databaseobject/db_credentials.py

    The example above is in the **package.json** file as the ``build:source:doc`` script.

References:
    `sphinx-apidoc ignoring some modules/packages`_

    `Coverage.py`_

    `Configuration reference`_

    `Test Code Coverage`_

    `Python Sphinx exclude patterns`_

    `sphinx-apidoc`_

.. _sphinx-apidoc ignoring some modules/packages:
   https://chadrick-kwag.net/sphinx-apidoc-ignoring-some-modules-packages/
.. _Coverage.py:
   https://coverage.readthedocs.io/en/6.3.2/#coverage-py
.. _Configuration reference:
   https://coverage.readthedocs.io/en/6.3.2/config.html#configuration-reference
.. _Test Code Coverage:
   https://cpske.github.io/ISP/testing/code-coverage
.. _Python Sphinx exclude patterns:
   https://stackoverflow.com/a/43868129
.. _sphinx-apidoc:
   https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html


"""


import os
import sys

import shared
import databaseobject


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
    database = databaseobject.ConnectionDB()
    result = database.query("""SELECT * from bicycles""")
    print("BRAND: {}".format(result[0]['brand']))

    # escaped_string = database.escape_string("Bob's Overdrive")
    # print(escaped_string)



main()
