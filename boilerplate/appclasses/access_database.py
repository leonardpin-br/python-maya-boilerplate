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
from databaseobject.connection_db import ConnectionDB


class Bicycle(object):

    # ----- START OF ACTIVE RECORD CODE -----
    database = ConnectionDB()
    """An instance of ConnectionDB.

    References:
        `Static class variables and methods in Python`_

    .. _Static class variables and methods in Python:
        https://stackoverflow.com/a/68672
    """

    @staticmethod
    def set_database(database):
        u"""Not implemented.

        Creating an instance of ConnectionDB (outside any method) allows the use
        of the required functions.

        This static method would inform this class about the connection with the
        database.

        Args:
            database (MySQLConnection): The connection with the database.

        References:
            `How to Use the Magical @staticmethod, @classmethod, and @property Decorators in Python`_

        .. _How to Use the Magical @staticmethod, @classmethod, and @property Decorators in Python:
           https://betterprogramming.pub/how-to-use-the-magical-staticmethod-classmethod-and-property-decorators-in-python-e42dd74e51e7
        """
        pass

    # ----- START OF ACTIVE RECORD CODE -----

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

            `How To Check If A Key in **kwargs Exists?`_

        .. _How can you set class attributes from variable arguments (kwargs) in python:
           https://stackoverflow.com/a/8187408
        .. _Python - Public, Protected, Private Members:
           https://www.tutorialsteacher.com/python/public-private-protected-modifiers
        .. _How To Check If A Key in **kwargs Exists?:
           https://stackoverflow.com/a/12399836

        """

        # Public properties:
        self.brand = kwargs['brand'] if 'brand' in kwargs else ''
        self.model_make = kwargs['model_make'] if 'model_make' in kwargs else ''
        self.year_make = kwargs['year_make'] if 'year_make' in kwargs else 0
        self.category_make = kwargs['category_make'] if 'category_make' in kwargs else ''
        self.color_make = kwargs['color_make'] if 'color_make' in kwargs else ''
        self.description = kwargs['description'] if 'description' in kwargs else ''
        self.gender = kwargs['gender'] if 'gender' in kwargs else ''
        self.price = kwargs['price'] if 'price' in kwargs else 0

        # Protected properties:
        self._weight_kg = kwargs['weight_kg'] if 'weight_kg' in kwargs else 0.0
        self._condition_id = kwargs['condition_id'] if 'condition_id' in kwargs else 3

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

    @property
    def weight_lbs(self):
        result = self._weight_kg * 2.2046226218
        formatted_str = "{weight_lbs} lbs".format(weight_lbs=shared.number_format(result, 2))
        return formatted_str

    @weight_lbs.setter
    def weight_lbs(self, value):
        self._weight_kg = value / 2.2046226218

    def condition(self):
        if self.condition_id > 0:
            return self.CONDITION_OPTIONS[self.condition_id]
        else:
            return "Unknown"
