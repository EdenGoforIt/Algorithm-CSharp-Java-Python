#!/bin/python3

from itertools import count
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
# 1(0,0) 2 3 (0,2)
# 4 5   (1,1)    6
# 7(2,0)  8  9(2,2)
# I can see the only different for the right to left is Y going in reverse


def diagonalDifference(arr):
    length = len(arr)
    diagonal_array = [arr[i][i] for i in range(length)]
    counter_diagonal_array = [arr[i][(length-i)-1] for i in range(length)]

    return abs(sum(diagonal_array) - sum(counter_diagonal_array))
    # print(diagonal_array)
    # print(counter_diagonal_array)


if __name__ == '__main__':
    print(diagonalDifference([[1, 2, 3],
                              [4, 5, 6],
                              [9, 8, 9]]))
