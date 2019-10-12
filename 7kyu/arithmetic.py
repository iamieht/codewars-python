def arithmetic(a, b, operator):
    """
    Input: Number, Number, String -> Number
    produces a result from the arithmetic operation: add(+), subtract(+), multiply(*), divide(/)
    """
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    else:
        return a / b

    



#Test 
print("Expected result: 3")
print("Actual result:", arithmetic(1, 2, "add"))
print("Expected result: 6")
print("Actual result:", arithmetic(8, 2, "subtract"))
print("Expected result: 10")
print("Actual result:", arithmetic(5, 2, "multiply"))
print("Expected result: 4")
print("Actual result:", arithmetic(8, 2, "divide"))
