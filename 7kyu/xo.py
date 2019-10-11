def xo(s):
    """
    Input: String -> Boolean
    produces True if the number of 'x' and 'o' are the same
    """
    x = s.count('x') + s.count('X')
    o = s.count('o') + s.count('O')

    return x == o

def xo_better(s):
    s = s.lower()
    return s.count('x') == s.count('o')

#Test
print("Expected result: True")
print("Actual result:", xo('xo'))
print("Expected result: True")
print("Actual result:", xo('xo0'))
print("Expected result: False")
print("Actual result:", xo('xxxoo'))