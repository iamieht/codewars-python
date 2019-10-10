def sum_two_smallest_numbers(numbers):
    """
    Input: List -> Int
    produces the sum of the two lowest elements of the list
    """
    sortedNumbers = sorted(numbers)
    return sortedNumbers[0] + sortedNumbers[1]

#Test
print('Expected result: 7')
print('Actual result:', sum_two_smallest_numbers([19, 5, 42, 2, 77]))
print('Expected result: 3453455')
print('Actual result:', sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))