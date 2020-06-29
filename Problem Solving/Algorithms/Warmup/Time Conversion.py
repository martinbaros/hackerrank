#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    t, p = s[2:8], s[:2]
    if "A" in s:
        if "12" == p:
            p = "00"
    else:
        if "12" != p:
            p = str(int(p)+12)
    return str(p+t)
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
