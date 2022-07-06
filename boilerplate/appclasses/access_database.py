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
from databaseobject.connection_db import ConnectionDB


class Bicycle(object):

    # ----- START OF ACTIVE RECORD CODE -----
    _database = ConnectionDB()
    u"""databaseobject.connection_db.ConnectionDB: Holds the connection
    information used by static methods.

    References:
        `Static class variables and methods in Python`_

    .. _Static class variables and methods in Python:
       https://stackoverflow.com/a/68672
    """

    @classmethod
    def set_database(cls, database):
        u"""**Not implemented.**

        Setting the value of ``_database`` (receiving an instance of
        ``ConnectionDB``) outside any methods make that property a static
        property.

        This allows the use of the required class methods. There is no need for
        using this method outside this class.

        This class method would inform this class about the connection with the
        database.

        Args:
            database (MySQLConnection): The connection with the database.

        References:
            `How to Use the Magical @staticmethod, @classmethod, and @property Decorators in Python`_

        .. _How to Use the Magical @staticmethod, @classmethod, and @property Decorators in Python:
           https://betterprogramming.pub/how-to-use-the-magical-staticmethod-classmethod-and-property-decorators-in-python-e42dd74e51e7
        """
        pass

    @classmethod
    def find_by_sql(cls, sql):
        u"""Sends the SQL query to the database and returns a list of objects.

        Args:
            sql (str): The SQL string to be executed.

        Returns:
            list[obj]: List containing objects from the query result.

        """

        result = cls._database.query(sql, read=True)

        # If the resulting list is empty:
        if not result:
            shared.print_error_message('Database query failed.')
            raise

        # results into objects
        object_list = []
        for record in result:
            object_list.append(cls._instantiate(record))

        return object_list

    @classmethod
    def find_all(cls):
        u"""Finds all records in the given database table.

        Returns:
            list[obj]: List containing objects.

        References:
            `Class method vs static method in Python`_

        .. _Class method vs static method in Python:
           https://www.tutorialspoint.com/class-method-vs-static-method-in-python#
        """

        sql = "SELECT * FROM bicycles"
        return cls.find_by_sql(sql)

    @classmethod
    def find_by_id(cls, id):
        u"""Finds a record in the database, using the ID.

        Args:
            id (int): The ID number to be used in the query.

        Returns:
            (obj | False): An object corresponding to the database record. False
            if it does not find anything.

        References:
            `How to check if a list is empty in python?`_

        .. _How to check if a list is empty in python\?:
           https://flexiple.com/check-if-list-is-empty-python/#section2
        """

        sql = "SELECT * FROM bicycles "
        sql += "WHERE id='{id}'".format(id=cls._database.escape_string(id))
        object_list = cls.find_by_sql(sql)

        # Checks if the list is NOT empty (does not need the "not" keyword).
        if object_list:
            return object_list[0]
        else:
            return False

    @classmethod
    def _instantiate(cls, record):
        u"""Creates an instance of the class setting the properties with
        the values of the object passed as argument.

        Args:
            record (dict): A dictionary representing a record (row) in the
                result set.

        Returns:
            obj: An instance of the subclass.

        References:
            `Protected method in python [duplicate]`_

            `How to know if an object has an attribute in Python`_

            `Object does not support item assignment error`_

        .. _Protected method in python [duplicate]:
           https://stackoverflow.com/a/11483397
        .. _How to know if an object has an attribute in Python:
           https://stackoverflow.com/a/610893
        .. _Object does not support item assignment error:
           https://stackoverflow.com/a/8542369
        """

        # Creates an instance of the subclass.
        obj = cls()

        # Loops through the dictionary.
        for key, value in record.items():

            # Checks if the instance has the same attribute as the dictionary
            # key.
            if hasattr(obj, key):

                # Sets the object attribute with the value from the key.
                setattr(obj, key, value)

        return obj

    def create(self):
        sql = "INSERT INTO bicycles ("
        sql += "brand, model, year, category, color, gender, price, weight_kg, condition_id, description"
        sql += ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        data = (
            self.brand,
            self.model,
            self.year,
            self.category,
            self.color,
            self.gender,
            self.price,
            decimal.Decimal(self._weight_kg),
            self.condition_id,
            self.description
        )

        result = self._database.query(sql, values=data, create=True)
        if result:
            self.id = self._database.insert_id
        return result

    # ----- END OF ACTIVE RECORD CODE -----

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
        self.id = kwargs['id'] if 'id' in kwargs else 0
        self.brand = kwargs['brand'] if 'brand' in kwargs else ''
        self.model = kwargs['model'] if 'model' in kwargs else ''
        self.year = kwargs['year'] if 'year' in kwargs else 0
        self.category = kwargs['category'] if 'category' in kwargs else ''
        self.color = kwargs['color'] if 'color' in kwargs else ''
        self.description = kwargs['description'] if 'description' in kwargs else ''
        self.gender = kwargs['gender'] if 'gender' in kwargs else ''
        self.price = kwargs['price'] if 'price' in kwargs else 0

        # Protected properties:
        self._weight_kg = kwargs['weight_kg'] if 'weight_kg' in kwargs else 0.0
        self._condition_id = kwargs['condition_id'] if 'condition_id' in kwargs else 3

    def name(self):
        return "{brand} {model} {year}".format(brand=self.brand, model=self.model, year=self.year)

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
        # https://stackoverflow.com/a/21418696
        result = self._weight_kg * decimal.Decimal(2.2046226218)
        formatted_str = "{weight_lbs} lbs".format(
            weight_lbs=shared.number_format(result, 2))
        return formatted_str

    @weight_lbs.setter
    def weight_lbs(self, value):
        # https://stackoverflow.com/a/21418696
        self._weight_kg = value / decimal.Decimal(2.2046226218)

    def condition(self):
        if self.condition_id > 0:
            return self.CONDITION_OPTIONS[self.condition_id]
        else:
            return "Unknown"
