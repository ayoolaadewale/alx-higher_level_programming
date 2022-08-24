#!/usr/bin/python3
for j in range(0, 100):
    if j < 10:
        print("0{}".format(j), end=', ')
    else:
        print("{}".format(j), end=', ')
