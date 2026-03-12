#Submission
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def candies(n, arr):
    candies = [1] * n
    for j in range(n):
            for i in range(n):
                if i > 0 and arr[i] > arr[i-1] and candies[i] <= candies[i-1]:
                    candies[i]= candies[i-1]+1
                if i < n-1 and arr[i] > arr[i+1] and candies[i] <= candies[i+1]:
                    candies[i] = candies[i+1]+1
    return sum(candies)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
