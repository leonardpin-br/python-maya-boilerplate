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

import decimal

import shared
from shared import constant
from activerecord.database_object import DatabaseObject


class Bicycle(DatabaseObject):

    _table_name = "bicycles"
    _db_columns = ['id', 'brand', 'model', 'year', 'category', 'color',
                   'gender', 'price', 'weight_kg', 'condition_id', 'description']

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

        super(Bicycle, self).__init__()

        # Public properties:
        self.id = kwargs['id'] if 'id' in kwargs else 0
        self.brand = kwargs['brand'] if 'brand' in kwargs else ''
        self.model = kwargs['model'] if 'model' in kwargs else ''
        self.year = kwargs['year'] if 'year' in kwargs else 0
        self.category = kwargs['category'] if 'category' in kwargs else ''
        self.color = kwargs['color'] if 'color' in kwargs else ''
        self.description = kwargs['description'] if 'description' in kwargs else ''
        self.gender = kwargs['gender'] if 'gender' in kwargs else ''
        self.price = kwargs['price'] if 'price' in kwargs else 0
        self.weight_kg = decimal.Decimal(
            kwargs['weight_kg']) if 'weight_kg' in kwargs else 0.0
        self.condition_id = kwargs['condition_id'] if 'condition_id' in kwargs else 3

    def name(self):
        return "{brand} {model} {year}".format(brand=self.brand, model=self.model, year=self.year)

    def get_weight_kg(self):
        return "{formatted_number} Kg".format(formatted_number=shared.number_format(self.weight_kg, 2))

    @property
    def weight_lbs(self):
        # https://stackoverflow.com/a/21418696
        result = self.weight_kg * decimal.Decimal(2.2046226218)
        formatted_str = "{weight_lbs} lbs".format(
            weight_lbs=shared.number_format(result, 2))
        return formatted_str

    @weight_lbs.setter
    def weight_lbs(self, value):
        # https://stackoverflow.com/a/21418696
        self.weight_kg = value / decimal.Decimal(2.2046226218)

    def condition(self):
        if self.condition_id > 0:
            return self.CONDITION_OPTIONS[self.condition_id]
        else:
            return "Unknown"

    def _validate(self):

        self.errors = []

        if shared.is_blank(self.brand):
            self.errors.append("Brand cannot be blank.")

        if shared.is_blank(self.model):
            self.errors.append("Model cannot be blank.")

        return self.errors


class Admin(DatabaseObject):

    _table_name = "admins"
    _db_columns = ['id', 'first_name', 'last_name', 'email', 'username',
                   'hashed_password']

    def __init__(self, **kwargs):
        u"""Creates an instance of Admin.

        Args:
            **kwargs: Keyword arguments with the admin properties.
        """

        super(Admin, self).__init__()

        # Public instance properties:
        self.id = kwargs['id'] if 'id' in kwargs else 0
        self.first_name = kwargs['first_name'] if 'first_name' in kwargs else ''
        self.last_name = kwargs['last_name'] if 'last_name' in kwargs else ''
        self.email = kwargs['email'] if 'email' in kwargs else ''
        self.username = kwargs['username'] if 'username' in kwargs else ''
        self.password = kwargs['password'] if 'password' in kwargs else ''
        self.confirm_password = kwargs['confirm_password'] if 'confirm_password' in kwargs else ''

        # Protected instance property:
        self._hashed_password = ''

    @property
    def hashed_password(self):
        return self._hashed_password

    @hashed_password.setter
    def hashed_password(self, value):
        self._hashed_password = shared.password_hash(value)

    def full_name(self):
        return "{self.first_name} {self.last_name}".format(self=self)

    def _create(self):
        self.hashed_password = self.password
        return super(Admin, self)._create()

    def _update(self):
        self._set_hashed_password()
        return super(Admin, self)._update()

    def _validate(self):
        pass