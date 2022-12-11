!/usr/bin/python3
def pow(a, b):
    index = 1
    if b == 0:
        return 1;
    elif b == 1:
        return a
    else:
        return (a * pow(a, b - 1)
