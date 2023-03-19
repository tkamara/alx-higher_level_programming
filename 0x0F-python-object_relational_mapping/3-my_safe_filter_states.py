#!/usr/bin/python3

# improving #2 to be safe from SQL injections

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Improving 2 to avoid SQL injections
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states`")
    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]
