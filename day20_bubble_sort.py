#!/bin/python3
# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/30-sorting/problem
# author = @engrjepmanzanillo

import sys

n = 3
a1 = [1, 2, 3]
a2 = [3, 2, 1]
# Write Your Code Here


def bubbleSort(n, a):
    numSwaps = 0
    i = 0
    while i < n:
        for j in range(n - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                numSwaps += 1
        i += 1

    return numSwaps, a


result = bubbleSort(n, a2)
print(f'Array is sorted in {result[0]} swaps.')
print(f'First Element: {min(result[1])}')
print(f'Last Element: {max(result[1])}')
