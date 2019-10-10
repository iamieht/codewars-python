def remove_char(s):
    """
    String -> String
    produces a new string (s) without the first and last character
    """
    return s[1:-1]

#Tests
print('Expected result: loquen')
print('Actual result:', remove_char('eloquent'))
print('Expected result: ountr')
print('Actual result:', remove_char('country'))
print('Expected result: erso')
print('Actual result:', remove_char('person'))
print('Expected result: lac')
print('Actual result:', remove_char('place'))
print('Expected result: ')
print('Actual result:', remove_char('ok'))
