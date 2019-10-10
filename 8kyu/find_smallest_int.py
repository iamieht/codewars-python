def find_smallest_int(arr):
    """
    Input: List -> Int
    produces the minimun integer in a list
    """
    return min(arr)

#Test
print("Expected result: 11")
print("Actual result:", find_smallest_int([78, 56, 232, 12, 11, 43]))
print("Expected result: -33")
print("Actual result:", find_smallest_int([78, 56, -2, 12, 8, -33]))
print("Expected result:", 1-2**64)
print("Actual result:", find_smallest_int([0, 1-2**64, 2**64]))