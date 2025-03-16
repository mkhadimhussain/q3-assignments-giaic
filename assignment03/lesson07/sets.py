# Agentic AI - Python - Lesson 07 - The Set, Frozenset & GC

# The Set Data Type
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are
# List, Tuple, and Dictionary, all with different qualities and usage.

# A set is:
# - unordered
# - unchangeable
# - unindexed

# An object cannot appear more than once in a set, whereas in List and Tuple, same object can appear
# more than once.

my_set: set = {123, 457, 5, 6}
my_set2: set = set([123, 457, 5, 6])

print("my_set            = ", my_set)
print("my_set2           = ", my_set2)
print("type(my_set)      = ", type(my_set))
print("type(my_set2)     = ", type(my_set2))
print("my_set == my_set2 = ", my_set == my_set2)  # True

# my_set            =  {457, 123, 5, 6}
# my_set2           =  {457, 123, 5, 6}
# type(my_set)      =  <class 'set'>
# type(my_set2)     =  <class 'set'>
# my_set == my_set2 =  True

#---------------------------------------------------------------------------------------------------

# Holds only Immutable Objects
# A set can store only immutable objects such as number (int, float, complex or bool), string or tuple. 
# If you try to put a list or a dictionary in the set collection, Python raises a TypeError.

# Lets check set if it can hold mutable object like list[]

# my_set: set = {[123, 345, 5, 6]}  # TypeError: unhashable type: 'list'
# print(my_set)    

#---------------------------------------------------------------------------------------------------

# It can hold multiple data types at once.
multi_set: set = {5, 8.3, False, True, "Hello World", (7, 3, 6, 'hi')}
print(multi_set)  # {False, True, (7, 3, 6, 'hi'), 5, 8.3, 'Hello World'}

#---------------------------------------------------------------------------------------------------

# The set is unordered
# Note that items in the set collection may not follow the same order in which they are entered. 
# The position of items is optimized by Python to perform operations over set as defined in mathematics.

set2: set = {'Java', 'Python', 'JavaScript', 'java'}
print(set2)   # {'java', 'Java', 'Python', 'JavaScript'}

# "Python sets are unordered collections, but internally, elements are stored based on their hash values.
# However, this internal structure is not predictable or stable across operations".
# We will dive in to the details of hashing later in this tutorial.

#---------------------------------------------------------------------------------------------------

# The set is Unchangeable
# When we say that set items are unchangeable, it means that you cannot modify an individual item 
# in a set directly. However, you can add or remove items from the set.

# Here is an example to illustrate this concept:

# create a set
my_set: set = {1, 2, 3, 4, 5}
print(my_set)  # {1, 2, 3, 4, 5}

# Try to change an item (this will raise an error)
try:
    my_set[0] = 10   # Sets are unordered, so indexing doesn't work.
except TypeError as e:  
    print(e)     # Output: 'set' object does not support item assignment

#---------------------------------------------------------------------------------------------------

# Create a set
my_set2: set = {10, 20, 30, 40, 50}
print(my_set2)

# Try to change an item (this will raise an error)
try:
    my_set2[0] = 90  # Sets are unirdered, so indexing doesn't work
except TypeError as e:
    print("*TypeError* ABC :", e)  # *TypeError* ABC : 'set' object does not support item assignment

print("Program execution continues as normal because we handle the error condition in try except block")
# Program execution continues as normal because we handle the error condition in try except block

#---------------------------------------------------------------------------------------------------

# As you can see, you can't change an individual item in a set directly. Instead, you can remove the 
# item and add a new one with the updated value. Alternatively, you can use the discard() or remove()
# methods to remove items and the add() or update() methods to add new items.

my_set: set = {1, 2, 3, 4, 5, "A", "a"}
print(my_set)   # {'a', 1, 2, 3, 4, 5, 'A'}

# Remove an item
my_set.remove(3)
my_set.remove("A")
print(my_set)  # {'a', 1, 2, 4, 5}

# Add an item
my_set.add(6)
print(my_set)  # {1, 2, 4, 5, 6, 'a'}

#---------------------------------------------------------------------------------------------------

my_set2: set = {10, 20, 30, 40, "B", "b"}
print(my_set2)

print(my_set2.discard(40))   # removes 40 and output: None

