# -*- coding: utf-8 -*-
u"""

"""

import os
import sys

sys.path.insert(0, os.path.abspath('../../py27env/Lib/site-packages'))

for path in sys.path:
    print(path)



# import mysql.connector
# from mysql.connector import Error

# __copyright__ = u"Copyright (C) 2022 Leonardo Pinheiro"
# __author__ = u"Leonardo Pinheiro <info@leonardopinheiro.net>"
# __link__ = u"https://www.leonardopinheiro.net"


# __all__ = [
#     'ConnectionDB'
# ]


# class ConnectionDB(object):


#     affected_rows = 0
#     insert_id = 0

#     def __init__(self, hostname, username, password, database):
#         # pass

#         cnx = mysql.connector.connect(user=username, password=password, host=hostname, database=database)

#         try:
#             cursor = cnx.cursor()
#             cursor.execute("""select 3 from your_table""")
#             result = cursor.fetchall()
#             print(result)
#         finally:
#             cnx.close()

#     def query(self, sql):
#         pass

#     def escape_string(self, string_to_escape):
#         pass