#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the equal function below.
def equal(arr):
    arr.sort(key=Counter(arr).get, reverse=True)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()