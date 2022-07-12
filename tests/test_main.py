# -*- coding: utf-8 -*-
u"""Example unittest.

Rererences:
    `Recursive unittest discover`_

    `Importing modules from parent folder`_

.. _Recursive unittest discover:
   https://stackoverflow.com/questions/29713541/recursive-unittest-discover#answer-29715336
.. _Importing modules from parent folder:
   https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder#answer-11158224

"""
import os
import sys
import unittest
import mock

# Autodesk Maya modules that need to be mocked:
maya_modules = [
    'maya',
    'maya.app',
    'maya.app.general',
    'maya.app.general.mayaMixin',
    'cmds',
    'mel',
    'pymel',
    'pymel.core'
    'MayaQWidgetBaseMixin',
    'MayaQWidgetDockableMixin',
    'PySide2',
    'PySide2.QtUiTools',
    'QtWidgets',
    'QUiLoader'
]

# Creates a mock for every module in the maya_modules list.
for mod in maya_modules:
    sys.modules[mod] = mock.MagicMock()

# Adds the boilerplate folder to sys.path, if it not already there,
# so unit tests can see the modules:
currentdir = os.path.dirname(os.path.realpath(__file__))    # tests
rootdir = os.path.dirname(currentdir)                       # <root_directory>
boilerplate_dir = os.path.join(rootdir, "boilerplate")

for path in sys.path:
    if path == boilerplate_dir:
        break
else:
    sys.path.append(boilerplate_dir)

# Imports the <root_directory>/boilerplate/main.py module.
import main


class mainTest(unittest.TestCase):

    def setUp(self):
        self.obj = main.main()

    def tearDown(self):
        pass

    def test_greeter(self):
        expected = u"hello"
        result = self.obj
        self.assertEqual(expected, result)

    @unittest.skip(u"demonstrating skipping")
    def test_does_nothing(self):
        self.fail()
