#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = [int(s+a) for s in apples]
    oranges = [int(s+b) for s in oranges]
    v_a = 0
    v_o = 0
    for apple in apples:
        if apple>=s and apple<=t:
            v_a += 1
    for orange in oranges:
        if orange>=s and orange<=t:
            v_o += 1
    print(v_a)
    print(v_o)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
