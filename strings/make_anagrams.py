#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a_histogram = {}
    b_histogram = {}

    deletions = 0

    #initialize histograms
    for i in range(0, 26):
        a_histogram[i] = 0
        b_histogram[i] = 0

    for i in range(0, len(a)):
        if (a[i:i+1] == 'a'):
            a_histogram[0] += 1
        if (a[i:i+1] == 'b'):
            a_histogram[1] += 1
        if (a[i:i+1] == 'c'):
            a_histogram[2] += 1
        if (a[i:i+1] == 'd'):
            a_histogram[3] += 1
        if (a[i:i+1] == 'e'):
            a_histogram[4] += 1
        if (a[i:i+1] == 'f'):
            a_histogram[5] += 1
        if (a[i:i+1] == 'g'):
            a_histogram[6] += 1
        if (a[i:i+1] == 'h'):
            a_histogram[7] += 1
        if (a[i:i+1] == 'i'):
            a_histogram[8] += 1
        if (a[i:i+1] == 'j'):
            a_histogram[9] += 1
        if (a[i:i+1] == 'k'):
            a_histogram[10] += 1
        if (a[i:i+1] == 'l'):
            a_histogram[11] += 1
        if (a[i:i+1] == 'm'):
            a_histogram[12] += 1
        if (a[i:i+1] == 'n'):
            a_histogram[13] += 1
        if (a[i:i+1] == 'o'):
            a_histogram[14] += 1
        if (a[i:i+1] == 'p'):
            a_histogram[15] += 1
        if (a[i:i+1] == 'q'):
            a_histogram[16] += 1
        if (a[i:i+1] == 'r'):
            a_histogram[17] += 1
        if (a[i:i+1] == 's'):
            a_histogram[18] += 1
        if (a[i:i+1] == 't'):
            a_histogram[19] += 1
        if (a[i:i+1] == 'u'):
            a_histogram[20] += 1
        if (a[i:i+1] == 'v'):
            a_histogram[21] += 1
        if (a[i:i+1] == 'w'):
            a_histogram[22] += 1
        if (a[i:i+1] == 'x'):
            a_histogram[23] += 1
        if (a[i:i+1] == 'y'):
            a_histogram[24] += 1
        if (a[i:i+1] == 'z'):
            a_histogram[25] += 1

    for i in range(0, len(b)):
        if (b[i:i+1] == 'a'):
            b_histogram[0] += 1
        if (b[i:i+1] == 'b'):
            b_histogram[1] += 1
        if (b[i:i+1] == 'c'):
            b_histogram[2] += 1
        if (b[i:i+1] == 'd'):
            b_histogram[3] += 1
        if (b[i:i+1] == 'e'):
            b_histogram[4] += 1
        if (b[i:i+1] == 'f'):
            b_histogram[5] += 1
        if (b[i:i+1] == 'g'):
            b_histogram[6] += 1
        if (b[i:i+1] == 'h'):
            b_histogram[7] += 1
        if (b[i:i+1] == 'i'):
            b_histogram[8] += 1
        if (b[i:i+1] == 'j'):
            b_histogram[9] += 1
        if (b[i:i+1] == 'k'):
            b_histogram[10] += 1
        if (b[i:i+1] == 'l'):
            b_histogram[11] += 1
        if (b[i:i+1] == 'm'):
            b_histogram[12] += 1
        if (b[i:i+1] == 'n'):
            b_histogram[13] += 1
        if (b[i:i+1] == 'o'):
            b_histogram[14] += 1
        if (b[i:i+1] == 'p'):
            b_histogram[15] += 1
        if (b[i:i+1] == 'q'):
            b_histogram[16] += 1
        if (b[i:i+1] == 'r'):
            b_histogram[17] += 1
        if (b[i:i+1] == 's'):
            b_histogram[18] += 1
        if (b[i:i+1] == 't'):
            b_histogram[19] += 1
        if (b[i:i+1] == 'u'):
            b_histogram[20] += 1
        if (b[i:i+1] == 'v'):
            b_histogram[21] += 1
        if (b[i:i+1] == 'w'):
            b_histogram[22] += 1
        if (b[i:i+1] == 'x'):
            b_histogram[23] += 1
        if (b[i:i+1] == 'y'):
            b_histogram[24] += 1
        if (b[i:i+1] == 'z'):
            b_histogram[25] += 1
        
        num_del = 0
        for i in range(0, 26):
            num_del += abs(a_histogram[i] - b_histogram[i])
            
        
    return num_del

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
