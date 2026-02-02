Error Handling in Python
Errors are situations where a program cannot run as expected.
Error handling allows a program to deal with such situations without crashing.

Python uses try, except, else, and finally to handle errors.

What is an Error?
An error occurs when Python encounters a problem while executing code.

Common examples:

Dividing by zero
Accessing a file that does not exist
Converting invalid data types
The try and except Block
Code that may cause an error is placed inside the try block.
If an error occurs, the code inside except runs.

try:
    x = int("abc")
except:
    print("An error occurred")

The program continues running instead of stopping.

Handling Specific Errors
You can catch specific error types.

try:
    x = int("abc")
except ValueError:
    print("Invalid conversion")

This helps in handling errors more precisely.

Multiple except Blocks
Different errors can be handled separately.

try:
    x = int(input("Enter a number: "))
    y = 10 / x
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Division by zero is not allowed")

The else Block
The else block runs if no error occurs.

try:
    x = int("10")
except ValueError:
    print("Error")
else:
    print("Conversion successful")

The finally Block
The finally block always runs, whether an error occurs or not.

try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution finished")

Raising Errors Manually
You can raise an error using the raise keyword.

age = -5
 
if age < 0:
    raise ValueError("Age cannot be negative")

Using pass in Error Handling
The pass statement can be used when you want to ignore an error.

try:
    x = int("abc")
except ValueError:
    pass

This is generally discouraged unless intentional.

Common Error Types
Some common built in exceptions:

ValueError
TypeError
ZeroDivisionError
FileNotFoundError
IndexError
KeyError
Why Error Handling is Important
Prevents program crashes
Makes programs more reliable
Helps handle unexpected inputs
Improves user experience