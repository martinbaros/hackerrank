#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    value = 1
    for numero in range(1,n+1):
        value*=numero
    print(value)
if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
