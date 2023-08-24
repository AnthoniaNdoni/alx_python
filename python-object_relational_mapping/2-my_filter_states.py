#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
 Usage: ./0-select_states.py <mysql username> \
                            <mysql password> \
                            <database name>
"""
import sys
import MySQLdb

try:
    if len(sys.argv) > 4:
        database = MySQLdb.connect(user=f"{sys.argv[1]}",
                                   passwd=f"{sys.argv[2]}",
                                   db=f"{sys.argv[3]}")
        cursor = database.cursor()
        state_name = sys.argv[4]
        cursor.execute("SELECT * FROM states WHERE BINARY name = %s "
                       "ORDER BY id ASC", (state_name,))

        rows = cursor.fetchall()
        for state in rows:
            print(state)

        database.close()
    else:
        pass
except MySQLdb.OperationalError as e:
    print("connection failed. {}".format(e))