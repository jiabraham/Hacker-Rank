#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    histogram = {}
    sock_counter = 0

    for i in range(0, len(ar)):
        key = str(ar[i])
        histogram[key] = 0

    for i in range(0, len(ar)):
    #    print("ar[" + i + "] = " + ar[i]) 
        key = str(ar[i])
        histogram[key] += 1
    
    for i in histogram:
        sock_counter += int(histogram[i]/2)
    
    return sock_counter 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
