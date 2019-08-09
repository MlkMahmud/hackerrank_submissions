#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
  total = sum(arr[0][0:3]) + sum(arr[1][1:2]) + sum(arr[2][0:3])

  for i in range(4):
    glass = sum(arr[i][0:3]) + sum(arr[i + 1][1:2]) + sum(arr[i + 2][0:3])
    if glass > total:
      total = glass
    glass = sum(arr[i][1:4]) + sum(arr[i + 1][2:3]) + sum(arr[i + 2][1:4])
    if glass > total:
      total = glass
    glass = sum(arr[i][2:5]) + sum(arr[i + 1][3:4]) + sum(arr[i + 2][2:5])
    if glass > total:
      total = glass
    glass = sum(arr[i][3:6]) + sum(arr[i + 1][4:5]) + sum(arr[i + 2][3:6])
    if glass > total:
      total = glass
  
  return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

