def persistence(n):
    """
    Input: Num -> Int
    produces the number of times you must multiply the digits in num until you reach a single digit.
    """

    listofNums = list(str(n))
    result = 1
    count = 0
    while len(listofNums) > 1:

        for element in listofNums:
            result = result * int(element)
        
        listofNums = list(str(result))
        result = 1
        count += 1
    

    return count


#Test
print("Expected result: 3")
print("Actual result:", persistence(39))
print("Expected result: 0")
print("Actual result:", persistence(4))
print("Expected result: 2")
print("Actual result:", persistence(25))
print("Expected result: 4")
print("Actual result:", persistence(999))