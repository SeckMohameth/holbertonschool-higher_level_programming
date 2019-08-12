#!/usr/bin/python3
#Getting item where name is in argument
if __name__ == '__main__':
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state = sys.argv[4]

    conn = MySQLdb.connect(host='localhost', user=username, port=3306,
                           password=password, db=dbname)


    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{:s}'
    ORDER BY id ASC",format(state))
    rows = cur.fetchone()
    while state:
        print(state)
        state = cur.fetchone()

    cur.close()
    conn.close()
