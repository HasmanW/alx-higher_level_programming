#!/usr/bin/python3
for alphabet in range(65, 91):
    print("{:c}".format(alphabet), end='\n' if alphabet == 90 else '')
