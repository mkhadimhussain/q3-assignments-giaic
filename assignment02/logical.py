# Logical Operators
# Logical operators are used for combining multiple conditions.

# and	Returns True if both conditions are True
# or	Returns True if at least one condition is True
# not	Reverses the boolean value

p, q = True, False

print(p and q)    # False (both must be True)
print(False and False)  # False
print(True and True)    # True

print(p or q)   # True (at least one is True)
print(not p)    # False (negates p)
print(not q)    # True
