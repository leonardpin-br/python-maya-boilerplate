# -*- coding: utf-8 -*-
u"""This file holds the credentials to access the database.

These are the reasons to keep the credentials in a separate file:

1. Easy to exclude this file from source code managers.
2. Unique credentials on development and production servers.
3. Unique credentials if working with multiple developers.

"""

DB_SERVER = 'localhost'
DB_USER = 'webuser'
DB_PASS = 'secretpassword'
DB_NAME = 'chain_gang'
