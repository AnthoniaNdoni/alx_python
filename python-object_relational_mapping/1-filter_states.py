#!/usr/bin/python3
"""
Lists all states with a name starting with N(Upper N)from db hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> \
                            <mysql password> \
                            <database name>
"""

# import dbobject
import sys
import MySQLdb

# try connction and execution
try:

    # connect to database
    if len(sys.argv) > 3:
        database = MySQLdb.connect(user=f"{sys.argv[1]}",
                                   passwd=f"{sys.argv[2]}",
                                   db=f"{sys.argv[3]}")

        # set cursor if connection succeed
        cursor = database.cursor()

        # run the select statement on the states table where users name start
        # with N using the like operation.
        cursor.execute("SELECT * FROM states WHERE name LIKE \
                        'N%' ORDER by states.id")

        # fatch all rows in the result
        rows = cursor.fetchall()

        # loop to get the id and name
        for row in rows:

            # print only the capital letter
            print(row) if row[1][0] == 'N' else None

        database.close()
    else:
        pass

    # if there is an error catch it with exception message
except MySQLdb.OperationalError as e:

        # print the error message
        print("connection failed. {}".format(e))