#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    
    single_string_a_count = 0
    complete_string_repeats = int(n/len(s))

    for i in range (0, len(s)):
        if (s[i:i+1] == 'a'):
            single_string_a_count += 1
    
    complete_string_a_count = (single_string_a_count)*complete_string_repeats
    total_a_count = complete_string_a_count
    incomplete_repeat_length = n - (complete_string_repeats*len(s))

    for i in range(0, incomplete_repeat_length):
        if (s[i:i+1] == 'a'):
            total_a_count += 1
    

    return total_a_count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
