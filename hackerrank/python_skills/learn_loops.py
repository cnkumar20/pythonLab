import math
import os
import random
import re
import sys


def list_squares_of_list_less_than_n(n):
    for x in range(n):
        print(x * x)


def list_number(n):
    for x in range(0, -n, -2):
        print(x)


def avg(np):
    return np



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nums = list(map(int, input().split()))
    res = avg(*nums)
    print(res)


