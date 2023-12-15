#!/bin/python3

import math
from operator import ne
import os
import random
import re
import sys


def miniMaxSum(arr):
    small = sum(sorted(arr)[:4])
    large = sum(sorted(arr, reverse=True)[:4])

    print("{0} {1}".format(large, small))


if __name__ == '__main__':

    arr = [7, 69, 2, 221, 8974
           ]

    miniMaxSum(arr)
