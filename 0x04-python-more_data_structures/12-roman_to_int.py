#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(roman_string)):
        value = roman_mapping.get(roman_string[i], 0)
        if i < len(roman_string) - 1 and roman_mapping.get(roman_string[i + 1], 0) > value:
            result -= value
        else:
            result += value
    return result
