#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
  if x2 > x1 and v2 > v1 or v1 == v2 and not x1 == x2: 
    return 'NO'
  a = x1 + v1    
  b = x2 + v2
  dist = b - a 

  while True:
    if dist < 0:
      return 'NO'
    if a == b:
      return 'YES'
    
    a += v1
    b += v2
    dist = b - a
  
    
    dist = b - a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

