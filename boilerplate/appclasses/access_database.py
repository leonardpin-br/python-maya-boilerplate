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

__all__ = [
    'Bicycle'
]
__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__link__ = u"https://www.leonardopinheiro.net"

from shared import constant


class Bicycle(object):

    brand = ''
    model_make = ''
    year_make = 0
    category_make = ''
    color_make = ''
    description = ''
    gender = ''
    price = 0.0

    @constant
    def CATEGORIES():
        return ['Road', 'Mountain', 'Hybrid', 'Cruiser', 'City', 'BMX']
    """You cannot declare a variable or value as constant in Python.

    To indicate to programmers that a variable is a constant, one usually writes
    it in upper case.
    """

    GENDERS = ['Mens', 'Womens', 'Unisex']

    def __init__(self, **kwargs):
        u"""Creates an instance of Bicycle.

        Args:
            **kwargs: Keyword arguments with the bicycle properties.

        References:
            `How can you set class attributes from variable arguments (kwargs) in python`_

        .. _How can you set class attributes from variable arguments (kwargs) in python:
        https://stackoverflow.com/a/8187408

        """

        allowed_keys = {'brand', 'model_make', 'year_make', 'category_make',
                        'color_make', 'description', 'gender', 'price'}
        self.__dict__.update((k, v)
                             for k, v in kwargs.items() if k in allowed_keys)



