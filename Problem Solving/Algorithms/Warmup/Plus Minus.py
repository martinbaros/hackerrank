#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pocty = [0,0,0]
    for c in arr:
        if c>0:
            pocty[0] = pocty[0] + 1
        elif c<0:
            pocty[1] = pocty[1] + 1
        else:
            pocty[2] = pocty[2] + 1
    vysledok = [float(round(s/len(arr),6)) for s in pocty]
    final = []
    for polozka in vysledok:
        if len(str(polozka))<8:
            final.append(str(polozka)+("0")*(8-len(str(polozka))))
        else:
            final.append(polozka)
    return final

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    q = plusMinus(arr)
    for a in q:
        print(a)
