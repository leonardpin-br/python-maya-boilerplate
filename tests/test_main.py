# -*- coding: utf-8 -*-
u'''Generated by unittest-skeleton-generator.sh on 2022-07-19 at 15:42:08.
'''
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

# Creates the mocks.
for mod in maya_modules:
    sys.modules[mod] = mock.MagicMock()

# Automatically calculated by unittest-skeleton-generator.sh to easily import main.py:
# Gets the src_dir.
tests_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(tests_dir)
src_dir = os.path.join(root_dir, "src")

# Adds src_dir to sys.path if it is not already there:
for path in sys.path:
    if path == src_dir:
        break
else:
    sys.path.append(src_dir)

# Imports the <root_directory>/boilerplate/main.py module.
import main


class MainTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # # Covers untested_function.
    # def test_untested_function(self):
    #     pass

    # Covers main.
    def test_main(self):
        expected = "hello"
        result = main.main()
        self.assertEqual(expected, result)


