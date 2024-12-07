import itertools

import numpy as np

from advent import common as util


def operate (op, a , b):
    #print(a, op, b, "=", )
    if op == '+':
        return a + b
    elif op == '*':
        return a * b
    elif op == '||':
        return int(str(a) + str(b))
    return None

f = "test.txt"
f1 = "2024-7-input.txt"



input = util.read_input(f1, ":")
#loop
sum = 0
for item in input:
  key = item[0]
  values = np.array(item[1].split(), dtype=int)
  boxes = values.size - 1
  combinations = list(itertools.product(['+', '*', '||'], repeat=boxes))

  # loop over values
  for combination in combinations:
      result = values[0]
      for i in range(1, len(values)):
          result  = operate(combination[i-1], result, values[i])
          #print("=", result)
      if result == int(key):
          print("===found ", result, " ", combination)
          sum += result
          success = True
          break

print("sum = " , sum)

