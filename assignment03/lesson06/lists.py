# Agentic AI - Python - Lesson 06 - Lists, Tuples & Dictionary

# Working with Lists and Tuples

# Introduction
# Python provides powerful sequence types: lists and tuples. These data structures help store and manage 
# collections of data efficiently.

#-----------------------------------------------------------------------------------------------

# 1. Lists in Python

# 1- Ordered: Lists are ordered, meaning that the items in the list have a specific order and can be
#    accessed by their index.
# 2- Mutable: Lists are mutable, meaning that they can be modified after they are created.
# 3- Indexed: Lists are indexed, meaning that each item in the list has a specific index that can be 
#    used to access it.
# 4- Dynamic size: Lists can grow or shrink dynamically as elements are added or removed.
# 5- Heterogeneous: Lists can contain elements of different data types, such as integers, strings,
#    floats, and other lists.
# 6- Supports duplicate values: Lists can contain duplicate values.


# Creating lists with different data types
fruits: list = ["apple", "banana", "mango"]
numbers: int = [10, 20, 30, 40, 50]
mixed: list = ["Hello", 24, 3.14, True]

print("fruits  = ", fruits)
print("numbers = ", numbers)
print("mixed   = ", mixed)

# fruits  =  ['apple', 'banana', 'mango']
# numbers =  [10, 20, 30, 40, 50]
# mixed   =  ['Hello', 24, 3.14, True]

#-----------------------------------------------------------------------------------------------

# Accessing List Elements
# You can access elements using indexing (starting from 0) and negative indexing (starting from -1).

fruits: list = ["apple", "banana", "mango"]
print(fruits[0])  # apple
print(fruits[1])  # banana
print(fruits[-1]) # mango, accessing element in reverse order
print(fruits[-3]) # apple, accessing element in reverse order

#-----------------------------------------------------------------------------------------------

# Modifying Lists
# Lists are mutable, meaning their elements can be changed.

fruits: list = ["apple", "banana", "mango"]
fruits[-3] = "orange"  # replacing "apple" with "orange"
print(fruits)  
# ['orange', 'banana', 'mango']

#-----------------------------------------------------------------------------------------------

# List Slicing
# Extract multiple elements using slicing.

print(fruits[0:2])  # 0 and 1
# ['orange', 'banana']

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

# 2. Common List Methods
# Lists provide built-in methods for efficient data manipulation.

# Appending and Extending Lists

# Add a single element
fruits.append("watermelon")  # add a single element 'watermelon' to the end
print(fruits)   # ['orange', 'banana', 'mango', 'watermelon']

# Add a multiple elements
fruits.extend(["cherry", "kiwi"])  # Adds multiple elements
print(fruits)  # ['orange', 'banana', 'mango', 'watermelon', 'cherry', 'kiwi']

#-----------------------------------------------------------------------------------------------

# Removing Elements
# In Python, remove() and pop() are two distinct methods used to manipulate lists. While they may 
# seem similar, they have different purposes and behaviors.

# Remove() Method
# The remove() method is used to delete the first occurrence of a specified value from a list. 
# If the value is not found in the list, a ValueError exception is raised.

# Key aspects of remove():

# - Value-based: remove() searches for a specific value in the list.
# - Returns None: The remove() method does not return any value.
# - Raises ValueError: If the value is not found in the list, a ValueError exception is raised.

fruits.remove("banana") # Removes 'banana' # run multiple times to see error as "banana" is already removed
print(fruits)   # ['orange', 'mango', 'watermelon', 'cherry', 'kiwi']

# fruits.remove("banana") # ValueError: list.remove(x): x not in list

# fruits.remove(0)  # ValueError: list.remove(x): x not in list

# Returns None
removed_element = fruits.remove("kiwi")
print("removed element: ", removed_element)  # removed element:  None

#-----------------------------------------------------------------------------------------------

# Pop() Method
# The pop() method is used to delete an item at a specified index from a list. If no index is provided,
# it removes and returns the last item in the list.

# Key aspects of pop():

# - Index-based: pop() searches for an item at a specific index in the list.
# - Returns the removed item: The pop() method returns the item that was removed from the list.
# - Raises IndexError: If the index is out of range, an IndexError exception is raised.

deleted = fruits.pop(1) # Removes and returns the element at index 1 # run it multiple time to see error
print("deleted element :", deleted)  # deleted element : mango
print(fruits)  # ['orange', 'watermelon', 'cherry', 'kiwi']

#-----------------------------------------------------------------------------------------------

# Sorting a List

# 1. Default Sorting (Ascending Order)
numbers: list[int] = [7, 3, 1, 9, 5, 2, 1]  # unorderd list
numbers.sort()
print(numbers)   # [1, 1, 2, 3, 5, 7, 9]

#-----------------------------------------------------------------------------------------------

# 2. Sorting in Descending Order (reverse=True)
numbers: list[int] = [3, 5, 9, 1]
numbers.sort(reverse=True)
print(numbers)  # [9, 5, 3, 1]

#-----------------------------------------------------------------------------------------------

# 3. Sorting by String length (key=len)
animals = ["Goat", "Cat", "Tiger", "Dog"]
animals.sort(key=len)
print(animals)  # ['Cat', 'Dog', 'Goat', 'Tiger']

#-----------------------------------------------------------------------------------------------

# 4. Sorting by Last Character (key=lambda word: word[-1])
words = ["famous", "zoo", "banana", "talk", "apple"]
words.sort(key=lambda word: word[-1])
print(words)  # ['banana', 'apple', 'talk', 'zoo', 'famous']

#-----------------------------------------------------------------------------------------------

# 5. Reverse Sorting
numbers = [2, 4, 6, 8, 10]
numbers.reverse()
print(numbers)   # [10, 8, 6, 4, 2]

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

# 3. Iterating Over Lists
# Use loops to process elements in a list.

# Using a for-loop
fruits = ["pineapple", "cherry", "apple"]
for fruit in fruits:
    print(fruit)
# pineapple
# cherry
# apple

#-----------------------------------------------------------------------------------------------

# Using list comprehension

# List comprehension is a powerful feature in Python that allows you to create new lists in a concise
# and readable way. It's a compact way to create lists from existing lists or other iterables by
# applying a transformation or filter to each element.

# new_list = [expression for element in iterable if condition]

# - expression is the operation you want to perform on each element.
# - element is the variable that takes on the value of each element in the iterable.
# - iterable is the list or other iterable that you want to process.
# - condition is an optional filter that determines whether an element is included in the new list.

# Without if condition
squared: list = [x**2 for x in [1, 3, 5, 7, 9] ]   # [1, 9, 25, 49, 81]
print(squared, " : ", type(squared))
# [1, 9, 25, 49, 81]  :  <class 'list'>


# With if condition
squared: list = [x**2 for x in [1, 2, 3, 4, 5] if x > 3]   # [16, 25]
print(squared, " : ", type(squared))
# [16, 25]  :  <class 'list'>

#-----------------------------------------------------------------------------------------------
