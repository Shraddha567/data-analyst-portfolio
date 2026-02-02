# A function is a group of statements performing a specific task. When a program gets bigger in size and its complexity grows, it gets difficult for aprogram to keep track on which piece of code is doing what! A function can be reused by the programmer in a given program any number of times. This avoids repetition of code and makes the program more modular and easier to debug.
# FUNCTION DEFINITION : The part containing the exact set of instructions which are executed during the functioncall.
# FUNCTION CALL: Whenever we want to call a function, we put the name of the function followed by parentheses as follows: func1() # This is called function call.
def greet(fname, lname):
    print("Good Morning!", fname, lname)
    print("How are you!")
    print("Thank you!")
greet("Shraddha", "Maheshwari")
greet("John", "Doe")

def add(a,b):
    # print(a + b)
    return a + b
c = add (4, 6)
print("The sum is:", c)
    
