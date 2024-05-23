#!/usr/bin/python3

def reverse_dictionary(dict):
    return {value: key for key, value in dict.items()}

dict = {'apple': 'red', 'banana': 'yellow', 'kiwi': 'green'}
print (reverse_dictionary(dict))
