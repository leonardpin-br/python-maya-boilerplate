# -*- coding: utf-8 -*-
u"""Keep database credentials in a separate file.

#. Easy to exclude this file from source code managers.
#. Unique credentials on development and production server.
#. Unique credentials if working with multiple developers.

"""

__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__link__ = u"https://www.leonardopinheiro.net"


__all__ = [
    'DB_SERVER',
    'DB_USER',
    'DB_PASS',
    'DB_NAME'
]


DB_SERVER = "localhost"
DB_USER = "webuser"
DB_PASS = "secretpassword"
DB_NAME = "chain_gang"
