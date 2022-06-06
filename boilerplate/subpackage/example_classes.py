# -*- coding: utf-8 -*-
u"""An example superclass to show inheritance and documentation.

This superclass is only an example to serve as a reference or be deleted.

Last modified in 2022-04-25

Python version 2.7.11 (Maya 2020)

Example:
    This is how to write **bold**, `italic`, *italic* and ``code`` text.

Unit tests:
    This is how unit tests are run::

        $ python -m unittest discover

References:
    `PEP 484`_

    `Python docstring rendering\: reStructuredText markup inside directives not recognized`_

.. _PEP 484:
   https://www.python.org/dev/peps/pep-0484/
.. _Python docstring rendering\: reStructuredText markup inside directives not recognized:
   https://youtrack.jetbrains.com/issue/PY-40010

"""

__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__link__ = u"https://www.leonardopinheiro.net"


__all__ = [
    'ExampleSuperclass',
    'ExampleSubclass'
]


class ExampleSuperclass(object):
    u"""Example of a superclass.
    """

    def __init__(self, any_number=10):
        u"""Creates an instance of ExampleSuperclass.

        Args:
            any_number (int, optional): An example of parameter. Defaults to 10.
        """

        self.any_number = any_number
        u"""int: Example of a **public** property."""

    def return_message(self):
        u"""Returns an example message.

        Returns:
            str: An example message.
        """
        return u"The constructor of the superclass received the number: {self.any_number}.".format(self=self)


class ExampleSubclass(ExampleSuperclass):
    u"""Creates an instance of the example subclass."""

    def __init__(self, any_number=10):
        super(ExampleSubclass, self).__init__(any_number)

    def greeter(self):
        u"""Returns a greeting to the user.

        Returns:
            str: The greeting message.
        """
        return u"Hello from subclass!"
