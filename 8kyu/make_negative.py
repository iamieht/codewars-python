def make_negative(number):
    """
    Input: Number -> Number
    produces a negative number if input is positive, if negetive, remains unchanged.
    """
    if number < 0:
        return number
    else:
        return -number


#Test
print("Expected result: -42")
print("Actual result:", make_negative(42))