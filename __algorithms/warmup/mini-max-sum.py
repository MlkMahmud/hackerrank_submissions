#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
  nums = sorted(arr)
  min = sum(nums[0:4])
  max = sum(nums[-4:])
  print(min, max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

