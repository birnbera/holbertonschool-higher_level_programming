#!/usr/bin/python3
"""Script that takes state name as an argument and lists all cities from
that state using database hbtn_0e_4_usa.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.`name` FROM cities "
                "JOIN states ON cities.`state_id` = states.`id` "
                "WHERE states.`name` = {}"
                "ORDER BY cities.`id` ASC".format(
                    db.string_literal(sys.argv[4]).decode()))
    print(', '.join(map(lambda x: x[0], cur.fetchall())))
