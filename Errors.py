# Raising Error
x = 10
if x == 0:
    raise Exception("\n{X} canot be equel zero")
else:
    print(f" X ===> {x} Thank you")
    
    
# Another Example
X = 19
if type(X) == str :
    raise Exception("We Need your age please write a integer") 
else:
    print(f"Your age ====> {X}")

# Try , Except , Else
"""
Comprehensive Lesson on Python's try-except Blocks
---------------------------------------------------

This lesson will cover the basics and advanced usage of try-except blocks in Python.
We'll explore different types of exceptions, how to handle multiple exceptions,
using else and finally with try-except, and custom exception handling.
"""

# Basic try-except block
# -----------------------
# Let's start with the simplest form of a try-except block.
# The try-except block allows you to handle errors gracefully
# instead of letting the program crash.

try:
    # Here, we try to perform a division by zero, which will cause an error.
    result = 10 / 0
except ZeroDivisionError:
    # If a ZeroDivisionError occurs, this block of code will execute.
    # This prevents the program from crashing.
    print("Error: You cannot divide by zero!")

# Example Output:
# Error: You cannot divide by zero!


# Handling Multiple Exceptions
# -----------------------------
# You can handle multiple exceptions by specifying different exception types.
# Let's see how this works.

try:
    num = int("not a number")  # This will cause a ValueError.
    result = 10 / 0  # This would cause a ZeroDivisionError, but it won't reach this line.
except ValueError:
    print("Error: Could not convert data to an integer.")
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

# Example Output:
# Error: Could not convert data to an integer.


# Catching All Exceptions
# ------------------------
# You can catch all exceptions using a bare except clause.
# However, this is generally not recommended because it catches all exceptions,
# including those you might not want to handle (like keyboard interruptions).

try:
    result = 10 / 0
except:
    print("An error occurred!")

# Example Output:
# An error occurred!


# Using else with try-except
# ---------------------------
# The else clause can be used with try-except to define a block of code to be executed
# if no exceptions are raised.

try:
    result = 10 / 2  # No error here, so the else block will execute.
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
else:
    # This block will run if no exceptions are raised in the try block.
    print(f"Success! The result is {result}")

# Example Output:
# Success! The result is 5.0


# The finally block
# ------------------
# The finally block is always executed, regardless of whether an exception occurred or not.
# It's typically used for cleanup actions like closing files or releasing resources.

try:
    file = open("example.txt", "r")  # Trying to open a non-existent file.
except FileNotFoundError:
    print("Error: The file was not found.")
finally:
    print("This block will always execute, whether an error occurred or not.")

# Example Output:
# Error: The file was not found.
# This block will always execute, whether an error occurred or not.


# Raising Exceptions
# -------------------
# You can also raise exceptions manually using the raise keyword.

def divide(a, b):
    if b == 0:
        raise ValueError("b cannot be zero!")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")

# Example Output:
# Error: b cannot be zero!

# Summary:
# ---------
# - The try-except block allows you to handle exceptions (errors) in your code.
# - You can specify multiple except blocks to handle different types of exceptions.
# - Use the else block to run code that should only execute if no exceptions are raised.
# - The finally block is used for cleanup actions and always runs.
# - You can raise exceptions manually and even create custom exceptions for specific cases.
try:
    print(int(10/2))
except: # If there is Errors
    print("canot be divied ")
else:   # If there NO Errors
    print("Can be divied")
finally: # Works any Way (there is errors) ; (No errors) 
    print("Hi Any Way")
# define the error
try:
    print(int(10/0))
except ZeroDivisionError: # If there is ZeroDivisionError
    print("canot be divied ")
else:   # If there NO Errors
    print("Can be divied")
finally: # Works any Way (there is errors) ; (No errors) 
    print("Hi Any Way") 

