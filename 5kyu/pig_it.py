def pig_it(text):
    """
    Input: String -> String
    produces a new string with the first letter moved to the end of it + "ay". Punctuation marks are untouched.
    """
    new_string = ''
    listOfChars = text.split(' ')

    for char in listOfChars:
        if char in '.-;?!':
            new_string += ' ' + char
        else:
            new_string += ' ' + char[1:] + char[0] + 'ay'
    
    return new_string[1:]

            
def pig_it_clever(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])


#Test
print("Expected result: igPay atinlay siay oolcay")
print("Actual result:", pig_it("Pig latin is cool"))
print("Expected result: hisTay siay ymay tringsay")
print("Actual result:", pig_it("This is my string"))
print("Expected result: uisQay ustodietcay psosiay ustodescay ?")
print("Actual result:", pig_it("Quis custodiet ipsos custodes ?"))