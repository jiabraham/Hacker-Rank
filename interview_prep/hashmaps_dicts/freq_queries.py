#!/bin/python3

import math
import os
import random
import re
import sys

def add_to_db(database_dict, insert, freq_dict):
    if insert in database_dict:
        prev_freq = database_dict[insert]
        database_dict[insert] += 1
        freq_dict[prev_freq] -= 1
        if prev_freq+1 in freq_dict:
            freq_dict[prev_freq+1] += 1
        else:
            freq_dict[prev_freq+1] = 1
    else:
        database_dict[insert] = 1
        if 1 in freq_dict:
            freq_dict[1] += 1
        else:
            freq_dict[1] = 0
    #print(database_dict)

def remove_from_db(database_dict, remove, freq_dict):
    if remove in database_dict and database_dict[remove] > 0 and freq_dict[database_dict[remove]] > 0:

        database_dict[remove] -= 1
        freq_dict[database_dict[remove]] -= 1
    #print(database_dict)

# Complete the freqQuery function below.
def freqQuery(queries):
    database_dict = {}
    freqlist = []
    freq_dict = {}
    #for i in range(0, len(queries)):
    #    print("query type = " + str(queries[i][0]) + " query data value = " + str(queries[i][1]))
    for i in range(0, len(queries)):
            if queries[i][0] == 1:
                add_to_db(database_dict, queries[i][1], freq_dict)
                continue
            elif queries[i][0] == 2:
                remove_from_db(database_dict, queries[i][1], freq_dict)
                continue
            else:
                if queries[i][1] in freq_dict:

                    freqlist.append("1")
                else:
                    freqlist.append("0")
    
    return freqlist
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
