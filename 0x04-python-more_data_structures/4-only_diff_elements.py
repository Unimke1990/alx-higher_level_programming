#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set()
    n1 = set_1 - set_2
    n2 = set_2 - set_1
    return new_set.union(n1, n2)
