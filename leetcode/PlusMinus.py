#!/bin/python3

import math
from operator import ne
import os
import random
import re
import sys


def plusMinus(arr):
    total_number = len(arr)
    positive = 0
    negative = 0
    zero = 0

    for i in range(len(arr)):
        value = arr[i]
        if value > 0:
            positive += 1
        elif value < 0:
            negative += 1
        else:
            zero += 1
    print("{0:.4f}".format(positive/total_number if positive != 0 else 0))
    print("{0:.4f}".format(negative/total_number if negative != 0 else 0))
    print("{0:.4f}".format(zero/total_number if zero != 0 else 0))

    return []


if __name__ == '__main__':

    arr = [1, 1, 0, -1, -1]

    plusMinus(arr)
