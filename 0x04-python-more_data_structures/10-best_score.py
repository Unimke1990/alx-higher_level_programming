#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    highest_key = None
    highest_value = float('-inf')
    for key, value in a_dictionary.items():
        if value > highest_value:
            highest_key = key
            highest_value = value
    return highest_key
