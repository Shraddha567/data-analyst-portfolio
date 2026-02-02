# Variables inside the function is local variable
def show_value():
    x = 11  # Local Variable
    print("Local variable x:", x)
show_value()


# Global Variables
# Global variables are created outside all functions. They can be accessed from anywhere in the program.
z = 78 # Global Variable
def show_value_of_z():
    print("Global variable z:", z)
show_value_of_z()