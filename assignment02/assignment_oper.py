# Assignment Operators
# Assignment operators assign values to variables.

# Operator 	Example  	Equivalent To
# =	        a = 10  	Assigns 10 to a
# +=	    a += 5	    a = a + 5
# -=	    a -= 5	    a = a - 5
# *=	    a *= 5	    a = a * 5
# /=	    a /= 5	    a = a / 5
# //=	    a //= 5	    a = a // 5
# %=	    a %= 5	    a = a % 5
# **=	    a **= 2	    a = a ** 2

x = 10

x += 5  # x = x + 5
print("Addition Assignment: ", x)  # 15

x -= 3  # x = x - 3
print("Subtraction Assignment: ", x)  # 12

x *= 2  # x = x * 2
print("Multiplication Assignment: ", x)  # 24

x /= 5  # x = x / 5
print("Division Assignment: ", x)  # 4.8

x //= 2 # x = x // 2
print("Floor Division Assignment: ", x)  # 2.0

x **= 3 # x = x ** 3
print("Exponentiation Assignment: ", x)  # 8.0

x %= 3 # x = x % 3
print("Modulus Assignment: ", x)  # 2.0
