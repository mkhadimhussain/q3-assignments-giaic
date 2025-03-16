# Agentic AI - Python - Lesson 07 - The Set, Frozenset & GC

# The Frozenset
# In Python, a frozenset is an immutable (unchangeable) version of a set. It is a collection of unique 
# elements, just like a set, but it cannot be modified after it is created.

# Here are the key features of a frozenset:

# 1- Immutable: A frozenset cannot be modified after it is created. You cannot add, remove, or change 
#   elements in a frozenset.
# 2- Ordered: Like sets, frozensets are unordered in Python versions before 3.7. However, from 
#   Python 3.7 onwards, frozensets maintain their insertion order, just like sets.
# 3- Hashable: frozensets are hashable, meaning they can be used as keys in dictionaries or elements 
#   in other sets.
# 4- Unique elements: A frozenset can only contain unique elements, just like a set.

#--------------------------------------------------------------------------------------------------

# Here are the key differences between a set and a frozenset in Python:

# 1- Immutability:
# - set: Mutable (can be modified after creation)
# - frozenset: Immutable (cannot be modified after creation)

# 2- Modification methods:
# - set: Supports methods like add(), remove(), discard(), clear(), pop(), update()
# - frozenset: Does not support any modification methods

# 3- Hashability:
# - set: Not hashable (cannot be used as keys in dictionaries or elements in other sets)
# - frozenset: Hashable (can be used as keys in dictionaries or elements in other sets)

# 4- Thread safety:
# - set: Not thread-safe (multiple threads can modify the set simultaneously, leading to inconsistencies)
# - frozenset: Thread-safe (since it's immutable, it's safe to access from multiple threads)

# 5- Syntax:
# - set: Created using the set() function or the {} syntax (e.g., my_set = {1, 2, 3})
# - frozenset: Created using the frozenset() function (e.g., my_frozenset = frozenset([1, 2, 3]))

# 6- Use cases:
# - set: Suitable for situations where you need to frequently add or remove elements (e.g., when filtering data)
# - frozenset: Suitable for situations where you need an immutable collection (e.g., when using it as a 
#   key in a dictionary or as an element in another set)

#--------------------------------------------------------------------------------------------------

# Here's a summary of the differences:

# Feature	             Set	                Frozenset
# ___________________________________________________________
# Immutability	         Mutable	            Immutable
# Modification methods 	 Yes	                No
# Hashability	         No	                    Yes
# Thread safety	         No	                    Yes
# Syntax	             set() or {}	        frozenset()
# Use cases	             Frequent modifications	Immutable collection

#--------------------------------------------------------------------------------------------------

# Creating frozenset
my_frozenset: frozenset = frozenset([1,2,3, "Hello World!"])
print("my_frozentset = ", my_frozenset)
# my_frozentset =  frozenset({1, 2, 3, 'Hello World!'})

# creating set
my_set: set = {10,20,30, "Python"}

my_frozenset2: frozenset = frozenset(my_set)
print("my_frozenset2 = ",my_frozenset2)
# my_frozenset2 =  frozenset({'Python', 10, 20, 30})

#--------------------------------------------------------------------------------------------------

# Set Methods

my_set: set  = {1,2,3, "Hello! World", 4,5,6}
my_set2: set = {1,2,3, "Hello! World", 8,9}

print("difference()           = ", my_set.difference(my_set2))  # {4, 5, 6}
#Returns a set containing the difference between two or more sets

print("intersection()         = ", my_set.intersection(my_set2)) # {1, 2, 3, 'Hello! World'}
#Return a set that contains the items that exist in both set

print("union()                = ", my_set.union(my_set2)) # {1, 2, 3, 4, 5, 6, 8, 9, 'Hello! World'}
#Return a set that contains all items from both sets, duplicates are excluded

print("symmetric_difference() = ", my_set.symmetric_difference(my_set2)) # {4, 5, 6, 8, 9}
#Return a set that contains only unique items from both sets

print("isdisjoint()           = ", my_set.isdisjoint(my_set2))  # False
#Return True if no items in set x is present in set y

my_set3 = {1,2,3, "Hello! World"}
print("issuperset()           = ", my_set.issuperset(my_set3))  # True
#Return True if all items in set x are present in set y

print("issubset()             = ", my_set.issubset(my_set3))   # False
print("issubset()             = ", my_set3.issubset(my_set))   # True

