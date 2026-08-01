#!/bin/python3

import math
import os
import random
import re
import sys


def stdDev(arr):
    n = len(arr)

    mean = sum(arr) / n

    squared_sum = 0

    for number in arr:
        squared_sum += (number - mean) ** 2

    standard_deviation = math.sqrt(squared_sum / n)

    print(f"{standard_deviation:.1f}")


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)