#!/usr/bin/python3

def roman_to_int(roman_string):

    roman_dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
    }

    num = 0
    for i in range(len(roman_string) - 1):
        if roman_string[i] < roman_string[i + 1]:
            num += roman_dict[roman_string[i + 1]] - roman_dict[roman_string[i]]
        else:
            num += roman_dict[roman_string[i]]

