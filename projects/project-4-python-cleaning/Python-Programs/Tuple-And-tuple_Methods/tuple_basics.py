# Tuples : Tuples are immutable and cannot be changed once created
# Tuples are used to store multiple values in a single variable. 
# They are similar as list we can access its elements using indexing and slicing
# but we cannot modify, add or remove elements from the tuple
# Tuples are defined using parentheses () instead of square brackets []
# Example of creating a tuple
numbers = (1,2,3,4,5)
print(numbers[0])# it will print 1
print(numbers[1:4]) # it will print (2, 3, 4
print(numbers[-3:]) # it will print (3, 4, 5)
single = (1,) # single element tuple
print(single)
# Tuples can store different types of data
# Tuple and List having a single difference that tuple is immutable and it is used to store multiple values in a single variable
# Tuples are generally faster than lists because of their immutability
# Tuples can be used as keys in dictionaries because they are hashable
# Example of a tuple with different data types
mixed_tuple = (1, "Hello", 3.14, True)
print(mixed_tuple)
# Nested tuples
nested_tuple = (1, (2, 3), (4, 5, 6))
print(nested_tuple)
# Tuple unpacking
a, b, c, d, e = numbers
print(a) # it will print 1
print(b) # it will print 2
# We can concatenate two or more tuples using + operator
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple) # it will print (1, 2, 3, 4, 5, 6)
# We can repeat a tuple using * operator
repeated_tuple = tuple1 * 3
print(repeated_tuple) # it will print (1, 2, 3, 1, 2, 3, 1, 2, 3)
# We can check if an element exists in a tuple using in keyword
print(2 in tuple1)
print(5 not in tuple1) # it will print True
# We can get the length of a tuple using len() function
print(len(tuple1)) # it will print 3
'''
Tuples are immutable: Once a tuple is created, it cannot be changed
It can only be reassigned to a new tuple
Tuples are generally faster than lists because of their immutability
Tuples can be used as keys in dictionaries because they are hashable
Tuples are used to store multiple values in a single variable.
They are one of the most flexible and commonly used data structures in Python.
A tuple can store different types of data and can be nested within other tuples.
'''
# You can destroy a tuple using del keyword and it will remove the tuple from memory
# then you can create a new tuple with the same name
# Example:
# del numbers
# numbers = (7, 8, 9)
# print(numbers) # it will print (7, 8, 9)
# but if you try to modify an element of the tuple it will give error because tuples are immutable
# Example:
# numbers[0] = 10 # it will give error
# we can reassign numbers to a new tuple and it will not give error
# Example:
# numbers = (10, 2, 3, 4, 5)
# print(numbers) # it will print (10, 2, 3, 4
# 5)
#We Can change a tuple into list and then we can modify that list and again convert that list into tuple.

