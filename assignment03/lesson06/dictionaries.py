# Agentic AI - Python - Lesson 06 - Lists, Tuples & Dictionary

# Dictionaries in Python

# 1. Introduction to Dictionaries
# A dictionary is a collection of key-value pairs. It is:

# - Ordered (since Python 3.7): Items are stored in the order they were inserted.
# - Mutable: Items can be added, removed, or modified after the dictionary is created.
# - Un-indexed: Items are accessed using keys, not indices.
# - Without duplicates: Keys must be unique, but values can be duplicated.

# Before Python 3.7, dictionaries were unordered, meaning that items were not stored in a specific order. 
# However, with the introduction of Python 3.7, dictionaries now maintain their insertion order.

#--------------------------------------------------------------------------------------------------

# 2. Creating a Dictionary
# Dictionaries are created using curly braces {} with key-value pairs separated by commas.

# The syntax is:
# dictionary = {key1: value1, key2: value2, ...}

#--------------------------------------------------------------------------------------------------

# prompt: genrate a List of 5 american cities
american_cities: dict = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
print(american_cities)
# ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

#--------------------------------------------------------------------------------------------------

# Create a dictionary to store a person's details
person: dict = {
    "name": "Alice",
    "age": 20,
    "visited_cities": american_cities 
}
print(person)
# {'name': 'Alice', 'age': 20, 'visited_cities': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']}

#--------------------------------------------------------------------------------------------------

thisdict: dict = dict(name = "John", age = 21, country = "Norway") 
# it is possible to use the dict() constructor to make a dictionary
print(type(thisdict), " - ", thisdict)
# <class 'dict'>  -  {'name': 'John', 'age': 21, 'country': 'Norway'}

#--------------------------------------------------------------------------------------------------

# 3. Accessing Values
# You can access the value associated with a key using square brackets [] or the get() method.

# Access values using keys
print(person["name"])    # Alice

# .get() method
# get("key", "default value (if key is not found)")

print(person.get("age", "99"))  # 20 (if not found it will return 99 (default value))

# Access a non-existent key
print(person.get("weight", 50)) # 50 (default value)

print(person.get("country", "my_default_value_if_not_found")) # my_default_value_if_not_found

#--------------------------------------------------------------------------------------------------

# 4. Modifying a Dictionary
# You can add new key-value pairs or modify existing ones.

# Add a new value key-value pair
person["email"] = "alice@gmail.com"
print(person)
# {'name': 'Alice', 'age': 20, 'visited_cities': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
# 'email': 'alice@gmail.com'}

# Modify an existing value
person["age"] = 24
print(person)
# {'name': 'Alice', 'age': 24, 'visited_cities': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], 
# 'email': 'alice@gmail.com'}

#--------------------------------------------------------------------------------------------------

# 5. Deleting Items
# You can remove a key-value pair using the del keyword or the .pop() method.

# Note that .pop() returns the value of the removed key-value pair, whereas del does not return anything.

# You can also use .pop() with a default value, in case the key is not found in the dictionary:

person: dict = {'name': 'Alice', 'age': 20, 'email': 'alice@gmail.com', 'city': ['New York', 'Los Angeles', 'Chicago']}
print(person) 
# {'name': 'Alice', 'age': 20, 'email': 'alice@gmail.com', 'city': ['New York', 'Los Angeles', 'Chicago']}

# Remove a key-value pair using del
del person["city"]
print(person)
# {'name': 'Alice', 'age': 20, 'email': 'alice@gmail.com'}

# Remove a key-value pair using .pop()
age: int = person.pop("age", -1)
print('Removed age: ', age)  # Removed age:  20
print(person)  
# {'name': 'Alice', 'email': 'alice@gmail.com'}

print("\n-----\n")
#Again remove a key which is already removed to check the default value

age: int = person.pop("age", -1)
print("key 'age' not found in dict so returning default value:", age)
# key 'age' not found in dict so returning default value: -1

#--------------------------------------------------------------------------------------------------

# 6. Dictionary Methods
# Python provides several useful methods for working with dictionaries.

# Method	Description	

# keys()	Returns a list of all keys in the dictionary.	
# values()	Returns a list of all values in the dictionary.	
# items()	Returns a list of key-value pairs as tuples.	
# clear()	Removes all items from the dictionary.	
# update()	Adds or updates multiple key-value pairs from another dictionary.	

person1: dict = {'name': 'Alice', 'age': 23, 'email': 'alice@gmail.com', 'city': ['New york', 'Los Angeles', 'Chicago']}

# Get all keys
print(person1.keys()) # dict_keys(['name', 'age', 'email', 'city'])

print("person1.keys() = ", person1.keys())
# person1.keys() =  dict_keys(['name', 'age', 'email', 'city'])

# Get all values
print("person1.values() = ", person1.values())
# person.values() =  dict_values(['Alice', 23, 'alice@gmail.com', ['New york', 'Los Angeles', 'Chicago']])

