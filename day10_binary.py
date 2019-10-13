#!/bin/python3
#https://www.hackerrank.com/challenges/30-binary-numbers/problem
#engrjepmanzanillo

import math
import os
import random
import re
import sys

def max_consecutive(dec_num):
    bin_num = bin(dec_num)
    bin_list = [item for item in str(bin_num)]
    del bin_list[:2] # removed the 0b prefix
    bin_list = ''.join(bin_list).split('0')
    counter = []
    for item in bin_list:
        counter.append(len(item))
    return max(counter)


if __name__ == '__main__':
    #n = int(input())
    n = 9999
    print(max_consecutive(n))