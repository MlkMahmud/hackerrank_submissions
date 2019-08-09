#!/bin/python3

import os
import sys

def timeConversion(s):
  time = ''
  hour = int(s[0:2])
  if 'AM' in s:
    if hour == 12:
      time = '00' + s[2:-2]
    else:
      time = s[0: -2]
  else:
    if hour == 12:
      time = s[0: -2]
    else:
      time = str(hour + 12) + s[2:-2]

  return time


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

