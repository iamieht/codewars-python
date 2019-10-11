def find_short(s):
    """
    Input: String -> Int
    produces the length of the shortest word in the string
    """
    listOfWords = s.split(' ')
    return min(map(len, listOfWords))


#Test
print("Expected result: 3")
print("Actual result:", find_short("bitcoin take over the world maybe who knows perhaps"))
print("Expected result: 3")
print("Actual result:", find_short("turns out random test cases are easier than writing out basic ones"))
print("Expected result: 3")
print("Actual result:", find_short("lets talk about javascript the best language"))
print("Expected result: 1")
print("Actual result:", find_short("i want to travel the world writing code one day"))
print("Expected result: 2")
print("Actual result:", find_short("Lets all go on holiday somewhere very cold"))

