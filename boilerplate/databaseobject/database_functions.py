# -*- coding: utf-8 -*-
u"""A collection of database related functions.

References:
    `5.1 Connecting to MySQL Using Connector/Python`_

.. _5.1 Connecting to MySQL Using Connector/Python:
   https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

"""

import os
import sys

import shared
shared.add_site_packages_to_sys_path(__file__)

import mysql.connector
from mysql.connector import errorcode

import db_credentials


def confirm_db_connect(connection):
    u"""Not implemented, following the `MySQL documentation`_.

    .. _MySQL documentation:
       https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
    """
    pass


def db_connect():
    u"""Establishes the connection with the MySQL database.

    If the connection is not successful, raises an error and shows the message.

    Returns:
        MySQLConnection: A MySQLConnection object.

    Raises:
        ER_ACCESS_DENIED_ERROR: Raised by the MySQLConnection object if the
            access to the database was denied.
        ER_DBACCESS_DENIED_ERROR: Raised by the MySQLConnection object if the
            database does not exist.
        Error: Any other error raised by the MySQLConnection object.

    Error:
        Sphinx shows a different (**wrong**) error message than is implemented
        here::

            UnboundLocalError: local variable 'connection_db' referenced before assignment

        Autodesk Maya 2018 and 2020 show the correct error message and the same
        wrong one as Sphinx.

    References:

        `5.1 Connecting to MySQL Using Connector/Python`_

        `Shared MariaDB/MySQL error codes`_

    .. _5.1 Connecting to MySQL Using Connector/Python:
       https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
    .. _Shared MariaDB/MySQL error codes:
       https://mariadb.com/kb/en/mariadb-error-codes/#shared-mariadbmysql-error-codes

    """

    try:
        connection_db = mysql.connector.connect(user=db_credentials.DB_USER, password=db_credentials.DB_PASS,
                                                host=db_credentials.DB_SERVER,
                                                database=db_credentials.DB_NAME)

        return connection_db

    except mysql.connector.Error as err:

        # err.errno means the error code (number).
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            shared.print_error_message(
                "Something is wrong with your username or password.")
            raise

        elif err.errno == errorcode.ER_DBACCESS_DENIED_ERROR:
            shared.print_error_message("Database does not exist.")
            raise

        else:
            shared.print_error_message(err)
            raise


def db_disconnect(connection):
    u"""Closes the database connection.
    """
    if shared.is_set(connection):
        connection.close()
