#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    time_list = list(map(int, s[:-2].split(":")))
    pm = s[-2:] in "PM"

    if pm and time_list[0] < 12:
        time_list[0] += 12

    if not pm and time_list[0] == 12:
        time_list[0] = 0

    return (":".join(map(lambda x: str(x).rjust(2, '0'), time_list)))

if __name__ == '__main__':
    timeConversion("12:01:00PM")
    timeConversion("07:05:45PM")
