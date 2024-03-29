#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    min_dif = 10000000

    arr_sorted = sorted(arr)

    for i in range(0, len(arr)-1):
        if (abs(arr[i]-arr[i+1]) < min_dif):
            min_dif = abs(arr[i]-arr[i+1])

    return min_dif

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
