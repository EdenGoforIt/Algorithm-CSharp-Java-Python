import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(a):
    answer = []
    a.sort()
    answer.append(a[0])
    value = a[0]
    # 1,1,2,2,3
    for i in range(1, len(a)):
        if value == a[i]:
            answer.remove(a[i])
        else:
            value = a[i]
            answer.append(a[i])

    return answer[0]


    # Write your code here
if __name__ == '__main__':
    lonelyinteger([1, 2, 3, 4, 3, 2, 1])
