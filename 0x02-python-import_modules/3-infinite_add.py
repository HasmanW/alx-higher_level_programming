#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0
    arg_len = len(sys.argv)
    for value in range(1, arg_len):
        sum += int(sys.argv[value])
    print("{}".format(sum))
