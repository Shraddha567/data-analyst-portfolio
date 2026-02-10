def greet(name="User"):
    print("Hello", name)
greet()
# Calling the function without any arguments")
greet("Rohan")  # This will raise an error
#   In case of name(), it will print default or initial value "Hello User" because we have provided a default value for the parameter 'name'.
# and In case of greet("Rohan") it will overwrite the default value with the provided argument "Rohan" and print "Hello Rohan".

def employee_details(name="user", city="Delhi"):
    print("Hello", name, city)
employee_details()  # Both parameters will take default values
employee_details("Alice")  # 'name' will be "Alice", 'city' will take default value "Delhi"
employee_details(city="Rajasthan", name="Aakash")
# Here, 'name' will be "Aakash" and 'city' will be "Rajasthan" because the arguments are passed in order.
# We can give keyword argument in above function call to avoid confusion.
employee_details("Bob", "Mumbai")  # Both parameters will take provided values
employee_details("Charlie", city="Chennai")
# Here, 'name' will be "Charlie" and 'city' will be "Chennai" because the second argument is passed as a keyword argument.

    


    