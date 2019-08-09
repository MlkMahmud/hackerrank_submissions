# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin, stdout
from re import sub

lines = sub('[\n\s]', ',', stdin.read()).split(',')
max = [0]
stack = []

for i in range(len(lines)):
  if lines[i] == '1':
    x = int(lines[i + 1])
    if x >= max[0]:
      max.insert(0, x)
    
    stack.append(x)
  
  elif lines[i] == '2':
    x = int(stack[-1])
    if x in max:
      max.remove(x)
    stack.pop(-1)
  
  elif lines[i] == '3':
    stdout.write(str(max[0])+ '\n')



