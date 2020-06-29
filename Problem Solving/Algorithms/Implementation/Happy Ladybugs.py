#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    empty = 0
    unhappy = 0
    samo = False
    nums = {}
    if len(b) == 1 and b != "_":
        return "NO"
    for i in range(len(b)):
        if b[i] not in nums:
            nums[b[i]] = 1
        else:
            nums[b[i]] = nums[b[i]] + 1
        if b[i] != "_":

            if i==0 and len(b)!=1:
                if b[i+1] != b[i]:
                    unhappy += 1
            elif i == len(b)-1:
                if b[i-1] != b[i]:
                    unhappy += 1
            else:
                defa = True
                if b[i+1] == b[i]:
                    defa = False
                if (b[i+1] != b[i]):
                    defa = False
                if defa == True:
                    unhappy += 1
    for x,y in nums.items():
        if x == "_":
            empty = y
        elif y == 1:
            samo = True
    if (empty >= 1) and (samo==False):
        return "YES"
    if empty==0 and unhappy ==0:
        return "YES"
    return "NO"

    #Not very good solution but it is almost midnight right now

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
