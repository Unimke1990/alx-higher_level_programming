#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_values = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            int_values += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            pass
    print("")
    return int_values
