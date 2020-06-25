#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    hladane = {}
    pocitadlo = 0
    for cislo in arr:
        if cislo in hladane:
            pocitadlo+=hladane[cislo]

        if cislo+k not in hladane:
            hladane[cislo+k] = 1
        else:
            hladane[cislo+k] = hladane[cislo+k]+1
        if cislo-k not in hladane:
            hladane[cislo-k] = 1
        else:
            hladane[cislo-k] = hladane[cislo-k]+1
        print(pocitadlo)

    return pocitadlo
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
