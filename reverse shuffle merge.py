#!/bin/python3

import sys
from collections import Counter
def reverseShuffleMerge(s):
    # Complete this function
    x = Counter(s)
    s1 = ""
    for i in x:
        s += i
    s2 = reversed(s1)

if __name__ == "__main__":
    s = input().strip()
    result = reverseShuffleMerge(s)
    print(result)
