#!/usr/bin/python3
def to_upper(character):
    if ord(character) >= 97 and ord(charcter) <= 122:
        return (ord(character) - 32)
    else:
        return ord(character)

def uppercase(str):
    new = ""
    for character in str:
        new += "%c" % to_upper(character) #we use the % string format method
    print("{:s}".format(new))
