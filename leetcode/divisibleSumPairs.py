#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#


def divisibleSumPairs(n, k, ar):
    rest = [0] * k
    nrOfPairs = 0
    for elem in ar:
        nrOfPairs += rest[(k - elem % k) % k]
        #this is the occurence of the previous where we can choose from the new element
        rest[elem % k] += 1
    return nrOfPairs


if __name__ == '__main__':
    print(divisibleSumPairs(4, , [1, 2, 3, 6]))
    print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))
    print(divisibleSumPairs(6, 5, [1, 2, 3, 4, 5, 6]))
