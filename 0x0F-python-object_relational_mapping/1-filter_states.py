#!/usr/bin/python3
#Getting items with capital N

if __name__ == '__main__':
    import MySQLdb
    import sys

    conn = MySQLdb.coonect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    cur.close()
    conn.close()
