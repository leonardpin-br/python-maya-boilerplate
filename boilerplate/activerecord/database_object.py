# -*- coding: utf-8 -*-

__all__ = [
    'DatabaseObject'
]
__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__link__ = u"https://www.leonardopinheiro.net"

# If Python >= 3.4:
try:
    from abc import ABC, abstractmethod
# If Python 2:
except ImportError:
    from abc import ABCMeta, abstractmethod

import shared
from connection_db import ConnectionDB


class DatabaseObject(object):
    u"""Abstract superclass to be instantiated from all the others that access
    the database.

    Last modified in 2022-07-09

    Python version 2.7.11 (Maya 2018 and 2020)

    References:
        `Conditional import of modules in Python`_

        `Is it possible to make abstract classes in Python?`_

    .. _Conditional import of modules in Python:
       https://stackoverflow.com/a/3496790
    .. _Is it possible to make abstract classes in Python?:
       https://stackoverflow.com/a/13646263

    """

    # Allows the creation of abstract classes.
    __metaclass__ = ABCMeta

    # ----- START OF ACTIVE RECORD CODE -----

    _database = ConnectionDB()
    u"""activerecord.connection_db.ConnectionDB: Holds the connection
    information used by static methods.

    References:
        `Static class variables and methods in Python`_

    .. _Static class variables and methods in Python:
       https://stackoverflow.com/a/68672
    """

    _table_name = ""
    _db_columns = []
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

        sql = "SELECT * FROM " + cls._table_name
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

        sql = "SELECT * FROM " + cls._table_name + " "
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

    @abstractmethod
    def _validate(self):
        u"""Every class that extends this one (DatabaseObject) must implement
        this method.

        Returns:
            list[str]: The errors string list.

        References:
            `Is it possible to make abstract classes in Python?`_

        .. _Is it possible to make abstract classes in Python?:
           https://stackoverflow.com/a/13646263
        """

        pass

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
        sql = "INSERT INTO " + self._table_name + " ("

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

        sql = "UPDATE " + self._table_name + " SET "
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

        sql = "DELETE FROM " + self._table_name + " "
        sql += "WHERE id=%s "
        sql += "LIMIT 1"

        data = (self.id, )

        result = self._database.query(sql, values=data)

        return result

    # ----- END OF ACTIVE RECORD CODE -----
