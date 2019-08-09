#!/bin/python3

import math
import os
import random
import re
import sys

def swap(n, arr):
  for i in range(n):
    x = arr.pop(0)
    arr.append(x)
  return " ".join(str(x) for x in arr)

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    print(swap(d, a))



