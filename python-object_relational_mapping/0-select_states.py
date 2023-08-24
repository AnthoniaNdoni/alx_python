#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
 Usage: ./0-select_states.py <mysql username> \
                            <mysql password> \
                             <database name>
"""
# import dbobject
import sys
import MySQLdb

try:
    # connect to the database
    if len(sys.argv) > 3:
        database = MySQLdb.connect(user=f"{sys.argv[1]}",
                                    passwd=f"{sys.argv[2]}", 
                                    db=f"{sys.argv[3]}")
        
        # set cursor if connection succed
        cursor = database.cursor()

        # Corrected line length and added spaces around operators
        cursor.execute("SELECT * FROM states ORDER by states.id")

        # fetch all rows in the result
        rows = cursor.fetchall()

        # loop through the result to get the state id and name
        for row in rows:
            print(row)

    else:
        pass

    database.close()
    # if there is an error catch it with and exception message
except MySQLdb.OperationalError as e:

    # print the error message
    print("Connection failed. {}".format(e))
