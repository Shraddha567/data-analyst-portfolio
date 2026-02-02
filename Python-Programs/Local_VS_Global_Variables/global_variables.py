# Variables outside the function is global variable

A = 10 # Global variable
def show_value():
    global A  # Declare A as global inside the function
    A = 5  # Modify the global variable A
    print(A)

show_value()
show_value()
print(A)  # Global variable

# If We use a variable inside the function which is never made inside the function then python will look for the variable outside the function will check globally and if it finds the variable it will use that variable.
# In the above example, we have a global variable A initialized to 10.
# global keyword  If we want to change variable value inside the function which is defined outside the function then we have to use global keyword inside the function before using that variable.
