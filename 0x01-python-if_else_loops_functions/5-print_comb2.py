#!/usr/bin/python3

for o in range(0, 100):
    if o != 99:
        print("{:02d}, ".format(o), end="")
    else:
        print("{:02d}".format(o))
