# -*- coding: utf-8 -*-


__all__ = ['ConnectionDB']
__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__link__ = u"https://www.leonardopinheiro.net"


import shared
shared.add_site_packages_to_sys_path(__file__)
import database_functions

from mysql.connector import errorcode
import mysql.connector


class ConnectionDB(object):
    u"""Mimics (loosely and in a very crud way) the mysqli (PHP) class.

    This class was built to access MySQL databases and depends on
    ``mysql.connector`` (mysql-connector-python==8.0.22) to execute queries.

    Warning:
        It is very important to **use a virtual environment.**

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
        # There is error checking inside the db_connect() function.
        self.connection_db = database_functions.db_connect()

    def query(self, sql, values=None, create=False, read=False, update=False, delete=False):
        u"""Performs a query on the database.

        Args:
            sql (str): The query to be executed.
            values (tuple, optional): The values to complete the SQL statement.
                Defaults to None.
            create (bool, optional): Flag to mark the creation of a record.
                Defaults to False.
            read (bool, optional): Flag to mark the read operation. Defaults to
                False.
            update (bool, optional): Flag to mark the update of a record.
                Defaults to False.
            delete (bool, optional): Flag to mark the delete operation. Defaults
                to False.

        Returns:
            (list[dict] | list[] | True): A list of dictionaries with all
            records or an empty list or True if it is a creation of a record.

        Raises:
            ER_NO_SUCH_TABLE: Raised by the MySQLConnection object if the
                table does not exist.
            ER_BAD_FIELD_ERROR: Raised by the MySQLConnection object if the
                column does not exist.
            Error: Any other error raised by the MySQLConnection object.

        References:
            `10.6.4 cursor.MySQLCursorDict Class`_

            `10.12.2 errors.Error Exception`_

            `MariaDB Error Codes`_

            `10.5.4 MySQLCursor.execute() Method`_

            `10.2.3 MySQLConnection.commit() Method`_

        .. _10.6.4 cursor.MySQLCursorDict Class:
           https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursordict.html
        .. _10.12.2 errors.Error Exception:
           https://dev.mysql.com/doc/connector-python/en/connector-python-api-errors-error.html
        .. _MariaDB Error Codes:
           https://mariadb.com/kb/en/mariadb-error-codes/
        .. _10.5.4 MySQLCursor.execute() Method:
           https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html
        .. _10.2.3 MySQLConnection.commit() Method:
           https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnection-commit.html

        """

        # If the execution got to this line, it passed the error checking in
        # db_connect().
        cursor = self.connection_db.cursor(dictionary=True)  # MySQLCursorDict

        if create:
            try:
                cursor.execute(sql, values)
                self.connection_db.commit()
                result = True

            except mysql.connector.Error as err:
                shared.print_error_message(err)
                raise Exception("There was an error in the creation of the record.")

        elif read:
            try:
                cursor.execute(sql)  # None
                result = cursor.fetchall()

            except mysql.connector.Error as err:

                # err.errno means the error code (number).
                if err.errno == errorcode.ER_NO_SUCH_TABLE:
                    shared.print_error_message(
                        "Database table does not exist.")
                    raise Exception("Database table does not exist.")

                if err.errno == errorcode.ER_BAD_FIELD_ERROR:
                    shared.print_error_message(
                        "Column does not exist in table.")
                    raise Exception("Column does not exist in table.")

                else:
                    shared.print_error_message(err)
                    raise Exception("There was an error reading the record(s).")

        elif update:
            pass

        elif delete:
            pass

        else:
            shared.print_error_message("Must inform the (CRUD) operation.")
            raise Exception("Must inform the (CRUD) operation.")

        # If there was no error in the execution:
        self.affected_rows = cursor.rowcount
        self.insert_id = cursor.lastrowid

        # Closes the cursor.
        cursor.close()

        # Closes the connection.
        #   Chose not to use this function because it is slow.
        #   database_functions.db_disconnect(self.connection_db)
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
