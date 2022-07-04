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

import shared
from shared import constant


class Bicycle(object):

    @constant
    def CATEGORIES():
        u"""You cannot declare a variable or value as constant in Python.

        To indicate to programmers that a variable is a constant, one usually
        writes it in upper case.

        If the behaviour of a constant is needed, the decorator ``@constant``
        (created in the ``shared.functions.constant`` function) should be used.

        References:
            `How do I create a constant in Python?`_

        .. _How do I create a constant in Python?:
        https://stackoverflow.com/a/2688086

        """
        return ['Road', 'Mountain', 'Hybrid', 'Cruiser', 'City', 'BMX']

    @constant
    def GENDERS():
        return ['Mens', 'Womens', 'Unisex']

    @constant
    def CONDITION_OPTIONS():
        return {
            1: 'Beat up',
            2: 'Decent',
            3: 'Good',
            4: 'Great',
            5: 'Like New'
        }

    def __init__(self, **kwargs):
        u"""Creates an instance of Bicycle.

        Args:
            **kwargs: Keyword arguments with the bicycle properties.

        References:
            `How can you set class attributes from variable arguments (kwargs) in python`_

            `Python - Public, Protected, Private Members`_

        .. _How can you set class attributes from variable arguments (kwargs) in python:
        https://stackoverflow.com/a/8187408
        .. _Python - Public, Protected, Private Members:
        https://www.tutorialsteacher.com/python/public-private-protected-modifiers

        """

        # Public properties:
        # self.brand = ''
        # self.model_make = ''
        # self.year_make = 0
        # self.category_make = ''
        # self.color_make = ''
        # self.description = ''
        # self.gender = ''
        # self.price = 0.0

        # Protected attributes:
        self._weight_kg = 0.0
        self._condition_id = 0

        # allowed_keys = {'brand', 'model_make', 'year_make', 'category_make',
        #                 'color_make', 'description', 'gender', 'price'}
        # self.__dict__.update((k, v)
        #                      for k, v in kwargs.items() if k in allowed_keys)

        # Public properties:
        self.brand = kwargs['brand'] if shared.is_set(kwargs['brand']) else ''
        self.model_make = kwargs['model_make'] if shared.is_set(kwargs['model_make']) else ''
        self.year_make = kwargs['year_make'] if shared.is_set(kwargs['year_make']) else 0
        self.category_make = kwargs['category_make'] if shared.is_set(kwargs['category_make']) else ''
        self.color_make = kwargs['color_make'] if shared.is_set(kwargs['color_make']) else ''
        self.description = kwargs['description'] if shared.is_set(kwargs['description']) else ''
        self.gender = kwargs['gender'] if shared.is_set(kwargs['gender']) else ''
        self.price = kwargs['price'] if shared.is_set(kwargs['price']) else 0
        self.weight_kg = kwargs['weight_kg'] if shared.is_set(kwargs['weight_kg']) else 0.0

        # TODO
        # This should be optional.
        self.condition_id = kwargs['condition_id'] if shared.is_set(kwargs['condition_id']) else "Value is not set!!"


    @property
    def weight_kg(self):
        return "{formatted_number} Kg".format(formatted_number=shared.number_format(self._weight_kg, 2))

    @weight_kg.setter
    def weight_kg(self, value):
        self._weight_kg = value
        return self._weight_kg

    @property
    def condition_id(self):
        return self._condition_id

    @condition_id.setter
    def condition_id(self, value):
        self._condition_id = value
        return self._condition_id