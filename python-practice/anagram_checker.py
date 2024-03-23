#!/usr/bin/python3

def anagram_check(word1, word2):
    w1 = ''.join(filter(str.isalnum, word1)).lower()
    w2 = ''.join(filter(str.isalnum, word2)).lower()
    sorted_w1 = sorted(w1)
    sorted_w2 = sorted(w2)
    return sorted_w1 == sorted_w2


first = "letter"
second = "rettel"
print(anagram_check(first, second))
