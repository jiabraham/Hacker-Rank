#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):

    total_dict = {}

    for i in range(0, len(s1)):
        total_dict[s1[i:i+1]] = "first"
    for i in range(0, len(s2)):
        total_dict[s2[i:i+1]] = "second"
    
    for i in range(0, len(s1)):
        if (total_dict[s1[i:i+1]] == "second"):
            return "YES"
    #for i in (0, len(s2)):
    #    if (total_dict[s2[i:i+1]] == "f"):
    #        return "YES"
    
    return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
