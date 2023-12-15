import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#


def flippingBits(n):
    return (2**32-1) ^ n


if __name__ == '__main__':
    print(flippingBits(2147483647))
    print(flippingBits(1))
    print(flippingBits(0))
