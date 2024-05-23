#!/usr/bin/python3

def only_unique_elements(list):
    unique_list = []
    for element in list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

list = [1, 2, 2, 3, 4, 4, 5]
print(only_unique_elements(list))
