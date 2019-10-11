def getCount(inputStr):
    """
    Input: String -> Int
    produces the number of vowels in a string
    """
    num_vowels = 0
    for letter in inputStr:
        if letter in 'aeiouAEIOU':
            num_vowels += 1
  
    return num_vowels

#Tests
print("Expected result: 5")
print("Actual result:", getCount('abracadabra'))