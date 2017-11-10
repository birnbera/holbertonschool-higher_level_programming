#!/usr/bin/python3
"""Script to list all states with name starting with `N` from
database `hbtn_0e_0_usa`
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states "
                "COLLATE 'utf8_bin' "
                "WHERE name LIKE 'N%' "
                "ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
