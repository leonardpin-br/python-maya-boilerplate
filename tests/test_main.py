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

for mod in maya_modules:
    sys.modules[mod] = mock.MagicMock()

currentdir = os.path.dirname(os.path.realpath(__file__))    # tests
rootdir = os.path.dirname(currentdir)                       # Boilerplate (root)
boilerplate_dir = os.path.join(rootdir, "boilerplate")

sys.path.append(boilerplate_dir)

import main


class mainTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_greeter(self):
        self.assertTrue(main.print_sys_path())
