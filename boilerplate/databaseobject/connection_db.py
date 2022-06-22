# -*- coding: utf-8 -*-

__all__ = ['ConnectionDB']
__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__link__ = u"https://www.leonardopinheiro.net"

import re

import database_functions


class ConnectionDB(object):
    u"""Mimics (loosely and in a very crud way) the mysqli (PHP) class.

    This class was built to access MySQL databases and depends on
    ``mysql.connector`` (mysql-connector-python==8.0.22) to execute queries.

    Note:
        It is very, very, very important to **use a virtual environment.**

        It is also important to install the right version of
        mysql-connector-python to use with Autodesk Maya 2020 and below (see
        the reference)::

            pip install mysql-connector-python==8.0.22

        If the mysql-connector-python installed is not of the right version, it
        will not work for accessing the database and will also create
        an error in Sphinx build process that is hard to track.

    References:
        `How do I connect to a MySQL Database in Python?`_

        `Python and MySQL Error\: No module named mysql`_

    .. _How do I connect to a MySQL Database in Python?:
       https://stackoverflow.com/a/20959654
    .. _Python and MySQL Error\: No module named mysql:
       https://sebhastian.com/no-module-named-mysql/

    """

    affected_rows = 0
    insert_id = 0

    def __init__(self):
        self.connection_db = database_functions.db_connect()

    def query(self, sql):
        try:
            cursor = self.connection_db.cursor()
            cursor.execute(sql)
            self.affected_rows = cursor.rowcount
            self.insert_id = cursor.lastrowid
            result = cursor.fetchall()

        finally:
            self.connection_db.close()

        return result

    def escape_string(self, string_to_escape):
        """https://stackoverflow.com/questions/15798969/python-mysql-escape-special-characters

        Args:
            string_to_escape (_type_): _description_
        """
        pass
