# Identity Operators
# Identity operators check if two variables refer to the same object in memory.

# is	    Returns True if both variables refer to the same object
# is not	Returns True if they do not

a = [1, 2, 3]
b = a     # Both point to the same memory location
c = [1, 2, 3]  # A different object with the same values (separate memory)

print( a is b)   # True  (same object)
print( a is c)   # False (different objects)

print( a is not c)  # True (different objects)
print( a is not b)  # False (same object)