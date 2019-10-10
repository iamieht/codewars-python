def even_or_odd(number):
    '''
    num -> string
    produces "Odd" if number is odd, "Even" otherwise
    '''
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

#Tests
print('Expected result: even_or_odd(2)', 'Even')
print('Actual result:', even_or_odd(2))
print('Expected result: even_or_odd(0)', 'Even')
print('Actual result:', even_or_odd(0))
print('Expected result: even_or_odd(7)', 'Odd')
print('Actual result:', even_or_odd(7))
print('Expected result: even_or_odd(1)', 'Odd')
print('Actual result:', even_or_odd(1))
print('Expected result: even_or_odd(-1)', 'Odd')
print('Actual result:', even_or_odd(-1))
