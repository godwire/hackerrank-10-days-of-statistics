#!/bin/python3

import math
import os
import random
import re
import sys


def median(arr):
    n = len(arr)
    middle = n // 2

    if n % 2 == 0:
        return (arr[middle - 1] + arr[middle]) / 2

    return arr[middle]


def interQuartile(values, freqs):
    data = []

    for i in range(len(values)):
        for _ in range(freqs[i]):
            data.append(values[i])

    data.sort()

    n = len(data)
    middle = n // 2

    if n % 2 == 0:
        lower_half = data[:middle]
        upper_half = data[middle:]
    else:
        lower_half = data[:middle]
        upper_half = data[middle + 1:]

    q1 = median(lower_half)
    q3 = median(upper_half)

    result = q3 - q1

    print(f"{result:.1f}")


if __name__ == '__main__':
    n = int(input().strip())

    values = list(map(int, input().rstrip().split()))

    freqs = list(map(int, input().rstrip().split()))

    interQuartile(values, freqs)