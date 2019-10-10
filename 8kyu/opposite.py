def opposite(number):
  """
  Number -> Number
  produces the opposite number
  """
  return abs(number) if number < 0 else number * -1

def opposite_better(number):
    return -number

#Tests
print('Expected result: -1')
print('Actual result:', opposite(1))
print('Expected result: -1')
print('Actual result:', opposite_better(1))