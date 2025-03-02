# Data Types

# 1. Numeric Data Types
#    int → Integer (whole number)
#    float → Decimal number
#    complex → Complex number (real + imaginary part)

# int (whole number)

a = 10       
print(type(a))   # <class 'int'>
print(a)         # 10

aa: int = 15  
print(type(aa))   # <class 'int'>
print(aa)         # 15


# float (decimal number)
b = 3.13     
print(type(b))   # <class 'float'>
print(b)         # 3.13

# complex number (2 is the real part, 3j is the imaginary part)
c = 2 + 3j   
print(type(c))   # <class 'complex'>
print(c)         # (2+3j)

#-----------------------------------------------------------------------

# 2. Sequence Data Types
#   str → String (Text)
#   list → A mutable (changeable) collection of elements. (array)
#   tuple → An immutable (unchangeable) collection.
#   range → Generates a sequence of numbers.


# str (string)
text = "Hello World!"
print(type(text))        # Output: <class 'str'>

# List
numbers = [1, 2, 3, 4]    # can be chnaged
print(type(numbers))      # Output: <class 'list'>
print(numbers[2])         # 3

# Tuple
fixed_values = (5, 6, 7)  # cannot be changed
print(type(fixed_values)) # Output: <class 'tuple'>
print(fixed_values[0])    # 5
# range
num_range = range(5)      # range generates numbers from 0 to 4
print(list(num_range))    # Output: [0, 1, 2, 3, 4]

#-----------------------------------------------------------------------

# 3. Set Data Types
#   set → Unordered collection of unique elements.(remove repeated data)
#   frozenset → Immutable version of a set.

# set
unique_numbers = {1, 2, 3, 4, 4}   # duplicates are removed
print(type(unique_numbers))     # Output: <class 'set'>
print(unique_numbers)           # Output: {1, 2, 3, 4}

# frozenset
immutable_set = frozenset({5, 6, 7, 8})  # cannot be modified
print(type(immutable_set))    # Output: <class 'frozenset'>



#-----------------------------------------------------------------------

# 4. Dictionary Data Type (dict)
# A dictionary stores data in key-value pairs (like objects)

person = {"name": "Saif", "age": 20, "city": "Karachi"}
print(type(person))     # Output: <class 'dict'>
print(person["city"])   # Karachi

#-----------------------------------------------------------------------

# 5. Boolean Data Type (bool)
# Used to represent True or False values.

is_python_fun = True
is_math_hard = False

print(type(is_python_fun))  # Output: <class 'bool'>
print(is_python_fun)        # Output: True

is_married: bool = False

#-----------------------------------------------------------------------
