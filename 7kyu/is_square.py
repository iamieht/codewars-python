import math
def is_square(n):
    """
    Input: Number -> Boolean
    produces True if input number is a perfect square, False otherwise
    """
    if n < 0:
        return False
    else:
        return int(math.sqrt(n)+0.5) ** 2 == n


#Test
print("Expected result:", False)
print("Actual result:", is_square(-1))
print("Expected result:", True)
print("Actual result:", is_square(0))
print("Expected result:", False)
print("Actual result:", is_square(3))
print("Expected result:", True)
print("Actual result:", is_square(4))
print("Expected result:", True)
print("Actual result:", is_square(25))
print("Expected result:", False)
print("Actual result:", is_square(26))
print("Expected result:", False)
print("Actual result:", is_square(2616647454))