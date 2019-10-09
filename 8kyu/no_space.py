def no_space(x):
    '''Input: string
       Returns: string without spaces 
    '''
    new_string = ''

    for c in x:
        if not c == ' ':
            new_string += c
    
    return new_string

#########
# Better solution
def no_space_better(x):
    return x.replace(' ' ,'')

    



# Tests
print('Expected result: ', '8j8mBliB8gimjB8B8jlB')
print('Actual result: ', no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))
print('Actual result: ', no_space_better('8 j 8   mBliB8g  imjB8B8  jl  B'))