# Bitwise Operators 
# Bitwise operators in Python allow us to manipulate binary numbers (0s and 1s)
# at the bit level. These operators perform operations directly on the binary
# representation of integers.

# Decimal	Binary
# 0	         0000
# 1	         0001
# 2	         0010
# 3	         0011
# 4	         0100
# 5       	 0101
# 6	         0110
# 7        	 0111
# 8   	     1000

# To get the binary representation of a number in Python:
print(bin(5))  # Output: '0b101'
print(bin(10)) # Output: '0b1010'

# 0b indicates that the number is in binary format.

# 1. Bitwise AND (&)
# AND operation returns 1 only if both bits are 1, otherwise returns 0.

a = 5  # Binary: 0101
b = 3  # Binary: 0011

result = a & b  # AND operation
print("5 & 3 =", result)  # Output: 1

# Explanation
#   0101   (5 in binary)
# & 0011   (3 in binary)
# --------
#   0001   (1 in decimal)

#------------------------------------------------------------------------------

# 2. Bitwise OR (|)
# OR operation returns 1 if at least one of the bits is 1.

a = 5  # 0101
b = 3  # 0011

result = a | b  # OR operation
print("5 | 3 =", result)  # Output: 7

# Explanation
#   0101   (5 in binary)
# | 0011   (3 in binary)
# --------
#   0111   (7 in decimal)

#------------------------------------------------------------------------------

# 3. Bitwise XOR (^)
# XOR returns 1 if the bits are different, otherwise returns 0.

a = 5  # 0101
b = 3  # 0011

result = a ^ b  # XOR operation
print("5 ^ 3 =", result)  # Output: 6

# Explanation
#   0101   (5 in binary)
# ^ 0011   (3 in binary)
# --------
#   0110   (6 in decimal)

#------------------------------------------------------------------------------

# 4. Bitwise NOT (~)
# NOT inverts all bits (flips 0 to 1 and 1 to 0).
# Python uses Two's Complement representation, so ~x is -(x+1).

a = 5  # 0101

result = ~a  # NOT operation
print("~5 =", result)  # Output: -6

# Explanation:

#   0101   (5 in binary)
# ~ 1010   (Inverted: -6 in Two's Complement)

# Formula: ~x = -(x + 1)

#------------------------------------------------------------------------------

# 5. Left Shift (<<)
# Left shifting moves bits to the left, filling with 0s. This effectively 
# multiplies the number by 2^n.

a = 5  # 0101

result = a << 1  # Shift left by 1
print("5 << 1 =", result)  # Output: 10

# Explanation

#   0101  (5 in binary)
# << 1
#  1010  (10 in decimal)

# Formula: x << n = x * (2^n)


# Another Example: 5 << 2 (Left Shift by 2)

a = 5  # Binary: 0101

result = a << 2  # Left shift by 2
print("5 << 2 =", result)  # Output: 20

# Step-by-Step Binary Calculation

# 5 in binary:  0000 0101  (5 in decimal)
# Left shift 2: 0001 0100  (20 in decimal)

#------------------------------------------------------------------------------

# 6. Right Shift (>>)
# Right shifting moves bits to the right, discarding the rightmost bit.
# This effectively divides the number by 2^n.

a = 5  # 0101

result = a >> 1  # Shift right by 1
print("5 >> 1 =", result)  # Output: 2

# Explanation

#   0101  (5 in binary)
# >> 1
#  0010  (2 in decimal)
# Formula: x >> n = x // (2^n)


# Another Example: 5 >> 2 (Right Shift by 2)
]
a = 5  # Binary: 0101

result = a >> 2  # Right shift by 2
print("5 >> 2 =", result)  # Output: 1

# Step-by-Step Binary Calculation

# 5 in binary:   0000 0101  (5 in decimal)
# Right shift 2: 0000 0001  (1 in decimal)




