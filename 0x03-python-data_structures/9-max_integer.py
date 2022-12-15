#!/usr/bin/python3

def max_integer(my_list=[]):
    max = my_list[0]
    for (i=0 ; i < len(my_list); i++):
        if (max < my_list[i]):
            max = my_list[i]

    return max
