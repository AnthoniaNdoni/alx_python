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
    if len(sys.argv) > 3:
        database = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        cursor =database.cursor()
        cursor.execute("SELECT * FROM states")
        rows= cursor.fetchall()
        for state in rows:
            print(state)

        database.close()
    else:
        None
except MySQLdb.OperationalError as e:
    print("connection failed. {}".format(e))