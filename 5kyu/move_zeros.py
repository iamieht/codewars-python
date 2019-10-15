def move_zeros(array):
    """
    Input: Array -> Array
    produces an array with all zeros at the end, preserving the order of the rest of the elements
    """
    zeros = []
    output = []

    for element in array:
        if element == 0 and element is not False:
            zeros.append(element)
        else:
            output.append(element)
    
    output.extend(zeros)
    return output






#Test
print("Expected result:", [ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
print("Actual result:", move_zeros([1,2,0,1,0,1,0,3,0,1]))
print("Expected result:", [9,9,1,2,1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
print("Actual result:", move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
print("Expected result:", ["a","b","c","d",1,1,3,1,9,9,0,0,0,0,0,0,0,0,0,0])
print("Actual result:", move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9]))
print("Expected result:", ["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])
print("Actual result:", move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))
print("Expected result:", [1,None,2,False,1,0,0])
print("Actual result:", move_zeros([0,1,None,2,False,1,0]))
print("Expected result:", ["a","b"])
print("Actual result:", move_zeros(["a","b"]))
print("Expected result:", ["a"])
print("Actual result:", move_zeros(["a"]))
print("Expected result:", [0,0])
print("Actual result:", move_zeros([0,0]))
print("Expected result:", [0])
print("Actual result:", move_zeros([0]))
print("Expected result:", [False])
print("Actual result:", move_zeros([False]))
print("Expected result:", [])
print("Actual result:", move_zeros([]))