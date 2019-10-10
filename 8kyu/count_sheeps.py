def count_sheeps(arrayOfSheeps):
    """
    Input: List -> Int
    produces the number of True values in the array
    """
    return arrayOfSheeps.count(True)

#Tests
array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]

print('Expected result: 17')
print('Actual result:', count_sheeps(array1))