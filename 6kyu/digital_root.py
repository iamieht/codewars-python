def digital_root(n):
    """
    Input: Int -> Int
    produces the recursive sum of all the digits in a number
    """
    listOfNums = list(str(n))
    result = 0

    while len(listOfNums) > 1:
        for digit in listOfNums:
            result += int(digit)
        
        listOfNums = list(str(result))

        if len(listOfNums) > 1:
            result = 0
    
    return result

def digital_root_recursive(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))



#Test
print("Expected result:", 7)
print("Actual result:", digital_root(16))
print("Expected result:", 6)
print("Actual result:", digital_root(456))