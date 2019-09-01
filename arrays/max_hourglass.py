#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):

    max_hour_glass_sum = -64

    for i in range(1, 5):
        curr_hour_glass_sum = 0
        for j in range(1, 5):
            
            top = arr[i-1][j-1]+arr[i-1][j] + arr[i-1][j+1]
            middle = arr[i][j]
            bottom = arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1]
            curr_hour_glass_sum = top + middle + bottom

            if (curr_hour_glass_sum > max_hour_glass_sum):
                max_hour_glass_sum = curr_hour_glass_sum
    
    return max_hour_glass_sum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
