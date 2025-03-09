# Membership Operators
# Membership operators check if a value exists in a sequence.

# in	    Returns True if value exists
# not in	Returns True if value does not exist

nums = [1, 2, 3, 4, 5]

print(3 in nums)   # True   (3 exists)
print(8 in nums)   # False  (8 doesn't exist)

print(10 not in nums)  # True (10 doesn't exist)
print(4 not in nums)   # Flase (4 exists)