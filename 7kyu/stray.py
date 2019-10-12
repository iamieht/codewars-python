def stray(arr):
    """
    Input: Array -> Int
    produces the single different number in the array
    """
    unique = 0
    for element in arr:
        if arr.count(element) == 1:
            unique = element
    
    return unique




#Test
print("Expected result: 2")
print("Actual result:", stray([1, 1, 1, 1, 1, 1, 2]))
print("Expected result: 3")
print("Actual result:", stray([2, 3, 2, 2, 2]))
print("Expected result: 3")
print("Actual result:", stray([3, 2, 2, 2, 2]))