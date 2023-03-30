#!/usr/bin/python3

for letter in string.ascii_lowercase:
    if letter not in "qe":
        print("{}".format(letter), end="")
