#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    n_a = (a[0])
    n_b = (b[0])

    for x in range(1,len(a)):
        n_a =  (n_a * a[x])//math.gcd(n_a,a[x])
    for q in range(1,len(b)):
        n_b = math.gcd(n_b,b[q])
    count = 0
    for x in range(int(n_a), n_b+1, int(n_a)):
        if math.gcd(x, n_b) == x:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
