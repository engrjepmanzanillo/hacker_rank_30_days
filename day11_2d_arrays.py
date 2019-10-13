#!/bin/python3
# https://www.hackerrank.com/challenges/30-2d-arrays/problem
# engrjepmanzanillo

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    arr = [[1, 1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0],
           [0, 0, 2, 4, 4, 0],
           [0, 0, 0, 2, 0, 0],
           [0, 0, 1, 2, 4, 0]]
    # for _ in range(6):
    #         arr.append(list(map(int, input().rstrip().split())))
    sums = []
    for i in range(len(arr)-2):
        for j in range(len(arr[i])-2):
            sub_total = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
                arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            sums.append(sub_total)

    print(max(sums))