# difference()           =  {4, 5, 6}
# intersection()         =  {1, 2, 3, 'Hello! World'}
# union()                =  {1, 2, 3, 4, 5, 6, 8, 9, 'Hello! World'}
# symmetric_difference() =  {4, 5, 6, 8, 9}
# isdisjoint()           =  False
# issuperset()           =  True
# issubset()             =  False
# issubset()             =  True

#--------------------------------------------------------------------------------------------------

# prompt: generate examples of all the method of set

# Example usage of set methods

# Initialize two sets for demonstration
set1: set = {1, 2, 3, 4, 5}
set2: set = {4, 5, 6, 7, 8}

# 1. add(): Adds an element to the set.
set1.add(6)
print(f"add(6): {set1}")  # Output: {1, 2, 3, 4, 5, 6}

# 2. clear(): Removes all elements from the set.
set_copy: set = set1.copy()
set_copy.clear()
print(f"clear(): {set_copy}")  # Output: set()

# 3. copy(): Returns a copy of the set.
set_copy: set = set1.copy()
print(f"copy(): {set_copy}")  # Output: {1, 2, 3, 4, 5, 6}

# 4. difference(): Returns a set containing the difference between two or more sets.
difference_set: set = set1.difference(set2)
print(f"difference(): {difference_set}")  # Output: {1, 2, 3}

# 5. difference_update(): Removes the items in this set that are also included in another, specified set.
set1.difference_update(set2)
print(f"difference_update(): {set1}")  # Output: {1, 2, 3}
set1: set = {1, 2, 3, 4, 5,6} #reset set1

# 6. discard(): Remove the specified item.
set1.discard(6)
print(f"discard(6): {set1}")  # Output: {1, 2, 3, 4, 5}

# 7. intersection(): Returns a set, that is the intersection of two other sets.
intersection_set: set = set1.intersection(set2)
print(f"intersection(): {intersection_set}")  # Output: {4, 5}

# 8. intersection_update(): Removes the items in this set that are not present in other, specified set(s)
set1.intersection_update(set2)
print(f"intersection_update(): {set1}") # Output: {4, 5}
set1 = {1, 2, 3, 4, 5,6} #reset set1

# 9. isdisjoint(): Returns whether two sets have a intersection or not.
print(f"isdisjoint(): {set1.isdisjoint(set2)}")  # Output: False
print(f"isdisjoint(): {set1.isdisjoint({9,10})}") # Output: True

# 10. issubset(): Returns whether another set contains this set or not.
print(f"issubset(): {set1.issubset(set2)}")  # Output: False
print(f"issubset(): {{1,2}}.issubset({set1})")  # Output: True
print(f"issubset(): {{1,2}}.issubset({{1,2}})")  # Output: True


# 11. issuperset(): Returns whether this set contains another set or not.
print(f"issuperset(): {set1.issuperset(set2)}")  # Output: False
print(f"issuperset(): {set1.issuperset({1,2})}")  # Output: True
print(f"issuperset(): {{1,2}}.issuperset({{1,2}})")  # Output: True

# 12. pop(): Removes a random element from the set.
removed_element: int = set1.pop()
print(f"pop(): {removed_element}")  # Output: (random element)
print(f"set after pop(): {set1}")  # Output: (set without removed_element)
set1.add(removed_element)#put back the element for others test

# 13. remove(): Removes the specified element. Raises an error if the element is not present.
set1.remove(1)
print(f"remove(1): {set1}")  # Output: {2, 3, 4, 5,6}
set1.add(1)#put back the element for others test

# 14. symmetric_difference(): Returns a set with the symmetric differences of two sets.
symmetric_difference_set: set = set1.symmetric_difference(set2)
print(f"symmetric_difference(): {symmetric_difference_set}")  # Output: {1, 2, 3, 6, 7, 8}

# 15. symmetric_difference_update(): Inserts the symmetric differences from this set and another
set1.symmetric_difference_update(set2)
print(f"symmetric_difference_update(): {set1}")  # Output: {1, 2, 3, 6, 7, 8}
set1 = {1, 2, 3, 4, 5,6} #reset set1

