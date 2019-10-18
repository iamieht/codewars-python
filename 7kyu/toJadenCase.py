def toJadenCase(string):
    """
    Input: String -> String
    produces a new string with each word capitalized
    """
    toJadenListString = string.split()
    toJadenString = ''
    for cha in toJadenListString:
        toJadenString += cha.capitalize() + ' '
    
    return toJadenString[:-1]

def toJadenCaseBetter(string):        
    return " ".join(w.capitalize() for w in string.split())
    
#Test
print("Expected result:", "How Can Mirrors Be Real If Our Eyes Aren't Real")
print("Actual result:", toJadenCase("How can mirrors be real if our eyes aren't real"))