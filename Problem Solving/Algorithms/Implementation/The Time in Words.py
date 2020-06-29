#!/bin/python3

import math
import os
import random
import re
import sys

def numToText(n):
    nums = ["zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen",
            "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen",
            "twenty", "twenty one", "twenty two",
            "twenty three", "twenty four",
            "twenty five", "twenty six", "twenty seven",
            "twenty eight", "twenty nine"];
    return nums[n]
# Complete the timeInWords function below.
def timeInWords(h, m):
    final = ""
    if m == 0:
        final = numToText(h) + " o' clock"
    elif m == 15:
        final = "quarter past " + numToText(h)
    elif m == 30:
        final = "half past " + numToText(h)
    elif m == 45:
        final = "quarter to " + numToText(h+1)
    elif m < 30:
        if m==1:
            final = numToText(m) + " minute past " + numToText(h)
        else:
            final = numToText(m) + " minutes past " + numToText(h)
    elif m > 30:
        final = numToText(60-m) + " minutes to " + numToText(h+1)
    return final

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
