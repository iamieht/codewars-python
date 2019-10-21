def longest(s1, s2):
    """
    Input: s1 String
            s2 String
            produces String
    Return a new sorted string, the longest possible, containing distinct letters
    """
    temp = set()
    tempString = s1 + s2
    
    for char in tempString:
        temp.add(char)
    
    return ''.join(sorted(temp))

def longest_better(a1, a2):
    return "".join(sorted(set(a1 + a2)))

#Test
print("Expectec result:", "aehrsty")
print("Actual result:", longest("aretheyhere", "yestheyarehere"))
print("Expectec result:", "abcdefghilnoprstu")
print("Actual result:", longest("loopingisfunbutdangerous", "lessdangerousthancoding"))
print("Expectec result:", "acefghilmnoprstuy")
print("Actual result:", longest("inmanylanguages", "theresapairoffunctions"))