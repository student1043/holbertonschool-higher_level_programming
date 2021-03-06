#!/usr/bin/python3
""" List states """
if __name__ == "__main__":
    import sys
    import MySQLdb

    engine = MySQLdb.connect(user=sys.argv[1],
                             passwd=sys.argv[2], host="localhost",
                             db=sys.argv[3])
    cursor = engine.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
    id ASC".format(sys.argv[4]))
    query = cursor.fetchall()
    for row in query:
        print(row)
    cursor.close()
    engine.close()
