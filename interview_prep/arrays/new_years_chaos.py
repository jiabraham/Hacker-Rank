#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    
    total_changes = 0
    for i in range(0, len(q)):
        if (i < q[i]-3):
            print("Too chaotic")
            return
    while (True):
        curr_changes = 0
        i = len(q)-1
        while (i > 0):
            
            if (q[i] < q[i-1]):
                temp = q[i]
                q[i] = q[i-1]
                q[i-1] = temp
                curr_changes += 1
            i -= 1 
        total_changes += curr_changes
        if (curr_changes == 0):
            print(total_changes)
            return


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
