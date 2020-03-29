#!/usr/bin/python3
""" List states """
if __name__ == "__main__":
    import sys
    import MySQLdb

    engine = MySQLdb.connect(user=sys.argv[1],
                             passwd=sys.argv[2], host="localhost",
                             db=sys.argv[3])
    cursor = engine.cursor()
    cursor.execute("SELECT name, id
                   FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query = cursor.fetchall()
    for row in query:
        print(row)
    cursor.close()
    engine.close()