# Get all key-value pairs (as tuples)
print("person1.items() = ", person1.items())
# person1.items() =  dict_items([('name', 'Alice'), ('age', 23), ('email', 'alice@gmail.com'), ('city',
# ['New york', 'Los Angeles', 'Chicago'])])

# Update the dictionary
person1.update({"city": "Los Angeles", "age": 27})
print("After: person1.update =", person1)
# After: person1.update = {'name': 'Alice', 'age': 27, 'email': 'alice@gmail.com', 'city': 'Los Angeles'}

# Clear the dictionary
person1.clear()
print("After: person1.clear() =", person1)
# After: person1.clear() = {}

#--------------------------------------------------------------------------------------------------

# Duplicate Key Not Allowed
# Dictionaries cannot have two items with the same key:

thisdict: dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020   # this will overwrite the previous key:value
}
print(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#---------------------------------------------------------------------------------------------------

# 7. Iterating Over a Dictionary
# You can loop through a dictionary using for loops.

for key in thisdict:
    print(key)
# brand
# model
# year

for key, value in thisdict.items():
    print(key, ":", value)
# brand : Ford
# model : Mustang
# year : 2020

#--------------------------------------------------------------------------------------------------

# 8. Practical Examples
# Here are two practical examples to solidify these concepts.

# Example 1: Building a Phonebook

# Create a phonebook
phonebook: dict = {
    "Alice": "123-456-7890",
    "John": "098-765-4321",
    "Charlie": "222-333-4444"
}

# Add a new contact
phonebook["David"]: "555-555-5555"

# Search for a contact
name: str = input("Enter a name to search: ")
if name in phonebook:
    print(f"{name}'s phone number is {phonebook[name]}.")
else:
    print(f"{name} is not in the phonebook.")

# Output
# Enter a name to search: John
# John's phone number is 098-765-4321.

# Enter a name to search: herry
# herry is not in the phonebook.
#--------------------------------------------------------------------------------------------------

# Example 2: Counting Word Frequencies in a Text

sentence = """
**Projected Economy Size of AI:**

The projected economy size of AI is significant, with estimates varying depending on the source and methodology. Here are some notable projections:

1. **Global AI Market Size:**
	* By 2025: $190 billion (Source: MarketsandMarkets)
	* By 2030: $1.5 trillion (Source: PwC)
2. **AI-Driven Economic Growth:**
	* By 2025: AI is expected to contribute 10% to global GDP growth (Source: Accenture)
	* By 2030: AI is expected to contribute 14% to global GDP growth (Source: PwC)
3. **AI-Generated Revenue:**
	* By 2025: AI is expected to generate $15.7 trillion in revenue (Source: IDC)
	* By 2030: AI is expected to generate $33.5 trillion in revenue (Source: McKinsey)
4. **Job Market Impact:**
	* By 2025: AI is expected to create 133 million new jobs globally (Source: World Economic Forum)
	* By 2030: AI is expected to automate 30% of current jobs globally (Source: McKinsey)

**Industry-Specific Projections:**

1. **Healthcare:**
	* By 2025: AI is expected to generate $150 billion in revenue (Source: MarketsandMarkets)
2. **Financial Services:**
	* By 2025: AI is expected to generate $100 billion in revenue (Source: Accenture)
3. **Manufacturing:**
	* By 2025: AI is expected to generate $50 billion in revenue (Source: IDC)
4. **Transportation:**
	* By 2025: AI is expected to generate $20 billion in revenue (Source: MarketsandMarkets)

**Regional Projections:**

1. **North America:**
	* By 2025: AI is expected to generate $100 billion in revenue (Source: MarketsandMarkets)
2. **Europe:**
	* By 2025: AI is expected to generate $50 billion in revenue (Source: IDC)
3. **Asia-Pacific:**
	* By 2025: AI is expected to generate $200 billion in revenue (Source: MarketsandMarkets)

Note: These projections are based on various assumptions, including the pace of AI development, adoption rates, and economic trends. The actual economy size of AI may vary depending on several factors.

"""

# Count the frequency of words in a sentence

words: list = sentence.split()  # ['Hello', 'world', 'Hello']
word_count = {}   # initializes an empty dictionary (word_count) to store the word frequencies.

for word in words:  # This starts a loop that iterates through each word in the list.
    if word in word_count:
        word_count[word] += 1  # If the word is already in the dictionary, increase its count by 1.
    else:
        word_count[word] = 1   # If the word is not in the dictionary, add it with an initial count of 1.

print(word_count)

#--------------------------------------------------------------------------------------------------

# prompt: sort the word count variable according to its value in descending order

# Sort the word_count dictionary by value in descending order
sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
print(sorted_word_count)

# word_count.items() returns a list of tuples like [('apple', 2), ('banana', 1)].
# key=lambda item: item[1] tells Python to sort by the second value (word count).
# reverse=True ensures sorting is in descending order (highest count first).

# lambda item: item[1]
# lambda → Defines an anonymous function.
# item → A parameter that represents each element in word_count.items() (which is a tuple like ('apple', 3)).
# item[1] → The function extracts the second element (value) of the tuple.

#--------------------------------------------------------------------------------------------------

# 9. Common Pitfalls
# Using a non-existent key without checking first for e.g. 

my_dict: dict = {"name": "saif", "age": 20}

# using .get()
print(my_dict.get("name_1"))   # Output: None
print(my_dict.get("name_1", "No name found"))  # Output: no name found

# without .get()
# print(my_dict["name_1"])  # (rises a KeyError)
# Output: KeyError: 'name_1'

# - Always use get() or check if the key exists with in to avoid error.

# - Forgetting that dictionary keys must be immutable (e.g., strings, numbers, or tuples).

# - Assuming dictionaries are ordered (in Python 3.6+, they retain insertion order, but this is not 
#   guaranteed in older versions).

#--------------------------------------------------------------------------------------------------

# prompt: generate a working example of all dictionary function

# Example Dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# 1. Accessing Items
print("1. Accessing Items")
print("Name:", my_dict["name"])  # Accessing by key
print("Age:", my_dict.get("age"))  # Accessing using get()
print("City (using get):", my_dict.get("city"))

# 2. Adding Items
print("\n2. Adding Items")
my_dict["email"] = "alice@gmail.com"
print("Dictionary after adding email:", my_dict)

# 3. Modifying Items
print("\n3. Modifying Items")
my_dict["age"] = 32
print("Dictionary after modifying age:", my_dict)

# 4. Removing Items
print("\n4. Removing Items")
my_dict.pop("city")
print("Dictionary after removing city (using pop):", my_dict)
del my_dict["email"]
print("Dictionary after removing email (using del):", my_dict)

# 5. Dictionary Methods
print("\n5. Dictionary Methods")
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

# 6. Clearing the Dictionary
print("\n6. Clearing the Dictionary")
my_dict.clear()
print("Dictionary after clearing:", my_dict)

# Adding items back for further examples
my_dict = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# 7. Updating the Dictionary
print("\n7. Updating the Dictionary")
my_dict.update({"age": 32, "city": "USA"})
print("Dictionary after updating:", my_dict)

# 8. Iterating Through a Dictionary
print("\n8. Iterating Through a Dictionary")
print("Iterating through keys:")
for key in my_dict:
    print(key)

print("\nIterating through values:")
for value in my_dict.values():
    print(value)

print("\nIterating through items (key-value pairs):")
for key, value in my_dict.items():
    print(f"{key} : {value}")

#9 checking if a key exist
print("\n9. checking if a key exist")
if "name" in my_dict:
    print("Name Exists")
else:
    print("Name do not exist")

# 10. Dictionary Length
print("\n10. Dictionary Length")
print("Length of the dictionary:", len(my_dict))

# 11. Creating a dictionary from iterable
print("\n11. Creating a dictionary from iterable")
iterable = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
new_dict = dict(iterable)
print("new dictionary:", new_dict)

# 12. Copying a dictionary
print("\n12. Copying a dictionary")
copied_dict = my_dict.copy()
print("Copied dictionary:", copied_dict)

# 13. Nested Dictionaries
print("\n13. Nested Dictionaries")
nested_dict = {
    "person1": {"name": "Alice", "age": 23},
    "person2": {"name": "John", "age": 40}
}

print("Nested dictionary:", nested_dict)
print("Alice's age:", nested_dict["person1"] ["age"])

# 1. Accessing Items
# Name: Alice
# Age: 30
# City (using get): New York

# 2. Adding Items
# Dictionary after adding email: {'name': 'Alice', 'age': 30, 'city': 'New York', 'email': 'alice@gmail.com'}

# 3. Modifying Items
# Dictionary after modifying age: {'name': 'Alice', 'age': 32, 'city': 'New York', 'email': 'alice@gmail.com'}

# 4. Removing Items
# Dictionary after removing city (using pop): {'name': 'Alice', 'age': 32, 'email': 'alice@gmail.com'}
# Dictionary after removing email (using del): {'name': 'Alice', 'age': 32}

# 5. Dictionary Methods
# Keys: dict_keys(['name', 'age'])
# Values: dict_values(['Alice', 32])
# Items: dict_items([('name', 'Alice'), ('age', 32)])

# 6. Clearing the Dictionary
# Dictionary after clearing: {}

# 7. Updating the Dictionary
# Dictionary after updating: {'name': 'John', 'age': 32, 'city': 'USA'}

# 8. Iterating Through a Dictionary
# Iterating through keys:
# name
# age
# city

# Iterating through values:
# John
# 32
# USA

# Iterating through items (key-value pairs):
# name : John
# age : 32
# city : USA

# 9. checking if a key exist
# Name Exists

# 10. Dictionary Length
# Length of the dictionary: 3

# 11. Creating a dictionary from iterable
# new dictionary: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# 12. Copying a dictionary
# Copied dictionary: {'name': 'John', 'age': 32, 'city': 'USA'}

# 13. Nested Dictionaries
# Nested dictionary: {'person1': {'name': 'Alice', 'age': 23}, 'person2': {'name': 'John', 'age': 40}}
# Alice's age: 23

#--------------------------------------------------------------------------------------------------
