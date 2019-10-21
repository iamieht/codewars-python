def find_outlier(integers):
    """
    Input: Array -> Int
    produces the only different number in terms of odd/even in the array
    """
    OddEven = {'odd': [],
               'even': []
               }

    for num in integers:
        if num % 2 == 0:
            OddEven['even'] += num,
        else:
            OddEven['odd'] += num,
    
    for value in OddEven.values():
        if len(value) == 1:
            return value[0]
    


        

#Test
print("Expected result:", 3)
print("Actual result:", find_outlier([2, 4, 6, 8, 10, 3]))
print("Expected result:", 11)
print("Actual result:", find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print("Expected result:", 160)
print("Actual result:", find_outlier([160, 3, 1719, 19, 11, 13, -21]))