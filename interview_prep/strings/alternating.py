#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):

    s_index = 0
    min_deletions = 0

    while s_index < len(s)-1:
        if s[s_index:s_index+1] == s[s_index+1:s_index+2]:
            s = s[0:s_index+1]+s[s_index+2:len(s)]
            min_deletions += 1
            continue
        s_index += 1

    return min_deletions;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
