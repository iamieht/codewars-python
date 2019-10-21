def basic_op(operator, value1, value2):
    """
    Input: operator -> String
           value1, value 2 -> Number -> Number
    produces a number after applying the chosen operator
    """

    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    else:
        return None



#Test
print("Actual result:", 11)
print("Expected result:", basic_op('+', 4, 7))
print("Actual result:", -3)
print("Expected result:", basic_op('-', 15, 18))
print("Actual result:", 25)
print("Expected result:", basic_op('*', 5, 5))
print("Actual result:", 7)
print("Expected result:", basic_op('/', 49, 7))