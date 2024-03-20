#!/usr/bin/python3
""" displays values in states where name matches the argument 4 """
import MySQLdb
import sys


if __name__ == "__main__":
    """ displays values in states where name matched the argument 4 """
    """
    password = '2792'
    dtb = MySQLdb.connect(host= 'localhost', user='root', port=3306,
    passwd=password, db='hbtn_0e_4_usa')
    """
    dtb = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                          passwd=sys.argv[2], db=sys.argv[3])
    curs = dtb.cursor()
    curs.execute("""SELECT cities.id, cities.name, states.name FROM cities
                 JOIN states ON cities.state_id = states.id
                 ORDER BY cities.id ASC""")
    rows = curs.fetchall()
    for row in rows:
        print(row)
