#!/usr/bin/python3
for digit1 in range(0,10):
    for digit2 in range(digit1 + 1,10):
        if digit1 == digit2:
            continue
        else:
            print("{}{}".format(digit1,digit2), end=", ")
~

