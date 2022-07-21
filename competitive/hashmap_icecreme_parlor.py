import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#


def icecreamParlor(m, arr):
    # Write your code here
    sum_money = m
    lookup = {}
    result_choices = []
    for idx, each in enumerate(arr):
        other = sum_money - each
        try:
            jidx = lookup[other]
            result_choices = sorted([idx + 1, jidx + 1])
            break
        except KeyError:
            lookup[each] = idx
    return result_choices


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        print(' '.join(map(str, result)))
        # fptr.write(' '.join(map(str, result)))
        # fptr.write('\n')

    # fptr.close()
