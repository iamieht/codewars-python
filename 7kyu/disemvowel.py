def disemvowel(string):
    """
    Input: String -> String
    produces a new String without the vowels
    """
    new_string = ''
    for cha in string:
        if cha not in 'aeiouAEIOU':
            new_string += cha

    return new_string

#Test
print("Expected result:", "Ths wbst s fr lsrs LL!")
print("Actual result:", disemvowel("This website is for losers LOL!"))