#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    n=len(h)
    max_area = 0
    for i in range(0,n):
        min_height = h[i]
        for j in range(i,n):
            min_height = min(min_height,h[j])
            area = min_height *(j-i+1)
            max_area = max(max_area,area)
    return max_area
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
