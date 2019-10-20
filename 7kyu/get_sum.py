def get_sum(a,b):
    """
    Input:  a -> Number
            b -> Number
            returns a Number
    produces the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.
    """
    if a == b:
        return a
    else:
        return sum(list(range(min(a,b), max(a,b)+1)))

    

#Test
print("Expected result:", 1)
print("Actual result:", get_sum(0,1))
print("Expected result:", -1)
print("Actual result:", get_sum(0,-1))
print("Expected result:", -1)
print("Actual result:", get_sum(-1,0))