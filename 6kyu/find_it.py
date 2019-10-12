def find_it(seq):
    """
    Input: Array -> Int
    produces the integer that appears an odd number of times
    """

    for element in seq:
        if not seq.count(element) % 2 == 0:
            return element


#Test
print("Expected result: 5")
print("Actual result:", find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))