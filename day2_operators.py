#!/bin/python3
"""Objective
In this challenge, you'll work with arithmetic operators. Check out the Tutorial tab for learning materials and an instructional video!

Task
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!"""

"""
Sample Input

12.00
20
8
"""


# Complete the solve function below.




import math
import os
import random
import re
import sys
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost*tip_percent/100
    tax = meal_cost*tax_percent/100
    print(round(meal_cost + tip + tax))


if __name__ == '__main__':
    meal_cost = float(12.00)

    tip_percent = int(20)

    tax_percent = int(8)

    solve(meal_cost, tip_percent, tax_percent)
