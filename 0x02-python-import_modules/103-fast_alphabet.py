#!/usr/bin/python3
if __name__ == "__main__":
    for alphabet in range(65, 91):
        print("{:c}".format(alphabet), end='\n' if alphabet == 90 else '')
