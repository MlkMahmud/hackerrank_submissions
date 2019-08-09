#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
  end = len(c) - 1
  pos = 0
  jumps = 0
  
  while True:
    if pos == end:
      return jumps
    else:
      if pos + 2 <= end and c[pos + 2] == 0:
        pos += 2
      else:
        pos += 1

      jumps += 1



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

