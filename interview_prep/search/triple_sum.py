#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    a = sorted(a)
    b = sorted(b)
    c = sorted(c)

    b_index = 0
    while b_index < len(b)-1:
        if b[b_index] == b[b_index+1]:
            del b[b_index]
            continue
        b_index += 1
        
    a_index = 0
    while a_index < len(a)-1:
        if a[a_index] == a[a_index+1]:
            del a[a_index]
            continue
        a_index += 1
        
    c_index = 0
    while c_index < len(c)-1:
       if c[c_index] == c[c_index+1]:
           del c[c_index]
           continue
       c_index += 1

    print(a)
    print(b)
    print(c)
    count = 0
    a_index = 0
    c_index = 0
    for b_element in b:
        while a_index < len(a):
            if (a[a_index] > b_element):
                break
            a_index += 1
            
        while c_index < len(c):
            if (c[c_index] > b_element):
                break
            c_index += 1
            
        count += (a_index * c_index)

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
