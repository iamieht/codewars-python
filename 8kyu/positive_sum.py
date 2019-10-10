def positive_sum(arr):
    """
    List of Ints -> Int
    produces the sum of all positive Integers in a List
    """
    result = 0
    for element in arr:
        if element > 0:
            result += element
    
    return result

#Test cases
print('Expected result: 20')
print('Actual result:', positive_sum([1,-4,7,12]))
print('Expected result: 15')
print('Actual result:', positive_sum([1,2,3,4,5]))
print('Expected result: 13')
print('Actual result:', positive_sum([1,-2,3,4,5]))
print('Expected result: 9')
print('Actual result:', positive_sum([-1,2,3,4,-5]))
print('Expected result: 0')
print('Actual result:', positive_sum([]))
print('Expected result: 0')
print('Actual result:', positive_sum([-1,-2,-3,-4,-5]))

