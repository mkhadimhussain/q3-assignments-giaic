# Agentic AI - Python - Lesson 05 - Control Flow & Loops

# Control Flow and Decision Making in Python

# 1. Introduction to Control Flow
# Control flow refers to the order in which statements are executed in a program. In Python,
# decision-making is achieved using if, elif, and else statements, along with comparison and logical operators.

#------------------------------------------------------------------------------------------------

# 2. Comparison Operators
# Comparison operators are used to compare values and return True or False. Here are the most common ones:

# == (equal to)
# !=  (not equal to)
# >   (greater than)
# <   (less than)
# >= (greater than or equal to)
# <= (less than or equal to)

x: int = 10
y: int = 20

print("x == y = ", x == y)   # False
print("x != y = ", x != y)   # True
print("x > y  = ", x > y)    # False
print("x < y  = ", x < y)    # True
print("x >= y = ", x >= y)   # False
print("x <= y = ", x <= y)   # True

#------------------------------------------------------------------------------------------------

# 3. Logical Operators

# Logical operators combine multiple conditions:

# and (True if both conditions are True)
# or (True if at least one condition is True)
# not (reverses the result of a condition)

age: int = 25
is_student: bool = True

# Check if age is greater than 18 AND is_student is True
if age > 18 and is_student:
    print("You are eligible for a student discount.")

# Check if age is less than 12 OR greater than 60
if age < 12 or age > 60:
    print("You qualify for a special discount.")

# Check if the person is NOT a student
if not is_student:
    print("You are not a student.")

#------------------------------------------------------------------------------------------------

# 4. The if Statement
# The if statement is used to execute a block of code only if a condition is True.

num: int = 10

if num > 0:
    print("The number is positive.")   # The number is positive.

#------------------------------------------------------------------------------------------------

# 5. The else Statement
# The else statement is used to execute a block of code if the if condition is False.
num: int = -5

if num > 0:
    print("The number is positive.")
else:
    print("The number is not positive.")  # The number is not positive.

#------------------------------------------------------------------------------------------------

# 6. The elif Statement
# The elif statement is used to check multiple conditions. It stands for "else if."
num: int = 0
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")    # The number is zero.

#------------------------------------------------------------------------------------------------

# 7. Nested if Statements
# if statements can be nested inside other if statements to check multiple conditions.

num: int = 10   # output: The number is positive and even.
# num: int = -10  # output: The number is negative.

if num > 0:   # check wather the number is positive or negative

    if num % 2 == 0:   # Modulus operator, remainder 0 = even_number,
        print("The number is positive and even.")
    else:   # remainder 1 = odd_number,
        print("The number is positive and odd.")

else:     
    print("The number is negative.")

#------------------------------------------------------------------------------------------------

# 8. Practical Examples
# Here are two practical examples to solidify these concepts.

# Simple Calculator

operation: str = input("Enter the operation (+, -, *, /): ")
num1: float = float(input("Enter the first number: "))
num2: float = float(input("Enter the second number: "))

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error, Division by zero."
else:
    result = "Invalid operation."

print("Result: ", result)

#------------------------------------------------------------------------------------------------

# From now onwards you will be seeing the power of Generative AI in our tutorial
# prompt: build a calculator which takes input from the user, beside basic functionality include
# modulus, floor division, Exponentiation

def calculator():
    """
    A calculator function that takes user input for numbers and operations,
    including modulus, floor division, and exponentiation.
    """
    while True:  # creates an infinite loop, which means it will keep running until explicitly stopped.

        operation = input("Enter the operation (+, -, *, /, %, //, ** or 'q' to quit): ")
        if operation.lower() == 'q':
            break   # break exits the loop, stopping the calculator

        if operation not in ('+', '-', '*', '/', '%', '//', '**'):
            print("Invalid operation")
            continue   # continue skips the rest of the loop and asks the user for input again.
            # if not in the given tuple, it prints "Invalid operation." and restarts the loop using continue
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            #If the user enters non-numeric input (like "abc"), a ValueError occurs.
            print("Invalid input. Please enter number only.")
            continue   # continue restarts the loop.
            
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero."
                print(result)
                continue   # If num2 == 0, it prints an error and restarts the loop.
        elif operation == '%':
                result = num1 % num2
        elif operation == '//':
            if num2 != 0:
                result = num1 // num2
            else:
                result = "Error: Division by zero."
                print(result)
                continue 
        elif operation == '**':
            result = num1 ** num2

        print("Result: ",  result)
calculator()

#------------------------------------------------------------------------------------------------

# prompt: generate a grading system for school which takes marks as an  input show grade according to the marks
def grading_system(marks):
    """
    This function takes marks as input and returns the corresponding grade.

    Args:
        marks: The marks obtained by the student.

    Returns:
        The grade corresponding to the marks.
    """
    if marks > 90:
        grade = "A+"
    elif marks > 80:
        grade = "A"
    elif marks > 70:
        grade = "B"
    elif marks > 60:
        grade = "C"
    elif marks > 50:
        grade = "D"
    else:
        grade = "F"
    return grade

# Get marks as input from the user
while True:
    try:  
        marks = float(input("Enter the marks: "))
        if 0 <= marks <= 100:
            break
        else:
            print("Marks must be between 0 and 100.")
    except ValueError:
        print("Invalid input, please enter a number.")

# Determine the grade
grade = grading_system(marks)

# Print the grade
print(f"The grade for {marks} marks is: {grade}")

#------------------------------------------------------------------------------------------------
