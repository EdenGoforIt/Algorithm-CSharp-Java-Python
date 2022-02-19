#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def pangrams(s):
    pangram = 'pangram'
    not_pangram = 'not pangram'

    sett = set(s.strip().lower().replace(' ', ''))
    return pangram if len(sett) == 26 else not_pangram

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return pangram
    if len(sett) == 21:
        return pangram
    return not_pangram


if __name__ == '__main__':
    print(pangrams("All of the letters of the alphabet are present in the string"))
    print(pangrams("We promptly judged antique ivory buckles for the prize"))
