#!/bin/python3

import math
import os
import random
import re
import sys


def get_median(arr):
    n = len(arr)
    middle = n // 2

    if n % 2 == 0:
        return (arr[middle - 1] + arr[middle]) // 2

    return arr[middle]


def quartiles(arr):
    arr.sort()

    n = len(arr)
    middle = n // 2

    q2 = get_median(arr)

    if n % 2 == 0:
        lower_half = arr[:middle]
        upper_half = arr[middle:]
    else:
        lower_half = arr[:middle]
        upper_half = arr[middle + 1:]

    q1 = get_median(lower_half)
    q3 = get_median(upper_half)

    return [q1, q2, q3]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()