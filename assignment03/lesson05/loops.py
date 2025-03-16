# Agentic AI - Python - Lesson 05 - Control Flow & Loops

# Loops and Iteration in Python

# 1. Introduction to Loops
# Loops are used to repeat a block of code multiple times. Python supports two types of loops:

# - for loops: Used to iterate over a sequence (e.g., lists, strings, or ranges).
# - while loops: Used to repeat a block of code as long as a condition is True.

# When to use scenario:

# A. For Loop:

# Grading a class of students: You have a list of 30 students and you want to calculate the 
# average score for each student. You use a for loop to iterate over the list of students and calculate
# the average score for each one.

# Washing Machine(number spins), Microwave Oven e.t.c.

# B. While Loop:

# Filling up a gas tank: You want to fill up your gas tank until it's full. You don't know how many 
# times you'll need to fill up the tank, but you'll keep filling it up until it's full. You use a
#  while loop to fill up the tank until it's full.

# Air Conditioner, Refigrator, Heater, Washing Machine(filling water) e.t.c.

#------------------------------------------------------------------------------------------------

# 2. The for Loop
# The for loop iterates over a sequence (like a list, string, or range) and executes a block of code
# for each item for a specified or fixed number of times.

# Iterate over a list
fruits: list = ["apple", "mango", "banana"]
for fruit in fruits:
    print(fruit)
# Note: Membership operators in python in, not in

# apple
# mango
# banana

# Iterate over a string
word: str = "Python"
for letter in word:
    print(letter)
# P
# y
# t
# h
# o
# n

#------------------------------------------------------------------------------------------------

# for Loop with else in Python
# In Python, a for loop can have an else block. The else block runs only if the loop completes without
# a break statement.

# Example 1: for loop with else (No break)
numbers: list = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
else:
    print("Loop completed successfully!")
# 1
# 2
# 3
# 4
# 5
# Loop completed successfully!

# Example 2: for loop with break (Skipping else)
for num in numbers:
    print(num)
    if num == 3:
        print("Breaking the loop!")
        break
else:
    print("Loop completed successfully!")  # This will not shown
# 1
# 2
# 3
# Breaking the loop!

# Example 3: Searching with else
for num in numbers:
    if num == 6:
        print("Number found!")
else:
    print("Number is not found!")  # Runs because 6 is not in the list
# Number is not found!

#------------------------------------------------------------------------------------------------

# In Lesson 01 we learned about range()

# print numbers from 0 to 4
for i in range(5):
    print(i)
# 0
# 1
# 2
# 3
# 4

# Print even numbers from 2 to 10
for i in range(2, 11, 2):
    print(i)
# 2
# 4
# 6
# 8
# 10

#------------------------------------------------------------------------------------------------

# _ (underscore) This is a throwaway variable, which is a common Python convention for a variable
# that you don't plan to use. In this case, the loop variable is not used within the loop, so it's assigned to _.

# If you want to use the loop variable, you can replace _ with a more meaningful variable name. For example:

for _ in range(10): # Just to show that _ is a loop variable, but its throwaway variable
    print(f"Iteration { _ }")
# Iteration 0
# Iteration 1
# Iteration 2
# Iteration 3
# Iteration 4
# Iteration 5
# Iteration 6
# Iteration 7
# Iteration 8
# Iteration 9

#------------------------------------------------------------------------------------------------

# 3. The while Loop
# The while loop repeats a block of code as long as a condition is True.

# Print numbers from 1 to 5
count: int = 1
while count <= 5:
    print(count)
    count += 1
# 1
# 2
# 3
# 4
# 5

#------------------------------------------------------------------------------------------------

# 4. Controlling Loops
# Python provides two keywords (break & continue) to control loops:

# - break: Exits the loop immediately.
# - continue: Skips the rest of the code in the current iteration and moves to the next iteration.

# Break example
for i in range(10):
    if i == 5:
        break
    print(i)
# 0
# 1
# 2
# 3
# 4

#------------------------------------------------------------------------------------------------

# Continue example
for i in range(5):
    if i == 3:
        continue
    print(i)
# 0
# 1
# 2
# 4

#------------------------------------------------------------------------------------------------

# 5. Nested Loops

# Nested loops, also known as inner loops or nested iterations, refer to the process of placing one
# loop inside another loop. The inner loop will iterate through its entire cycle for each iteration 
# of the outer loop.

# Multiplication table
for outer in range(1, 6):   # outer loop
    print(f"Multiplication Table of {outer}:")
    for inner in range(1, 6): # nested inner loop
        print(f"{outer} * {inner} = {outer * inner}")
    print() # Add a blank line after each row

# it prints the 1 to 5 tables till 5 in a this format (5 * 5 = 25)

#------------------------------------------------------------------------------------------------

# 6. Practical Examples
# Here are two practical examples to solidify these concepts.

# Example 1: Sum of Numbers

# Sum numbers from 1 to 100
total: int = 0
for i in range(1, 101):
    total += i
print("Sum of numbers from 1 to 100: ", total)
# Sum of numbers from 1 to 100:  5050


# Example 2: Finding Factors of a Number

# Find factors of a number
num: int = 24
factors = []   # An empty list factors is created.

for i in range(1, num + 1):  # range(1, 25)
    if num % i == 0:  # The modulus operator (%) checks if num is divisible by i. 24 % 3 == 0 (so 3 is a factor).
        factors.append(i)  # If i is a factor, it is added to the factors list using .append(i).
print(f"Factors of {num}: {factors}")

# Factors of 24: [1, 2, 3, 4, 6, 8, 12, 24]
