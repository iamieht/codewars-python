def repeat_str(repeat, string):
    """
    Input: Int:String -> String
    produces a string repeated n times
    """
    return repeat*string

#Tests
print('Expected result: aaaa')
print('Actual result:', repeat_str(4, 'a'))
print('Expected result: hello hello hello ')
print('Actual result:', repeat_str(3, 'hello '))
print('Expected result: abcabc')
print('Actual result:', repeat_str(2, 'abc'))