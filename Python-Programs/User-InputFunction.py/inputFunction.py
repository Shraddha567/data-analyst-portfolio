print ("Welcome")
name = input("Who are you? ")
print ("Hello " + name)
# The input function always returns a string (text)
# Convert to Integer or Float to perform math
age = int(input("How old are you? "))
price = float(input("Enter price: "))

''' 
The input() function is used to take
User input from the console.

To perform math, you must convert the input 
using: int() for whole numbers
or float() for decimal numbers.

input() pauses the program execution
and waits for the user to type something
and press Enter. The typed value is then
returned as a string.

Aceepts an optional prompt string argument
which is displayed to the user before
waiting for input. Always returns a string.

And if we want do math operations, we need to convert the input
to the appropriate numeric type using int() or float().
str to int conversion.
'''