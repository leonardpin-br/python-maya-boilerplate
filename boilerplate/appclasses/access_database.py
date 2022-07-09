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

    _db_columns = ['id', 'brand', 'model', 'year', 'category', 'color',
                   'gender', 'price', 'weight_kg', 'condition_id', 'description']

    errors = []

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
            (list[obj] | False): List containing objects from the query result.
            False if it does not find anything.

        References:
            `How to check if a list is empty in python?`_

        .. _How to check if a list is empty in python?:
           https://flexiple.com/check-if-list-is-empty-python/#section2

        """

        result = cls._database.query(sql)

        # If the resulting list is empty:
        if not result:
            shared.print_error_message(
                'Database query failed. The resulting list is empty.')
            return False

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

    def _validate(self):
        u"""Every class that extends this one (DatabaseObject) must implement
        this method.

        Returns:
            list[str]: The errors string list.
        """

        self.errors = []

        if shared.is_blank(self.brand):
            self.errors.append("Brand cannot be blank.")

        if shared.is_blank(self.model):
            self.errors.append("Model cannot be blank.")

        return self.errors

    def _create(self):
        u"""Creates a record in the database with the properties' values of the
        current instance in memory.

        Returns:
            (list[dict] | list[] | bool): The result of the **query()** method
            executed inside this method.

        References:
            `How to Convert a List to String in Python`_

            `Last Key in Python Dictionary`_

            `Python add item to the tuple`_

            `Prepared Statements`_

            `How to check if a list is empty in python?`_

        .. _How to Convert a List to String in Python:
           https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python#how_to_convert_a_list_to_string_in_python
        .. _Last Key in Python Dictionary:
           https://stackoverflow.com/a/16125237
        .. _Python add item to the tuple:
           https://stackoverflow.com/a/16730584
        .. _Prepared Statements:
           https://www.php.net/manual/en/mysqli.quickstart.prepared-statements.php
        .. _How to check if a list is empty in python?:
           https://flexiple.com/check-if-list-is-empty-python/
        """

        self._validate()
        if self.errors:
            return False

        attributes = self._sanitized_attributes()

        # Prepared statement, stage 1: prepare
        # ----------------------------------------------------------------------
        temporary_list = []
        sql = "INSERT INTO bicycles ("

        # Loops through the dictionary:
        for key in attributes:
            sql += key
            temporary_list.append(attributes[key])

            # If it is the last key in the dictionary:
            if key == attributes.keys()[-1]:
                break

            sql += ", "

        sql += ") VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        data = tuple(temporary_list)

        # Prepared statement, stage 2: bind and execute happen inside query().
        # ----------------------------------------------------------------------
        result = self._database.query(sql, values=data)
        if result:
            self.id = self._database.insert_id

        return result

    def _update(self):
        u"""Updates the database with the properties' values of the current
        instance in memory.

        Returns:
            bool: The result of the query() method executed inside this
            method. True if the update is successful. False otherwise.

        References:
            `How to Convert a List to String in Python`_

        .. _How to Convert a List to String in Python:
           https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python#how_to_convert_a_list_to_string_in_python
        """

        self._validate()
        if self.errors:
            return False

        attributes = self._sanitized_attributes()
        key_list = []
        value_list = []

        # Loops through the dictionary:
        for key, value in attributes.items():
            key_list.append("{key}=%s".format(key=key))
            value_list.append(value)

        sql = "UPDATE bicycles SET "
        sql += ", ".join(key_list)
        sql += " WHERE id=%s "
        sql += "LIMIT 1"

        # Appends the ID at the end of the value_list.
        value_list.append(self.id)
        data = tuple(value_list)

        result = self._database.query(sql, values=data)
        return result

    def save(self):
        u"""Executes the update() or the create() instance methods based on the
        presence of an ID.

        Returns:
            (list[dict] | list[] | bool): Returns the same as the instance
            method that was executed.
        """

        if self.id > 0:
            return self._update()
        return self._create()

    def merge_attributes(self, **kwargs):
        u"""Merges the attributes from the given dictionary into the object in
        memory created from the findById() method.

        Args:
            **kwargs: The dictionary containing the new values to be merged and later updated.

        Example:
            How to call this method::

                    bike = Bicycle.find_by_id(26)

                    if bike:
                        kwargs = {
                            "id": bike.id,
                            "brand": bike.brand,
                            "model": "Bob's Overdrive", # bike.model
                            "year": bike.year,
                            "category": bike.category,
                            "gender": bike.gender,
                            "color": bike.color,
                            "weight_kg": bike.weight_kg,
                            "condition": bike.condition,
                            "price": bike.price
                        }

                        bike.merge_attributes(**kwargs)
                        result = bike.update()
                        if result:
                            print("The bicycle was updated.")
                        else:
                            print("There was an error in the update process.")
                    else:
                        print("The ID was not found.")
        """

        for key, value in kwargs.items():
            if hasattr(self, key) and not shared.is_none(value):
                setattr(self, key, value)

    def attributes(self):
        u"""Creates a dictionary that have, as properties, the database columns
        (excluding ID) and the corresponding values from the instance object in
        memory.

        Returns:
            dict: Dictionary containing the names of the columns and the
            corresponding values from the instance object in memory.

        References:
            `Add Key to a Python Dictionary`_

            `Python Break and Continue: Step-By-Step Guide`_

            `How to dynamically access class properties in Python?`_

        .. _Add Key to a Python Dictionary:
           https://stackabuse.com/python-how-to-add-keys-to-dictionary/#addkeytoapythondictionary
        .. _Python Break and Continue\: Step-By-Step Guide:
           https://careerkarma.com/blog/python-break-and-continue/
        .. _How to dynamically access class properties in Python?:
           https://stackoverflow.com/a/2425281
        """

        attributes = {}
        for column in self._db_columns:
            if column == 'id':
                continue
            attributes[column] = getattr(self, column)

        return attributes

    def _sanitized_attributes(self):
        u"""Sanitizes (escapes the values) of the object before sending to the
        database.

        Returns:
            dict: Dictionary with the values escaped.

        References:
            `Python - Loop Dictionaries`_

        .. _Python - Loop Dictionaries:
           https://www.w3schools.com/python/python_dictionaries_loop.asp
        """

        sanitized = {}
        attributes = self.attributes()
        for key, value in attributes.items():
            sanitized[key] = self._database.escape_string(value)

        return sanitized

    def delete(self):
        u"""Deletes, in the database, the record that corresponds to the current
        instance object in memory.

        After deleting, the instance of the object will still exist, even though
        the database record does not. This can be useful, as in the example
        below.

        Returns:
            (False | obj): The return value will be:
            An object with information provided by MySQL.
            False if there is no answer.

        Example:
            This is how it can be used::

                print("{user.first_name} was deleted.".format(user=user))
                # But, for example, we can't call user.update() after
                # calling user.delete().
        """

        sql = "DELETE FROM bicycles "
        sql += "WHERE id=%s "
        sql += "LIMIT 1"

        data = (self.id, )

        result = self._database.query(sql, values=data)

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
        self.weight_kg = decimal.Decimal(
            kwargs['weight_kg']) if 'weight_kg' in kwargs else 0.0
        self.condition_id = kwargs['condition_id'] if 'condition_id' in kwargs else 3

    def name(self):
        return "{brand} {model} {year}".format(brand=self.brand, model=self.model, year=self.year)

    # @property
    # def weight_kg(self):
    #     # return "{formatted_number} Kg".format(formatted_number=shared.number_format(self.weight_kg, 2))
    #     return decimal.Decimal(self.weight_kg)

    # @weight_kg.setter
    # def weight_kg(self, value):
    #     self.weight_kg = value
    #     return self.weight_kg

    # @property
    # def condition_id(self):
    #     return self.condition_id

    # @condition_id.setter
    # def condition_id(self, value):
    #     self.condition_id = value
    #     return self.condition_id

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
