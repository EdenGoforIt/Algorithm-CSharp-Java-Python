#!/bin/python3

import math
import os
import random
import re
import sys


def breakingRecords(s):
    min, max = s[0], s[0]
    least, most = 0, 0

    for v in s:
        if v < min:
            min = v
            least += 1
        if v > max:
            max = v
            most += 1

    print([most, least])


if __name__ == '__main__':
    breakingRecords([12, 24, 10, 24])
