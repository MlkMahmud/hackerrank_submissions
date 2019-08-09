#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
  if p == n or p == 1:
    return 0
  front = 1
  front_cnt = 0
  back_cnt = 0
  if not n % 2 == 0:
    back = n - 1
  else:
    back = n
  while True:
    if front >= p:
      return front_cnt
    elif back <= p:
      return back_cnt
    else:
      front += 2
      back -= 2
      front_cnt += 1
      back_cnt += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

