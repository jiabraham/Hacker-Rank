#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    cost_dict = {}

    for i in range(0, len(cost)):
        cost_dict[cost[i]] = i
    
    for i in range(0, len(cost)):
        target = money - cost[i]
        try:
            target_index = cost_dict[target]
            if (target_index == i):
                continue
            print(str(i+1)+ " " + str(target_index+1))
            break
        except:
            continue




if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
