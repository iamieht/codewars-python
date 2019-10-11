def get_middle(s):
    """
    Input: String -> String
    produces the middle character of a string. If # of chars is pair returns 2 middle char, 1 otherwise
    """
    if len(s) % 2 == 0:
        return s[len(s)//2 - 1:len(s)//2 + 1]
    else:
        return s[len(s)//2]


def get_middle_better(s):
   return s[(len(s)-1)//2:len(s)//2+1]

#Test
print("Expected result: es")
print("Actual result:", get_middle("test"))
print("Expected result: t")
print("Actual result:", get_middle("testing"))
print("Expected result: dd")
print("Actual result:", get_middle("middle"))
print("Expected result: A")
print("Actual result:", get_middle("A"))
print("Expected result: of")
print("Actual result:", get_middle("of"))

#Test get_middle_better
print("Expected result: es")
print("Actual result:", get_middle_better("test"))
print("Expected result: t")
print("Actual result:", get_middle_better("testing"))
print("Expected result: dd")
print("Actual result:", get_middle_better("middle"))
print("Expected result: A")
print("Actual result:", get_middle_better("A"))
print("Expected result: of")
print("Actual result:", get_middle_better("of"))