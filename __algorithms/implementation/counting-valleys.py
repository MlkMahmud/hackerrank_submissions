#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
  level = 0
  valleys = 0

  for i in s:
    if i == 'U':
      level += 1
    elif i == 'D':
      level -= 1

    step = i
    
    if level == 0 and step == 'U':
      valleys += 1
      
  return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

