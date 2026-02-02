Functions in Python
Functions are used to group reusable code into a single block.
They help make programs organized, readable, and easier to maintain.

Instead of writing the same code again and again, you can define a function and reuse it whenever needed.

Defining a Function
Functions are defined using the def keyword.

def greet():
    print("Hello")

Calling a Function
To execute a function, you call it using its name followed by parentheses.

greet()

Functions with Parameters
Parameters allow you to pass data into a function.

def greet(name):
    print("Hello", name)
 
greet("Harry")

Here, name is a parameter and "Harry" is an argument.

Functions with Multiple Parameters
def add(a, b):
    print(a + b)
 
add(5, 3)

Return Statement
The return statement sends a value back from the function.

def add(a, b):
    return a + b
 
result = add(10, 5)

Once return is executed, the function stops running.

Default Parameter Values
You can provide default values to parameters.

def greet(name="User"):
    print("Hello", name)
 
greet()
greet("Harry")

Keyword Arguments
Arguments can be passed using parameter names.

def user_info(name, age):
    print(name, age)
 
user_info(age=25, name="Harry")

Variable Length Arguments
*args
Used to pass multiple positional arguments.

def total(*args):
    print(args)
 
total(1, 2, 3, 4)

**kwargs
Used to pass multiple keyword arguments.

def user_details(**kwargs):
    print(kwargs)
 
user_details(name="Harry", age=25)

Function Docstrings
Docstrings are used to describe what a function does.

def add(a, b):
    """Returns the sum of two numbers"""
    return a + b

Scope of Variables
Variables defined inside a function are local to that function.

def test():
    x = 10
    print(x)

Variables defined outside functions are global.

Function Inside a Function
Functions can be defined inside other functions.

def outer():
    def inner():
        print("Inside inner function")
    inner()

Lambda Functions
Lambda functions are small anonymous functions written in one line.

add = lambda a, b: a + b
print(add(3, 5))