#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for nums in my_list:
        elements = nums % 2 == 0
        new_list.append(elements)
    return new_list
