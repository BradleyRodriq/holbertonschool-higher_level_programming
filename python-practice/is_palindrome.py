#!/usr/bin/python3

def is_palindrome(string):
    reversed_string = string[::-1]

    if reversed_string == string:
        return True
    else:
        return False

print(is_palindrome("radar"))
