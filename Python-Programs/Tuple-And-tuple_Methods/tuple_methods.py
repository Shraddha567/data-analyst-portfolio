items = ("apple", "banana", "orange")
print(len(items))
print(items[-1])
print(items.count("apple"))
print(items.index("banana"))
# Tuples are immutable, so we cannot modify elements directly
# But we can convert the tuple to a list, modify it, and convert it back to a tuple
list_1 = list(items)
print(list_1)
list_1[1] = "grapes"
items = tuple(list_1)
print(items) 
# We can concatenate two or more tuples using + operator
tuple1 = ("apple", "banana")
tuple2 = ("orange", "grapes")
combined_tuple = tuple1 + tuple2
print(combined_tuple)
# We can repeat a tuple using * operator
repeated_tuple = tuple1 * 2
print(repeated_tuple)
# We can check if an element exists in a tuple using in keyword
print("banana" in tuple1)
print("kiwi" not in tuple1)
'''
Tuples are immutable: Once a tuple is created, it cannot be changed
It can only be reassigned to a new tuple
We can convert a tuple to a list, modify the list, and convert it back to a
tuple
Tuples are used to store multiple values in a single variable.
They are one of the most flexible and commonly used data structures in Python.
A tuple can store different types of data and can be nested within other tuples.
'''
# You can destroy a tuple using del keyword and it will remove the tuple from memory
# then you can create a new tuple with the same name
# Example:
# del items
# items = ("kiwi", "mango")
# print(items) # it will print ("kiwi", "mango")
# but if you try to modify an element of the tuple it will give error because tuples are
# immutable
# Example:
# items[0] = "chiku" # it will give error
# we can reassign items to a new tuple and it will not give error
# Example:
# items = ("chiku", "mango")
# print(items) # it will print ("chiku", "mango")
