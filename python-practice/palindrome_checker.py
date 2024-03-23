#!/usr/bin/python3

def palindrome_check(string):
    clean_string = ''.join(filter(str.isalnum, string)).lower()
    return clean_string == clean_string[::-1]


s = "radar", "A man, a plan, a canal, Panama"
print(palindrome_check(s))
