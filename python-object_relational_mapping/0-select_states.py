#!/usr/bin/python3
""" list all states from the database """
import MySQLdb
import sys


if __name__ == "__main__":
    """ list all states from the database """
    dtb = MySQLdb.connect(user=sys.argv[1], port=3306, passwd=sys.argv[2], db=sys.argv[3])
    cursor = dtb.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
