def high_and_low(numbers):
    """
    Input: String -> String
    produces the min and max value in the string
    """
    new_string = numbers.rsplit(' ')
    listofNumbers = list(map(int, new_string))
    return str(max(listofNumbers)) + ' ' + str(min(listofNumbers)) 


def high_and_low_clever(numbers):
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

#Test
print("Expected result: 542 -214")
print("Actual result:", high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))

#Test high_and_low_clever
print("Expected result: 542 -214")
print("Actual result:", high_and_low_clever("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))