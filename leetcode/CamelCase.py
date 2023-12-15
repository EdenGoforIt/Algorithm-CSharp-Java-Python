#!/bin/python3

import math
import os
import random
import re
import sys


def camelCase(s):
    isSplit = is_split(s)

    if isSplit:
        trimmed = s.replace("()", "")
        return (process_split_word(trimmed))
    else:
        return (process_combine_word(s))


def process_combine_word(s):
    type = s[2]
    values = s.split(";")[2].split(" ")

    new_values =  capitalize_second_words(values, type)
    new_value = ''.join(new_values)

    if new_value[0].isupper() and type == "C":
        new_value[0] = new_value[0].upper()
    if type == "M":
        return new_value + "()"
    return new_value


def capitalize_second_words(values, type):
    new_values = []
    for i in range(len(values)):
        if i != 0 and type != "C":
            new_values.append(values[i].capitalize())
        else:
            new_values.append(values[i])
    return new_values

def initial_to_upper(i, s):
    if i != 0:
        return s.capitalize()
    return s


def process_split_word(s):
    result = ""
    values = s.split(";")[2]
    for i in range(len(values)):
        c = values[i]
        if c.isupper():
            if i != 0:
                result += " "
            result += c.lower()
        else:
            result += c
    return result


def is_split(s):
    if s[0] == "S":
        return True
    return False


if __name__ == '__main__':
    # camelCase("S;M;plasticCup()")
    camelCase("C;V;mobile phone")
    camelCase("C;C;coffee machine")
    # camelCase("S;C;LargeSoftwareBook")
    camelCase("C;M;white sheet of paper")
    # camelCase("S;V;pictureFrame")
