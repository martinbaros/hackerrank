#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matrixRotation function below.
def matrixRotation(matrix, r, m, n):
    nova = matrix.copy()
    pocet=min([m,n])//2
    for k in range(pocet):
        a = m-(k*2)
        b = n-(k*2)
        vrstva = []
        hodnoty = []
        poc = 0
        for i in range(a):
            vrstva.append((i+k,k))
            hodnoty.append(matrix[i+k][k])
            poc+=1
        for i in range(1,b):
            vrstva.append((m-k-1,i+k))
            hodnoty.append(matrix[m-k-1][i+k])
            poc+=1
        for i in range(1,a):
            vrstva.append((m-k-i-1,n-1-k))
            hodnoty.append(matrix[m-k-i-1][n-1-k])
            poc+=1
        for i in range(1,b-1):
            vrstva.append((k,n-1-i-k))
            hodnoty.append(matrix[k][n-1-i-k])
            poc+=1

        obvod = (2*(a)+2*(b-2))
        real_r = r-((r//obvod)*obvod)

        zmenene = []
        for oio in range(obvod):
            zmenene.append(0)
        for ind in range(obvod):
            if ind+real_r > obvod-1:
                h = ind+real_r-obvod
            else:
                h = ind+real_r
            zmenene[h] = hodnoty[ind]
        for ind in range(obvod):
            poz = vrstva[ind]
            nova[poz[0]][poz[1]] = zmenene[ind]

    for i in range(m):
        print(' '.join(map(str, nova[i])))






if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r, m, n)
