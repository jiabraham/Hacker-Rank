#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    min_jumps = 0
    i = 0
    while (i < len(c)):
        if (i+2 >= len(c)):
            min_jumps += 1
            i += 1
        elif (c[i+2] == 1):
            min_jumps += 1
            i += 1
        else:
            min_jumps += 1
            i += 2

    
    return min_jumps-1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
