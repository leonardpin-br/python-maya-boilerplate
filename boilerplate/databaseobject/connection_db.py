# -*- coding: utf-8 -*-

__all__ = ['ConnectionDB']
__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__link__ = u"https://www.leonardopinheiro.net"


import database_functions


class ConnectionDB(object):
    u"""Mimics (loosely and in a very crud way) the mysqli (PHP) class.

    This class was built to access MySQL databases and depends on
    ``mysql.connector`` (mysql-connector-python==8.0.22) to execute queries.

    Warning:
        It is very important to **use a virtual environment.**

        It is also important to install the right version of
        mysql-connector-python to use with Autodesk Maya 2020 and below (see
        the reference)::

            $ pip install mysql-connector-python==8.0.22

        If the mysql-connector-python installed is not of the right version, it
        will not work for accessing the database and will also create
        an error in Sphinx build process that is hard to track.

    References:
        `How do I connect to a MySQL Database in Python?`_

        `Python and MySQL Error\: No module named mysql`_

        `3.7.4. Admonitions`_

    .. _How do I connect to a MySQL Database in Python?:
       https://stackoverflow.com/a/20959654
    .. _Python and MySQL Error\: No module named mysql:
       https://sebhastian.com/no-module-named-mysql/
    .. _3.7.4. Admonitions:
       https://sphinx-rtd-theme.readthedocs.io/en/stable/demo/demo.html#admonitions

    """

    affected_rows = 0
    insert_id = 0

    def __init__(self):
        self.connection_db = database_functions.db_connect()

    def query(self, sql):
        u"""Performs a query on the database

        Args:
            sql (str): The query to be executed

        Returns:
            list[dict]: A list of dictionaries with all records or an empty
            list.

        References:
            `10.6.4 cursor.MySQLCursorDict Class`_

        .. _10.6.4 cursor.MySQLCursorDict Class:
           https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursordict.html
        """
        try:
            cursor = self.connection_db.cursor(dictionary=True)
            cursor.execute(sql)
            self.affected_rows = cursor.rowcount
            self.insert_id = cursor.lastrowid
            result = cursor.fetchall()
            cursor.close()

        finally:
            self.connection_db.close()

        return result

    def escape_string(self, string_to_escape):
        u"""Roughly does the same as the ``mysqli::real_escape_string`` method,
        that is, escapes a string. It is meant to be used before sending it to
        the database.

        Args:
            string_to_escape (str): The string to be escaped.

        Returns:
            str: The escaped string.

        References:

            `Escaping strings with python mysql.connector`_

        .. _Escaping strings with python mysql.connector:
           https://stackoverflow.com/a/32124096/3768670

        """
        return self.connection_db.converter.escape(string_to_escape)
