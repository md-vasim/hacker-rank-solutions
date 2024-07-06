#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    # minsum = sum(arr[1:])
    # maxsum = sum(arr[:-1])
    # print(f"{minsum} {maxsum}") 

    avgs = []
    for i in range(len(arr)):
        avgs.append(sum(arr[:i]+arr[i+1:]))
        print(arr[:i]+arr[i+1:])

    print(avgs)
    print(f"{min(avgs)} {max(avgs)}")

if __name__ == '__main__':

    # arr = list(map(int, input().rstrip().split()))
    # sample input: 1 2 3 4 5, 7 69 2 221 8974
    # [1, 2, 3, 4, 5]
    # miniMaxSum(arr)
    miniMaxSum([7, 69, 2, 221, 8974])


