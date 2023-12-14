#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = my_list[0]
    for nums in my_list[1:]:
        if nums > max_value:
            max_value = nums
    return max_value
