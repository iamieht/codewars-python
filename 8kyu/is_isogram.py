def is_isogram(string):
    checked_letters = ''
    
    for letter in string.lower():
        if letter in checked_letters:
            return False
        else:
            checked_letters += letter
    
    return True