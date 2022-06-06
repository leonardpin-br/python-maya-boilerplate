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

currentdir = os.path.dirname(os.path.realpath(__file__))    # subpackage
testsdir = os.path.dirname(currentdir)
rootdir = os.path.dirname(testsdir)                       # Boilerplate (root)
boilerplate_dir = os.path.join(rootdir, "boilerplate")

sys.path.append(boilerplate_dir)
sys.path.append(os.path.join(boilerplate_dir, "subpackage"))

import subpackage


class ExampleSubclassTest(unittest.TestCase):

    def setUp(self):
        self.object = subpackage.example_classes.ExampleSubclass()

    def tearDown(self):
        pass

    def test_greeter(self):
        expected = u"Hello from subclass!"
        result = self.object.greeter()
        self.assertEqual(expected, result)

    @unittest.skip(u"demonstrating skipping")
    def test_does_nothing(self):
        self.fail()
