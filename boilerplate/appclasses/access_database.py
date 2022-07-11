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
    'Bicycle',
    'Admin'
]
__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__link__ = u"https://www.leonardopinheiro.net"

import decimal
import re

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
    _password_required = True

    def __init__(self, **kwargs):
        u"""Creates an instance of Admin.

        Args:
            **kwargs: Keyword arguments with the admin properties.
        """

        super(Admin, self).__init__()

        # Public instance properties:
        self.id = kwargs['id'] if 'id' in kwargs else 0
        self.first_name = kwargs['first_name'] if 'first_name' in kwargs else None
        self.last_name = kwargs['last_name'] if 'last_name' in kwargs else None
        self.email = kwargs['email'] if 'email' in kwargs else None
        self.username = kwargs['username'] if 'username' in kwargs else None
        self.password = kwargs['password'] if 'password' in kwargs else None
        self.confirm_password = kwargs['confirm_password'] if 'confirm_password' in kwargs else None

        self.hashed_password = None

    def set_hashed_password(self, value):
        # Maya cannot load the .pyd file from BCrypt.
        # <project_root>/py27env/Lib/site-packages/bcrypt/_bcrypt.pyd
        # But, outside of Maya, the line below works OK.
        # self.hashed_password = shared.password_hash(value)
        self.hashed_password = value

    def verify_password(self, password):
        return shared.password_verify(password, self.hashed_password)

    def full_name(self):
        return "{self.first_name} {self.last_name}".format(self=self)

    def _create(self):
        self.set_hashed_password(self.password)
        return super(Admin, self)._create()

    def _update(self):

        # If the user is being updated, but the password is not, it will
        # allow updating the record, skipping the validation.
        # If it comes from a form (like an UI) and the password field is
        # empty, the validation will be skipped.
        if self.password != '':
            self.set_hashed_password(self.password)
            # Validate password.
        else:
            # Password not being updated, skip hashing and validation.
            self._password_required = False
        return super(Admin, self)._update()

    def _validate(self):
        self.errors = []

        if shared.is_blank(self.first_name):
            self.errors.append('First name cannot be blank.')
        elif not shared.has_length(self.first_name, {'min': 2, 'max': 255}):
            self.errors.append('First name must be between 2 and 255 characters.')

        if shared.is_blank(self.last_name):
            self.errors.append('Last name cannot be blank.')
        elif not shared.has_length(self.last_name, {'min': 2, 'max': 255}):
            self.errors.append('Last name must be between 2 and 255 characters.')

        if shared.is_blank(self.email):
            self.errors.append('Email cannot be blank.')
        elif not shared.has_length(self.email, {'max': 255}):
            self.errors.append('Email must be less than 255 characters.')
        elif not shared.has_valid_email_format(self.email):
            self.errors.append('Email must be a valid format.')

        if shared.is_blank(self.username):
            self.errors.append('Username cannot be blank.')
        elif not shared.has_length(self.username, {'min': 8, 'max': 255}):
            self.errors.append('Username must be between 8 and 255 characters.')
        elif not Admin.has_unique_username(self.username, self.id if self.id > 0 else 0):
            self.errors.append('Username not allowed. Try another.')

        if self._password_required:
            if shared.is_blank(self.password):
                self.errors.append('Password cannot be blank.')
            elif not shared.has_length(self.password, {'min': 12}):
                self.errors.append('Password must contain 12 or more characters.')
            elif not re.search(r"[A-Z]", self.password):
                self.errors.append('Password must contain at least 1 uppercase letter.')
            elif not re.search(r"[a-z]", self.password):
                self.errors.append('Password must contain at least 1 lowercase letter.')
            elif not re.search(r"[0-9]", self.password):
                self.errors.append('Password must contain at least 1 number.')
            elif not re.search(r"[^A-Za-z0-9\s]", self.password):
                self.errors.append('Password must contain at least 1 symbol.')

            if shared.is_blank(self.confirm_password):
                self.errors.append('Confirm password cannot be blank.')
            elif self.password != self.confirm_password:
                self.errors.append('Password and confirm password must match.')

        return self.errors

    @classmethod
    def find_by_username(cls, username):

        sql = "SELECT * FROM " + cls._table_name + " "
        sql += "WHERE username='{username}'".format(username=cls._database.escape_string(username))
        object_list = cls.find_by_sql(sql)

        # Checks if the list is NOT empty (does not need the "not" keyword).
        if object_list:
            return object_list[0]
        else:
            return False

    @classmethod
    def has_unique_username(cls, username, current_id="0"):
        admin = cls.find_by_username(username)
        if not admin or admin.id == current_id:
            # Is unique.
            return True
        else:
            # Not unique.
            return False