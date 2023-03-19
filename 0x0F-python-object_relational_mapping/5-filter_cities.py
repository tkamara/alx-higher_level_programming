#!/usr/bin/python3

# Listing state dependent on argument

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Listing states
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name FROM cities \
                INNER JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s", [sys.argv[4]])

    rows = cur.fetchall()
    j = []
    for i in rows:
        j.append(i[1])
    print(", ".join(j))

    cur.close()
    db.close()
