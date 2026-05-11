name = input("What is your name: ")
work = input("What do you work: ")
city = input("Where do you live:")
#  Shraddha Maheshwari is a Data Analyst working in Mumbai.
print(f"{name} is a {work} working in {city}.")
# Here, {name} and {city} are automatically replaced with their actual values.
'''
Why f-Strings?
1) Cleaner than string concatenation (+) and .format()
2) Faster and easier to read
3) Supports expressions and method calls within the curly braces {}
4) Useful for debugging by embedding variable names and values directly in the string
5) Supports multi-line strings with triple quotes (''' ''') or  (""" """) 
6) Can be used with different data types without explicit conversion to string
Examples of f-strings:
f"Hello {name}, you are {age} years old."
f"Result: {a + b}"
f"List: {[x for x in range(5)]}"
'''
'''


f-strings (formatted string literals) are an easy and modern way to format strings in Python. They were introduced in Python 3.6.
and f-strings are a way to embed expressions inside string literals, using curly braces {}.
To use an f-string we can add f or F before the opening quotation mark of the string.
and place input variables or expressions inside curly braces {} within the string.
They provide a easy and readable way to include variable values and expressions directly within string literals.
'''