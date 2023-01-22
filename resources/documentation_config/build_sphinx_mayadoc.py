#! /usr/bin/env python2
# -*- coding: utf-8 -*-
u"""Serves as a configuration file to Sphinx to work with Maya 2020 modules.

There are more explanations on how to use it on the README.md file.

Warning:
    The Shebang Line appears to have no practical effect, at least on Windows,
    in the ``<project_root>/resources/documentation_config/build_sphinx_mayadoc.py``
    file even with the ``.py`` files associated with the launcher
    (``C:\\Windows\\pyw.exe``).

    To make this script a little bit more portable, the shebang line is:

        #! /usr/bin/env python2


    The use of the **mayapy** command, inside the ``make.bat`` file, makes all
    the difference in the execution of the documentation generation.

References:
    `Getting Sphinx to work with Maya modules`_

    `How Should I Set Default Python Version In Windows?`_

    `unable to run 'aws' from cygwin`_

    `Find full path of the Python interpreter?`_

    `How to force Sphinx to use Python 3.x interpreter`_

    `Standalone Maya Python Interpreter`_

    `Could not import extension sphinxcontrib.napoleon #10378`_

    `3.7 Shebang Line`_

    `Should I put #! (shebang) in Python scripts, and what form should it take?`_

.. _Getting Sphinx to work with Maya modules:
   https://geektalker.wordpress.com/2013/03/26/getting-sphinx-to-work-with-maya-modules/
.. _How Should I Set Default Python Version In Windows?:
   https://stackoverflow.com/a/52913040/3768670
.. _unable to run \'aws\' from cygwin:
   https://stackoverflow.com/a/62093489/3768670
.. _Find full path of the Python interpreter?:
   https://stackoverflow.com/a/2589722/3768670
.. _How to force Sphinx to use Python 3.x interpreter:
   https://stackoverflow.com/a/40638825/3768670
.. _Standalone Maya Python Interpreter:
   https://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/PyMel/standalone.html#standalone-maya-python-interpreter
.. _Could not import extension sphinxcontrib.napoleon #10378:
   https://github.com/sphinx-doc/sphinx/issues/10378#issuecomment-1107455569
.. _3.7 Shebang Line:
   https://google.github.io/styleguide/pyguide.html#37-shebang-line
.. _Should I put #! (shebang) in Python scripts, and what form should it take?:
   https://stackoverflow.com/a/14599026/3768670
"""


import os
import sys

# Gets the full path of this script file dinamically.
THIS_FILE_DIR = os.path.realpath(os.path.dirname(__file__))

# Gets the full path of the project's root folder:
pathList = THIS_FILE_DIR.split("\\")
pathList = pathList[:-2]
project_root = "\\".join(pathList)

# Builds the path to the Sphinx's directory (inside the virtual environment):
sphinx_dir = os.path.join(project_root, "py27env", "Lib", "site-packages")

# If the path is not in sys.path:
for path in sys.path:
    if path == sphinx_dir:
        break
else:
    sys.path.insert(0, sphinx_dir)

import sphinx

import maya.standalone
maya.standalone.initialize(name='python')

if __name__ == '__main__':

    # sys.argv is a list containing the name of the script being executed
    # and all the arguments passed. The first item is the name of the script.
    # Below is the entire sys.argv list passed to this file by Sphinx:
    # ['E:/cloud/Videoaulas/Digital Tutors - Procedural Rigging with Python in Maya/procedural_rigging/resources/documentation_config/build_sphinx_mayadoc.py', '-M', 'clean', 'source', 'build']
    # The line below skips the first item.
    argv = sys.argv[1:]

    # The insert() method inserts the specified value at the specified position.
    argv.insert(0, sphinx.__file__.replace("\\", "/"))

    sphinx.main(argv)
