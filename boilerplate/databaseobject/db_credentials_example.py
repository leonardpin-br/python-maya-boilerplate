# -*- coding: utf-8 -*-
u"""This file holds the credentials to access the database.

These are the reasons to keep the credentials in a separate file:

1. Easy to exclude this file from source code managers.
2. Unique credentials on development and production servers.
3. Unique credentials if working with multiple developers.

"""

DB_SERVER = 'localhost'
"""str: The address of the database server."""

DB_USER = 'username'
"""str: The username to access the database server."""

DB_PASS = 'userpassword'
"""str: The password to access the database server."""

DB_NAME = 'databasename'
"""str: The database name."""
