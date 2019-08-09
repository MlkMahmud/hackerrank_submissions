
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
  pos, neg, zero, nums = (0, 0, 0, len(arr))

  for i in arr:
    if i > 0:
      pos += 1
    elif i < 0:
      neg += 1
    else:
      zero += 1
  
  print(round(pos / nums, 6))
  print(round(neg / nums, 6))
  print(round(zero / nums, 6))
  

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

