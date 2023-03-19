#!/usr/bin/python3
"""
Lists all states from databse hbtn_0e_0_usa
"""


import MySQLdb
import sys

if __name__ == "__main__":
    """
    Listing the states
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * from states")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
