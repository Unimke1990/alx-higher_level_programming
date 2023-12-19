#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_values = set()
    for elements in my_list:
        unique_values.add(elements)
        sum_unique = sum(unique_values)
    return sum_unique
