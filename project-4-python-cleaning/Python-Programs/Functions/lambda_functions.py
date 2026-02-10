#  def add(a, b) :
#      return a + b
add = lambda a, b : a +b # lambda function to add two numbers and a +b gives us output 
result = add(5, 3)
print("The sum is:", result)
# In this example, we define a lambda function that takes two parameters, a and b, and returns their sum.
# We then call this lambda function with the arguments 5 and 3, and print the
# result, which is 8.
# What is lambda function in Python?
# A lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.
# The syntax of a lambda function is:
# lambda arguments: expression
# Lambda functions are often used for short, throwaway functions that are not needed elsewhere in the code.
# They are commonly used in situations where a simple function is required for a short period of time, such as in functional programming or when working with higher-order functions like map(), filter(), and reduce().
# Lambda functions can be assigned to variables, passed as arguments to other functions, and returned from other functions.
# However, since lambda functions are limited to a single expression, they are not suitable for complex operations that require multiple statements or a lot of logic.
# In such cases, it is better to define a regular function using the def keyword.   
# Example 2: Lambda function to find the square of a number
square = lambda x: x ** 2
result = square(4)
print("The square is:", result)
# In this example, we define a lambda function that takes one parameter, x, and returns its square.
# We then call this lambda function with the argument 4, and print the result, which is 16.
# Example 3: Lambda function with multiple arguments
multiply = lambda a, b, c: a * b * c
result = multiply(2, 3, 4)
print("The product is:", result)
# In this example, we define a lambda function that takes three parameters, a, b, and c, and returns their product.
# We then call this lambda function with the arguments 2, 3, and 4, and print the result, which is 24.
# Example 4: Using lambda function with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)
# In this example, we use the map() function to apply a lambda function that squares each number in the numbers list.
# The result is converted to a list and printed, which gives us [1, 4, 9, 16, 25].
# Example 5: Using lambda function with filter() 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)
# In this example, we use the filter() function to apply a lambda function that filters out
# even numbers from the numbers list. The result is converted to a list and printed, which gives us [2, 4, 6, 8, 10].
# Example 6: Using lambda function with reduce()
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers:", product)
# In this example, we use the reduce() function from the functools module to apply a lambda function that multiplies all the numbers in the numbers list together.
# The result is printed, which gives us 120.
# In summary, lambda functions are a powerful feature in Python that allow for the creation of small, anonymous functions for short-term use.
# They are commonly used in functional programming and with higher-order functions like map(), filter(), and reduce().
# However, for more complex operations, it is recommended to use regular functions defined with the def keyword.    


