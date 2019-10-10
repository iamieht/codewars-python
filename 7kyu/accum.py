def accum(s):
    """
    Input: String -> String
    produces a String with the first character in uppercase and each letter * index of the character. All separeted by '-'
    """
    count = 1
    numberOfLetters = len(s)
    new_string = ''
    idx = 0
    while numberOfLetters >= count:
        new_string += (s[idx] * count).capitalize()
        if count < numberOfLetters:
            new_string += '-'
        count += 1
        idx += 1
    
    return new_string


def accum_clever(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))


#Test
print("Expected result: A-Bb-Ccc-Dddd")
print("Actual result:", accum("abcd"))
print("Expected result: R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy")
print("Actual result:", accum("RqaEzty"))
print("Expected result: C-Ww-Aaa-Tttt")
print("Actual result:", accum("cwAt"))

#Test accum_clever
print("Expected result: A-Bb-Ccc-Dddd")
print("Actual result:", accum_clever("abcd"))
print("Expected result: R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy")
print("Actual result:", accum_clever("RqaEzty"))
print("Expected result: C-Ww-Aaa-Tttt")
print("Actual result:", accum_clever("cwAt"))