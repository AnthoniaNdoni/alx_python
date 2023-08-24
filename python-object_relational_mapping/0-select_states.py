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

        # Corrected line length and added spaces around operators
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        
        rows= cursor.fetchall()
        for state in rows:
            print(state)

        cursor.cose() # move this line insde the if block
        database.close()
    else:
        None
except MySQLdb.OperationalError as e:
    print("Connection failed. {}".format(e))