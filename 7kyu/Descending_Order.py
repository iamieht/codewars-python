def Descending_Order(num):
    """
    Input: Int -> Int
    produces a new integer in descending order
    """
    elements = str(num)
    return int(''.join(sorted(elements, reverse=True)))


#Test
print("Expected result: 0")
print("Actual result:", Descending_Order(0))
print("Expected result: 51")
print("Actual result:", Descending_Order(15))
print("Expected result: 987654321")
print("Actual result:", Descending_Order(123456789))