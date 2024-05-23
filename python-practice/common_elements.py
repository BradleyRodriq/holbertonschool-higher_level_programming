#!/usr/bin/python3

def common_elements(list1, list2):
    common_list = []
    for element in list1:
        if element in list2:
            if element in common_list:
                continue
            else:
                common_list.append(element)
    return common_list

list1 = [1, 2, 2, 3, 4, 4, 5]
list2 = [2, 3, 5]
print(common_elements(list1, list2))
