#!/usr/bin/python3

from sys import argv

def add(a, b):
    return a + b

if len(argv) != 3:
    print("This function needs two integers")

else:
    a = int(argv[1])
    b = int(argv[2])
    result = a + b
    print(result)
