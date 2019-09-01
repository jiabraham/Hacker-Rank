#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    altitude = 0
    previous_move = 0
    if (s[0:1] == "U"):
        altitude = 1
        previous_move = "up"
    else:
        altitude = -1
        previous_move = "down"


    
    for i in range(1, len(s)):
        if (s[i:i+1] == "U"):
            altitude += 1
            previous_move = "up"
        else:
            altitude -= 1
            previous_move = "down"
        
        if (previous_move == "up" and altitude == 0):
            valleys += 1
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
