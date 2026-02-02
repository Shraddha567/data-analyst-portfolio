# RECURSION : Recursion is a function which calls itself. It is used to directly use a mathematical formula as function.
# Example: Factorial of a number n is represented as n! and is calculated as:
# n! = n x (n-1) x (n-2) x ….. x 1
# It can also be represented using recursion as:
# factorial(n) = n x factorial (n-1)
# This function can be defined as follows:
def factorial(n):
    if n == 0 or n == 1: # base condition which doesn’t call the function any further
        return 1
    else:
        return n*factorial(n-1)
# function calling itself
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")
# In this example, the factorial function calls itself with a decremented value of n until it reaches the base condition of n being 0 or 1.
# At that point, it returns 1, and the recursive calls start resolving, ultimately calculating the factorial of the original number.
# This approach is elegant and closely mirrors the mathematical definition of factorial, making it easier to understand and implement for problems that have a recursive nature.    
# However, it's important to note that recursion can lead to performance issues and stack overflow errors if the recursion depth is too high.
# Therefore, it's essential to ensure that the base condition is well-defined and that the recursion depth is manageable for the problem at hand.