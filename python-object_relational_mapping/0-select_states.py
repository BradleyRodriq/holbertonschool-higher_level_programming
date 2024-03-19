#!/usr/bin/python3
""" list all states"""
import MySQLdb
import sys


if __name__ == "__main__":
    """ list all states """
    dtb = MySQLdb.connect(user=sys.arg[1], passwd=sys.arg[2], db=sys.arg[3])
    cursor = dtb.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    dtb.close()
