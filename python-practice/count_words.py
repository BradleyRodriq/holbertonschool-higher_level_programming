#!/usr/bin/python3

import sys

def count_words(string):
    words = string.split()

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

input_string = "Hello, world! hello,"
print(count_words(input_string))
