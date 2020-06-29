#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    mino = 0
    maxo = 0
    arr.sort()
    for i in range(4):
        mino += arr[i]
        maxo += arr[i+1]
    print(mino,maxo)



if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
