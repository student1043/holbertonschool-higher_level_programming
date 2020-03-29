#!/usr/bin/python3
""" List cities """
if __name__ == "__main__":
    import sys
    import MySQLdb

    engine = MySQLdb.connect(user=sys.argv[1],
                             passwd=sys.argv[2], host="localhost",
                             db=sys.argv[3])
    execution = """SELECT id FROM states INNER JOIN cities ON \
                  states.id=cities.states_id ORDER BY id ASC"""
    cursor = engine.cursor()
    cursor.execute(execution)
    query = cursor.fetchall()
    for row in query:
        print(row)
    cursor.close()
    engine.close()
