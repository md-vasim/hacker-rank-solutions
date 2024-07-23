#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here

    # checking shift 
    shift = s[-2:]

    # separating time from shift 
    t = s[:-2]

    # separating hour to preprocess 
    h = s[:2]
    new_t = ""
    if shift == "AM" and int(h) == 12: 
        h = "00" 
        new_t = h + t[2:]
        print(new_t)
    elif shift == "AM":
        print(t)
    elif shift == "PM" and int(h) == 12:
        print(t)
    elif shift == "PM": 
        new_t = str(int(h)+12) + t[2:]
        print(new_t)


if __name__ == '__main__':
    # 07:05:45PM
    s = "07:05:45PM"
    timeConversion(s)