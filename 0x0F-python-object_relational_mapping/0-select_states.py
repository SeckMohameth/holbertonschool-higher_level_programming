#!/usr/bin/python3
#listing items in db

if __name__ == '__main__':
    import MySQLdb
    import sys
    connect = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                              passwd=sys.argv[2], db=sys.argv[3])

    cur = connect.cursor()

    cur.execute('SELECT * FROM states ORDER BY id ASC')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    connect.close()