# discard() only removes a single element
# {10, 20, 30} is a set itself, not an element within my_sets
# Therefore, discard does not find it and returns None, without modifying the set.
print(my_set2.discard({10, 20, 30}))  # None

print("After: my_set2 =", my_set2) # After: my_set2 = {20, 'B', 30, 10, 'b'} 

# To remove multiple elements, iterate and discard each one individually:
for item in {10, 20, 30}:
    my_set2.discard(item)
print("After removing multiple elements: my_set2 = ", my_set2)
# After removing multiple elements: my_set2 =  {'b', 'B'}

#---------------------------------------------------------------------------------------------------

# Use difference_update() method to remove multiple element at once.
my_set3: set = {2, 4, 6, 8, "C", "c"}
print("Before: my_set3 :", my_set3)
# Before: my_set3 : {2, 4, 'c', 6, 'C', 8}

my_set3.difference_update({2, 6, "c"})
print("After: my_set3 :", my_set3)
# After: my_set3 : {4, 'C', 8}

#---------------------------------------------------------------------------------------------------

# Add multiple items
my_set3.update([1, 2, 3, "hello"])
print(my_set3)   # {1, 2, 3, 4, 8, 'C', 'hello'}

#--------------------------------------------------------------------------------------------------

# Using the union() method or | operator:

# In Python, the union() method or the | operator is used to combine two sets into a single set. This 
# operation returns a new set containing all unique elements from both sets.

# Using the union() method:

# The union() method is a built-in method of the set data type in Python. It takes an iterable (such as 
# a set, list, or tuple) as an argument and returns a new set containing all unique elements from both 
# the original set and the iterable.

set1: set = {10, 22, 33, 4, 5}
set2: set = {5, 6, 7}

set3: set = set1.union(set2)
print(set3)   # {33, 4, 5, 22, 6, 7, 10}

#--------------------------------------------------------------------------------------------------

# Using the | operator:

# The | operator is a binary operator that can be used to combine two sets into a single set. It has the 
# same effect as the union() method, but is often more concise and readable.

set4: set = set1 | set2 
print(set4)   # {33, 4, 5, 22, 6, 7, 10}

# Key aspects of union() and | operator:

# - Unique elements: The resulting set contains only unique elements from both sets.
# - Order does not matter: The order in which the sets are combined does not affect the result.
# - Original sets remain unchanged: The original sets are not modified by the union operation.

#--------------------------------------------------------------------------------------------------

# Unique Elements
# Note that sets only store unique elements, so if you try to add a duplicate item, it will be ignored. For example:

my_set4: set = {1, 3, 5, 7, "Python"} 
print("Before:", my_set4)  # Before: {1, 'Python', 3, 5, 7}

my_set4.add(5)
my_set4.add("Python")

print("After:", my_set4)  # After: {1, 3, 5, 7, 'Python'}

#--------------------------------------------------------------------------------------------------

# discard() and remove() methods
# In Python, both discard() and remove() methods are used to remove items from a set. However, there is a 
# key difference between the two methods:

# 1. remove() method:

# - The remove() method removes the specified item from the set.
# - If the item is not found in the set, it raises a KeyError.
# - This method is suitable when you are sure that the item exists in the set.

# 2. discard() method:

# - The discard() method also removes the specified item from the set.
# - However, if the item is not found in the set, it does not raise any error. It simply does nothing.
# - This method is suitable when you are not sure if the item exists in the set.

# Here's an example to illustrate the difference:

# Lets create an error to understand
my_set6: set = {1,2,3}

# my_set6.remove(4)
# print(my_set6)   # KeyError: 4

# Now trying with discard
my_set6.discard(4) # method
print(my_set6)   # {1, 2, 3}

#--------------------------------------------------------------------------------------------------

print("Before pop() = ", my_set6)

#When you call `my_set.pop()`, it removes and returns an arbitrary element from the set.
#Since sets are unordered data structures, the element that is removed and returned is not predictable.
my_set6.pop()
print("After pop() = ", my_set6)

# Before pop() =  {1, 2, 3}
# After pop() =  {2, 3}

#--------------------------------------------------------------------------------------------------

# In summary:

# - Use remove() when you are sure that the item exists in the set and you want to handle the error if
#   it does not exist.

# - Use discard() when you are not sure if the item exists in the set and you want to avoid raising an
#   error if it does not exist.

# When to use each method:

