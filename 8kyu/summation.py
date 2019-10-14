def summation(num):
    """
    Input: Int -> Int
    produces the summation of every number from 1 to num
    """
    result = 0
    for number in range(num+1):
        result += number
    
    return result
    

#Test
print("Expected result:", 1)
print("Actual result:", summation(1))
print("Expected result:", 36)
print("Actual result:", summation(8))
print("Expected result:", 253)
print("Actual result:", summation(22))
print("Expected result:", 5050)
print("Actual result:", summation(100))
print("Expected result:", 22791)
print("Actual result:", summation(213))