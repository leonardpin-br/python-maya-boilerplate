# -*- coding: utf-8 -*-
u"""

"""

import os
import sys

sys.path.insert(0, os.path.abspath('../../py27env/Lib/site-packages'))
# import mysql.connector

__copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
__author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
__link__ = u"https://www.leonardopinheiro.net"


__all__ = [
    'ConnectionDB'
]


class ConnectionDB(object):


    affected_rows = 0
    insert_id = 0

    def __init__(self, hostname, username, password, database):
        pass


        # self.cnx = mysql.connector.connect(user=username, password=password, host=hostname, database=database)

        # print(self.cnx)

    def query(self, sql):
        pass

    def escape_string(self, string_to_escape):
        pass