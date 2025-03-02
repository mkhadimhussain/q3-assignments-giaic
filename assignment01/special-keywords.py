# Special Keywords in Python
# Python has some reserved words that cannot be used as variable names.

# 1. Conditional Statements (if, elif, else)
a = 10

if a > 5:
    print("a is greater then 5")  # Output will be this
elif a == 5:
    print("a is 5")
else:
    print("a is less than 5")

#-----------------------------------------------------------------------

# 2. Loops (for, while)

# for loop
for i in range(3):      # loops 3 times (0, 1, 2)
    print("Iteration:", i)
# Iteration: 0
# Iteration: 1
# Iteration: 2
# for loop runs a fixed number of times.


# while loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1   # increases count by 1
# Count: 0
# Count: 1
# Count: 2
# while loop runs until the condition is False.

#-----------------------------------------------------------------------

# 3. Function Definition (def)
# def is used to define a function.
def greet(name):
    return f"Hello, {name}!"

print(greet("Saif"))  # Hello, Saif!

#-----------------------------------------------------------------------

# 4. Class (class)
class Car:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        return f"Car brand: {self.brand}"

car = Car("Toyota")
print(car.show_brand())    # Car brand: Toyota

# class is used to create an object.
# __init__ is the constructor that runs when the object is created.

#-----------------------------------------------------------------------

# 5. Exception Handling (try, except,  finally)
try: 
    num = int(input("Enter a number: "))
    result = 10/num
except ZeroDivisionError:
    print("Cannot divide by Zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
finally:
    print("Execution Completed.")   # always runns

# If the user enters 0, it triggers a ZeroDivisionError.
# If the user enters text, it triggers a ValueError.
# finally always runs.

#-----------------------------------------------------------------------

# 6. Anonymous Function (lambda)
square = lambda x: x * x
print(square(5))   # Output: 25

# lambda is used to create small functions without using def.

#-----------------------------------------------------------------------

# 7. Importing Modules (import)
import math
print(math.sqrt(16))   # Output: 4.0

# math.sqrt(16) finds the square root.

#-----------------------------------------------------------------------

# 8. pass Keyword
# The pass statement is used when you need a block of code syntactically, but you don’t 
# want to execute anything.

def my_function():
    pass   # Placeholder for future code

class MyClass:
    pass   # Placeholder for future class definition

for i in range(5):     # (0, 1, 2, 3, 4)
    if i == 3:
        pass   # No action when i is 3
    else:
        print(i)

# pass does nothing; it’s a placeholder.
# Used when defining empty functions or classes to avoid syntax errors.
# In the loop, pass is used when i == 3, meaning nothing happens at that iteration.

#-----------------------------------------------------------------------

# 9. break Keyword
# break is used to exit a loop immediately.

for i in range(5):
    if i == 3:
        break   # Exit the loop when i == 3
    print(i)

# The loop runs until i == 3, then break stops the loop.
# The output will be:
# 0
# 1
# 2

#-----------------------------------------------------------------------

# 10. continue Keyword
# continue is used to skip the current iteration and move to the next one.

for i in range(5):
    if i == 3:
        continue  # Skips when i is 3
    print(i)

# When i == 3, continue skips that iteration.
# The output will be:
# 0
# 1
# 2
# 4

#-----------------------------------------------------------------------

# 11. yield Keyword
# yield is used in generators to produce values one at a time.

# A generator is a special type of function that remembers where it left off 
# each time it is called. It does not store all values in memory, making it
# memory-efficient.

# Saves memory (Does not store all values at once).

def generate_number():
    for i in range(3):
        yield i    # Pauses and returns the value

gen = generate_number()
print(next(gen))   # Outout: 0
print(next(gen))   # Output: 1
print(next(gen))   # Output: 2

# yield pauses the function but remembers its state.
# next(gen) retrieves the next value.
#-----------------------------------------------------------------------

# 12. global Keyword
# global is used to modify a variable outside a function.

x = 10

def change_global():
    global x    # refers to the global variable(x)
    x = 20

change_global()
print(x)     # Output: 20

# Without global, x inside change_global() would not affect the global x.

#-----------------------------------------------------------------------

# 13. nonlocal Keyword
# nonlocal is used inside nested functions to modify a variable in the enclosing function.

def outer():
    x = "Outer"

    def inner():
        nonlocal x    # refers to the x in outer
        x = "Inner"

    inner()
    print(x)   # Output: Inner

outer()

# nonlocal allows inner() to modify x in outer().

#-----------------------------------------------------------------------

# 14. is Keyword
# is checks if two variables refer to the same object.

a = [1, 2, 3]
b = a 
c = [1, 2, 3]

print(a is b)   # True (same object)
print(a is c)   # False (different objects with same values)

# a is b is True because both refer to the same object.
# a is c is False because they are different objects.

#-----------------------------------------------------------------------

# 15. in Keyword
# in checks if a value exists in a list, tuple, set, dictionary, or string.

numbers = [1, 2, 3, 4, 5]
print(3 in numbers)    # True

text = "Python"
print("P" in text)     # True
print("Q" in text)     # False

# "P" in text is True because "P" exists in "Python".

#-----------------------------------------------------------------------

# 16. assert Keyword
# assert is used for debugging; it raises an error if a condition is False.

age = 18
assert age >= 18, "Age must be 18 or older!"  # No error

# age = 16 
# assert age >= 18, "Age must be 18 or older!" # AssertionError

# If age < 18, an AssertionError occurs.

#-----------------------------------------------------------------------

# 17. del Keyword
# del is used to delete a variable, list element, or dictionary key.

m = 5
del m
# print(m)   # NameError: x is not defined

my_list = [1, 2, 3]
del my_list[1]
print(my_list)   # Output: [1, 3]

# del m deletes the variable m.
# del my_list[1] removes the second element.

#-----------------------------------------------------------------------

# 18. with Keyword
# with is used for resource management, like handling files.

with open("sample.txt",  "w") as file:
    file.write("Hello,  Python!")   # Automatically close the file

# with ensures the file closes automatically.

#-----------------------------------------------------------------------

# 19. async & await Keywords
# Used in asynchronous programming to handle tasks without blocking execution.

import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(2)    # waits for 2 seconds
    print("Python!")

asyncio.run(hello())

# async def defines an asynchronous function.
# await pauses execution for asyncio.sleep(2).

#-----------------------------------------------------------------------

# 20. return Keyword
# The return statement sends a value from a function back to the caller.

def square(num):
    return num * num   # send result back

results = square(4)
print(results)       # Output: 16