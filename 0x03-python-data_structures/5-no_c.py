#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for characters in my_string:
        if characters.lower() != 'c':
            new_string += characters
    return new_string
