def solution(number):
    """
    Input: Int -> Int
    produces the sum of all the multiples of 3 or 5 below the number passed in.
    If the number is a multiple of both 3 and 5, only count it once.
    """
    result = 0

    for num in range(number):
        if num % 3 == 0 and num % 5 == 0:
            result += num
        elif num % 3 == 0:
            result += num
        elif num % 5 == 0:
            result += num
    
    return result


#Test
print("Expected result:", 23)
print("Actual result:", solution(10))