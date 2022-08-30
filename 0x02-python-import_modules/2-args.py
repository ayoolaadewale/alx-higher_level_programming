#!/usr/bin/python3
if __name == "__main__":
    import sys
    length = len(sys.argv)-1
    if length == 0:
        print("0 arguments.")
    else:
        if length == 1:
            print("{:d} argument:".format(length))
            print("{:d}: {}".format(length, sys.argv[length]))
        else:
            print("{:d} arguments:".format(length))
            for i in range(length):
                print("{:d}: {}".format(i+1, sys.argv[i+1]))
