#!/usr/bin/python3
"""
Listing all states that begin with N from database hbtn_0e_0_usa
"""


import MySQLdb
import sys

if __name__ == "__main__":
    """
    Listing states beginning with N
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
