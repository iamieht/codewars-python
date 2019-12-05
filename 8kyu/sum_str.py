def sum_str(a, b):
    '''a is String
       b is String
       returns sum in String'''
    return str(int(a or 0) + int(b or 0))

# Test
print(sum_str("", ""))