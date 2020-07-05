#!/usr/bin/python3
""" List cities """
if __name__ == "__main__":
    import sys
    import MySQLdb

    engine = MySQLdb.connect(user=sys.argv[1],
                             passwd=sys.argv[2], host="localhost",
                             db=sys.argv[3])
    search = MySQLdb.escape_string(sys.argv[4]).decode()
    execution = "SELECT cities.name FROM cities LEFT JOIN states \
    ON cities.state_id = states.id \
    WHERE states.name = '{}'".format(search)
    cursor = engine.cursor()
    cursor.execute(execution)
    query = cursor.fetchall()
    if len(query) == 0:
        print()
    else:
        for i in range(len(query)):
            if i == len(query) - 1:
                print(query[i][0])
            else:
                print("{}, ".format(query[i][0]), end="")
    cursor.close()
    engine.close()
