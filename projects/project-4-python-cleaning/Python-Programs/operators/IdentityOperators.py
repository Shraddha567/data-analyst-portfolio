'''
Object Identity Vs Value Equality : Identity operators are used to compare
the memory locations of two objects. In Python, there are two identity
operators: is and is not.
1. is operator: It returns True if both variables point to the same object
in memory, otherwise it returns False.
2. is not operator: It returns True if both variables point to different
objects in memory, otherwise it returns False.
example:
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b) # it will return True because both a and b point to the same
# object in memory
print(a is c) # it will return False because a and c point to different
# objects in memory
print(a is not c) # it will return True because a and c point to different
# objects in memory
print(a is not b) # it will return False because both a and b point to the
# same object in memory
'''
'''
Identity operators compare memory locations of objects, 
not values.

Operator	
is - Same object
is not -Different object
'''