# -*- coding: utf-8 -*-
u"""

"""

__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__link__ = u"https://www.leonardopinheiro.net"


__all__ = [
    'Connection'
]


class Connection(object):
    """Mimics (loosely and in a very crud way) the mysqli (PHP) class.

    Args:
        hostname (str): The hostname (or address) of the database server.
        username (str): The username to connect to the database server.
        password (str): The password to connect to the database server.
        database (str): The database that will be used.
    """
    affected_rows = 0
    insert_id = 0

    def __init__(self, hostname, username, password, database):

        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database

    def query(sql):
        """Executes the query.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            sql (str): sql The SQL query as a string to be executed.

        Returns:
            bool | object | object[]: The return value. True for success, False otherwise.

        """
        pass

    def escape_string(string_to_escape):
        pass
