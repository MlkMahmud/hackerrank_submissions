#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
  block = '#'

  for i in range(n):
    print(block.rjust(n))
    block += '#'

if __name__ == '__main__':
    n = int(input())

    staircase(n)