# 16. union(): Returns a set containing the union of sets.
union_set = set1.union(set2)
print(f"union(): {union_set}")  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# 17. update(): Update the set with the union of this set and others
set1.update(set2)
print(f"update(): {set1}") # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# add(6): {1, 2, 3, 4, 5, 6}
# clear(): set()
# copy(): {1, 2, 3, 4, 5, 6}
# difference(): {1, 2, 3}
# difference_update(): {1, 2, 3}
# discard(6): {1, 2, 3, 4, 5}
# intersection(): {4, 5}
# intersection_update(): {4, 5}
# isdisjoint(): False
# isdisjoint(): True
# issubset(): False
# issubset(): {1,2}.issubset({1, 2, 3, 4, 5, 6})
# issubset(): {1,2}.issubset({1,2})
# issuperset(): False
# issuperset(): True
# issuperset(): {1,2}.issuperset({1,2})
# pop(): 1
# set after pop(): {2, 3, 4, 5, 6}
# remove(1): {2, 3, 4, 5, 6}
# symmetric_difference(): {1, 2, 3, 7, 8}
# symmetric_difference_update(): {1, 2, 3, 7, 8}
# union(): {1, 2, 3, 4, 5, 6, 7, 8}
# update(): {1, 2, 3, 4, 5, 6, 7, 8}

#--------------------------------------------------------------------------------------------------

# Create some example frozensets
frozen_set1: frozenset = frozenset([1, 2, 3, 4])
frozen_set2: frozenset = frozenset([3, 4, 5, 6])
frozen_set3: frozenset = frozenset([1, 2])

print(f"frozen_set1: {frozen_set1}")
print(f"frozen_set2: {frozen_set2}")
print(f"frozen_set3: {frozen_set3}")
print("\n----------\n")
# Methods that work with frozensets (since they are immutable)
# These methods return a new frozenset or a boolean value

# 1. difference(): Returns a new frozenset with elements present in the first frozenset but not in the second.
difference_set: frozenset = frozen_set1.difference(frozen_set2)
print(f"difference(): {difference_set}")  # Output: frozenset({1, 2})

# 2. intersection(): Returns a new frozenset containing only elements common to both frozensets.
intersection_set: frozenset = frozen_set1.intersection(frozen_set2)
print(f"intersection(): {intersection_set}")  # Output: frozenset({3, 4})

# 3. union(): Returns a new frozenset containing all unique elements from both frozensets.
union_set: frozenset = frozen_set1.union(frozen_set2)
print(f"union(): {union_set}")  # Output: frozenset({1, 2, 3, 4, 5, 6})

# 4. symmetric_difference(): Returns a new frozenset with elements that are in either of the sets but not in both.
symmetric_difference_set: frozenset = frozen_set1.symmetric_difference(frozen_set2)
print(f"symmetric_difference(): {symmetric_difference_set}")  # Output: frozenset({1, 2, 5, 6})

# 5. isdisjoint(): Returns True if the two frozensets have no elements in common; otherwise, False.
print(f"isdisjoint(): {frozen_set1.isdisjoint(frozen_set2)}")  # Output: False
print(f"isdisjoint(): {frozen_set1.isdisjoint(frozenset([7, 8]))}")  # Output: True

# 6. issubset(): Returns True if all elements of the first frozenset are present in the second frozenset.
print(f"issubset(): {frozen_set3.issubset(frozen_set1)}")  # Output: True
print(f"issubset(): {frozen_set1.issubset(frozen_set3)}")  # Output: False

# 7. issuperset(): Returns True if all elements of the second frozenset are present in the first frozenset.
print(f"issuperset(): {frozen_set1.issuperset(frozen_set3)}")  # Output: True
print(f"issuperset(): {frozen_set3.issuperset(frozen_set1)}")  # Output: False

# 8. copy(): Returns a new frozenset that is a shallow copy of the original.
copy_set: frozenset = frozen_set1.copy()
print(f"copy(): {copy_set}")  # Output: frozenset({1, 2, 3, 4})
print(f"copy() is same object?: {copy_set is frozen_set1}") # Output: True because frozensets are immutable

# frozen_set1: frozenset({1, 2, 3, 4})
# frozen_set2: frozenset({3, 4, 5, 6})
# frozen_set3: frozenset({1, 2})

# ----------

# difference(): frozenset({1, 2})
# intersection(): frozenset({3, 4})
# union(): frozenset({1, 2, 3, 4, 5, 6})
# symmetric_difference(): frozenset({1, 2, 5, 6})
# isdisjoint(): False
# isdisjoint(): True
# issubset(): True
# issubset(): False
# issuperset(): True
# issuperset(): False
# copy(): frozenset({1, 2, 3, 4})
# copy() is same object?: True

#--------------------------------------------------------------------------------------------------