# remove():
# - When working with small sets where performance is not a concern.
# - When you need to handle the error if the item does not exist.

# discard():
# - When working with large sets where performance is a concern.
# - When you do not care about handling the error if the item does not exist.

# In general, if you are not sure which method to use, discard() is a safe choice as it does not raise an
# error if the item does not exist.

#--------------------------------------------------------------------------------------------------

# The Inner Working of SET (Advance Topic)

# The Hashing
# - Hashing is a mechanism in computer science which enables quicker searching of objects in computer's
#   memory. Only immutable objects are hashable.

# - Immutable data types in Python come with a built-in method for computing their hash value, which is
#   called hash.

# - A hash table is a data structure that can map keys to values and that implements a hash function to 
#   compute the index to an array of buckets or slots

a: str = "Hello World!"
b: str = "Hello World!"

print("id(a):", id(a))
print("id(b):", id(b))
# id(a): 2078956827504
# id(b): 2078956827504

#--------------------------------------------------------------------------------------------------

print("hash(a):", hash(a))
print("hash(b):", hash(b))
print("---------------")
print("hash(a)      = ",hash(a))
print("a.__hash__():", a.__hash__())  # __dunder__()

# hash(a): -7031855288120552143
# hash(b): -7031855288120552143
# ---------------
# hash(a)      =  -7031855288120552143
# a.__hash__(): -7031855288120552143

#--------------------------------------------------------------------------------------------------

# Important Note:
# - Even if a set only allows immutable items, the set itself is mutable. Hence, add/delete/update operations 
# are permitted on a set object

# - In Python, a dictionary key must be an immutable object, meaning its value cannot be changed after it's 
# created. This is because dictionaries use a hash table to store key-value pairs, and mutable objects 
# cannot be hashed.

# - Lets pass the set as key in dictionary which only accept immutable item as a key.

# TypeError: unhashable type: 'set'
# my_set: set   = {1,2,3,4,5, "Hello! World"}
# my_dict: dict = {my_set: "Hello! World"} # dictionary only accept immutable objects as a key
# print(my_dict)
# TypeError: unhashable type: 'set'

#--------------------------------------------------------------------------------------------------

# How Hashing Determines Internal Storage in Sets

# In Python, sets are implemented using hash tables (specifically, dictionaries under the hood). This 
# allows O(1) average-time complexity for lookups, insertions, and deletions. However, the way elements 
# are stored in memory depends on hashing, which can lead to unpredictable ordering.

# Key Points About Hashing in Sets:
# 1- Each element in a set is hashed to determine its storage position.

# 2- The internal order is based on hash values, not insertion order.

# 3- The order can change dynamically when elements are added or removed.

#--------------------------------------------------------------------------------------------------

# Understanding Rehashing and Changing Order

# What is Rehashing?
# - Rehashing occurs when the underlying hash table needs to expand due to increasing elements.

# - Python dynamically resizes the hash table when it reaches a certain load factor (a ratio of stored 
#   elements to available slots).

# - During rehashing, all elements get redistributed, meaning their storage positions can change, even 
#   if no explicit sorting is done.

# Example: How Set Order Can Change Dynamically

# Initial set
my_set7: set = {20, 9, 3, 8}
print(my_set7)  # output may be {8, 9, 3, 20} or another order

# Adding an element
my_set7.add(30)
print(my_set7)  # The order might change unpredictably

# Removing an element
my_set7.remove(20)
print(my_set7)  # Again, the order can change

# {8, 9, 3, 20}
# {3, 8, 9, 20, 30}
# {3, 8, 9, 30}

#--------------------------------------------------------------------------------------------------

# Why Does the Order Change?

# - New elements may trigger rehashing, leading to reallocation of storage.
# - Removing an element can also affect the layout, especially if rehashing is triggered due to shrinking.

# Does This Mean Sets Are Ordered Internally?
# 🚫 No.
# Even though elements are stored based on their hash values, this does not mean sets are ordered in the 
# way lists or tuples are. Order can change unexpectedly, so it’s unreliable for ordered operations like
# indexing.

# Conclusion
# - Hashing determines where elements are stored, but this structure is not stable across operations.
# - Adding or removing elements can trigger rehashing, which causes internal storage reallocation and an 
#   unpredictable order.

#--------------------------------------------------------------------------------------------------
