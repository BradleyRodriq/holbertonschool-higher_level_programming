#!/usr/bin/python3
for letter in range(97, 123):
    print(f"{chr(letter)}", end="\n" if letter == 122 else "")
