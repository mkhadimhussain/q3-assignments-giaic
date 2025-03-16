# Agentic AI - Python - Lesson 06 - Lists, Tuples & Dictionary

# 4. Tuples in Python
# A tuple is an ordered, immutable (unchangeable) sequence of elements. Tuples are useful for fixed data
# collections.

# In Python, a tuple is an immutable data type. This means that once a tuple is created, its elements 
# cannot be changed, added, or removed.

# 1. Cannot Modify Elements:
# Once a tuple is created, you cannot change its elements.

# 2. Cannot Add or Remove Elements:
# You cannot add new elements to a tuple or remove existing ones.

# Why Use Tuples?
# Immutable: Since tuples cannot be changed, they are safer to use when you want to ensure that the data
#  remains constant.

# Hashable: Tuples can be used as keys in dictionaries because they are immutable.

# Performance: Tuples are generally faster than lists because of their immutability.

# When to Use Tuples vs Lists
# Use tuples when you want to store data that should not change (e.g., coordinates, constants).

# Use lists when you need a collection that can be modified (e.g., adding or removing elements).

# Creating a Tuple
tuple1: tuple = tuple(["apple", "banana", "mango"])  # cast a list into tuple
tuple2: tuple = (10, 20, 30)    # tuple
mixed_tuple: tuple = ("hello", 5, 3.14, True)   # tuple

print("tuple1      =", tuple1)
print("tuple2      =", tuple2)
print("mixed_tuple =", mixed_tuple)
# tuple1      = ('apple', 'banana', 'mango')
# tuple2      = (10, 20, 30)
# mixed_tuple = ('hello', 5, 3.14, True)

# tuple3: tuple = tuple("cat", "dog", "cow")  
# TypeError: tuple expected at most 1 argument, got 3

#--------------------------------------------------------------------------------------------------

# Even though tuples are immutable, Python may create new instances in memory when you define identical 
# tuples in separate assignments. This is why id(tuple_1) and id(tuple_2) may differ.

tuple_1: tuple = (20, 40, 60)   # tuple
tuple_2: tuple = (20, 40, 60)   # tuple

print("id(tuple_1) = ", id(tuple_1))  # unique memory address
print("id(tuple_2) = ", id(tuple_2))  # unique memory address
# id(tuple_1) =  1469783762944
# id(tuple_2) =  1469783762944

# comparing by value
print("tuple_1 == tuple_2 = ", tuple_1 == tuple_2)
# tuple_1 == tuple_2 =  True

#--------------------------------------------------------------------------------------------------

# Why are Tuples Immutable?

# There are several reasons why tuples are immutable:

# - Memory Efficiency: Immutable tuples can be stored in a single block of memory, which makes them more
#   memory-efficient than lists.
# - Thread Safety: Immutable tuples are thread-safe, meaning that they can be safely accessed and shared 
#   between multiple threads without fear of modification.
# - Hashability: Immutable tuples are hashable, meaning that they can be used as keys in dictionaries.

# lets create an error.
tuple5: tuple = ("apple", "mango", "orange", "grapes")

# tuple5[0] = 'Watermelon'  # immutable

# TypeError: 'tuple' object does not support item assignment

#--------------------------------------------------------------------------------------------------
# Tuples in Python

# A tuple is an `ordered`, `immutable` (unchangeable) sequence of elements.
# Tuples are useful for fixed data collections.

# Creating a Tuple
tuple1: tuple = tuple(["apple", "banana", "mango"])  # cast a list into tuple
tuple2: tuple = (10, 20, 30)    # tuple
mixed_tuple: tuple = ("hello", 5, 3.14, True)   # tuple

print("tuple1      =", tuple1)
print("tuple2      =", tuple2)
print("mixed_tuple =", mixed_tuple)
# tuple1      = ('apple', 'banana', 'mango')
# tuple2      = (10, 20, 30)
# mixed_tuple = ('hello', 5, 3.14, True)


# Accessing elements in a tuple
print("tuple1[0] = ", tuple1[0])  # accessing first element
# tuple1[0] =  apple


# Tuple slicing
print("tuple2[1:] = ", tuple2[1:])  # slicing from index 1 till end
# tuple2[1:] =  (20, 30)


# Tuple lenght
print("Length of tuple1: ", len(tuple1))
# Length of tuple1:  3


# Iterating through a tuple
print("Iterating through tuple2:")
for item in tuple2:
    print(item)
# Iterating through tuple2:
# 10
# 20
# 30


# Checking if an item exists in a tuple
print("Is 20 in tuple2?", 20 in tuple2)  # Is 20 in tuple2? True
print("Is 89 in tuple2?", 89 in tuple2)  # Is 89 in tuple2? False


# Concantenating tuples
tuple4: tuple = tuple1 + tuple2
print("tuple1 + tuple2 = ", tuple4)
# tuple1 + tuple2 =  ('apple', 'banana', 'mango', 10, 20, 30)


# Repeating tuples
tuple5: tuple = tuple2 * 2
print("tuple2 * 2 =", tuple5)
# tuple2 * 2 = (10, 20, 30, 10, 20, 30)


# Nested tuples
nested_tuple = (tuple1,  tuple2)
print("nested_tuple =", nested_tuple)
# nested_tuple = (('apple', 'banana', 'mango'), (10, 20, 30))


# unpacking tuples
a, b, c = tuple1
print("unpacking tuple1:", a, b, c)
# unpacking tuple1: apple banana mango


# Using tuples as keys in dictionaries (because they are immutable)
my_dict = {tuple1: "This is a tuple key", tuple2: "Another tuple key"}
print("Dictionary with tuple keys:", my_dict)
# Dictionary with tuple keys: {('apple', 'banana', 'mango'): 'This is a tuple key', (10, 20, 30): 'Another tuple key'}


#Trying to modify a tuple will result in a TypeError
# tuple[0] = 'Watermelon'  #immutable. This line will raise an error
# TypeError: 'type' object does not support item assignment

#--------------------------------------------------------------------------------------------------

# positive indexing
print(tuple1[0])     # apple

# negative indexing
print(tuple1[-3])    # apple

# item count
print(tuple1.count("apple"))  # 1

# index of item
print(tuple1.index("apple"))  # 0

#--------------------------------------------------------------------------------------------------

# Errors
# AttributeError: 'tuple' object has no attribute 'method name'

# tuple1.sort()  
# tuple1.reverse()   
# tuple1.append("kiwi")
# tuple1.extend(["pineapple", "grapes"])
# tuple1.remove("banana")
# deleted = tuple1.pop(1)

#--------------------------------------------------------------------------------------------------

# prompt: print the complete list of methods and attribute of tuple, dont include dunders

# Get a list of all attributes and methods of a tuple

# Formula
# new_list = [expression for element in iterable if condition]

tuple_methods: list = [method for method in dir(tuple) if not method.startswith('__')]

# Print the list of methods (excluding dunder methods)
print(tuple_methods)
# ['count', 'index']

#--------------------------------------------------------------------------------------------------

# Python is Type Hint Language
a: int = input("Enter your name: ")
print(a, type(a))
# Enter your name: saif
# saif <class 'str'>

# Enter your name: 78
# 78 <class 'str'>

# Type Hinting (a: int)
# - a: int is a type hint, which suggests that the variable 'a' is expected to be an integer.
# - However, type hints are not enforced in Python. They are only for documentation and tools like 
#   linters or type checkers.
# - The actual value assigned to 'a' will still be a string, because input() always returns a string.

#--------------------------------------------------------------------------------------------------
