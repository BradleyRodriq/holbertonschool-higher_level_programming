#!/usr/bin/python3
""" list all states"""
import MySQLdb
import sys


if __name__ == "__main__":
    """ list all states """
    """
    password = '2792'
    dtb = MySQLdb.connect(user='root', passwd=password, db='hbtn_0e_0_usa')
    """
    dtb = MySQLdb.connect(user=sys.argv[1], port=3306, passwd=sys.argv[2], db=sys.argv[3])
    cursor = dtb.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    dtb.close()
