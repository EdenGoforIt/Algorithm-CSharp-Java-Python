#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#


def matchingStrings(strings, queries):
    result = []

    for s in queries:
        numbers = strings.count(s)
        result.append(numbers)

    return (result)


if __name__ == '__main__':
    matchingStrings(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc'])
