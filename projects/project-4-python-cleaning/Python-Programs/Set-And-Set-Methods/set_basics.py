# To create an empty set, use set().
emptySet = set()   # Correct

'''
empty = {} # Incorrect, this creates an empty dictionary
print(type(empty)) # Output: <class 'dict'>
'''
# Creating a set with values
# In sets we will put values inside curly braces {} separated by commas
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Sets are collection of objects in which each object is unique and unordered
# sets are also collection of data and used to store multiple items in a single variable
# Creating an empty set
emptySet = set()
print(type(emptySet))  # Output: <class 'set'>
'''
A set in Python is an unordered collection of unique items, mainly used to remove duplicates and check membership efficiently.
'''

# Sets are used to store multiple values in a single variable and no duplicate values allowed. (jab bhi hume duplicate values nhi chahiye then hum set ka use karte hain)

# A set does not allow duplicate values and does not maintain any specific order.

# Sets are unordered, meaning that the items have no defined order, and cannot be accessed by index

# Sets are mutable, So we can add or remove items after its creation

# If you try to access an element in a set, it will raise a TypeError because sets are unordered and do not support indexing e.g: s1[0] will raise a TypeError).You cannot access elements by position like in a list.

# Sets are defined using curly braces {} or the set() function

#If you inserted duplicate values in your set, it will automatically remove the duplicate values and keep only unique values and show the output by processing itself 


# Key Characteristics of Sets
# 1. No Duplicates : Sets automatically remove duplicate values.
s = {1, 2, 2, 3}
print(s)   # {1, 2, 3}


# 2. Unordered : Sets do not maintain any specific order of elements.
s = {10,20,30}

# 3. Mutable : You can add or remove elements from a set after its creation.


# 4. No Indexing : Sets do not support indexing or slicing.


# Insertion Order (Python 3.7+)
'''
Python remebers in the order which items or elements are added in the set  but, 
* sets are not sorted 
* ordered may look like sorted but it is not sorted
* sets are still unordered collections
'''

# Example of creating a set
s1 = {1, 5, 6, 4, 9, 2, 3, 5}
print(s1) # {1, 2, 3, 4, 5, 6, 9}


# Creating a Set : Sets are created using curly braces {} or the set() function.
# Using curly braces
numbers = {1, 2, 3}

# Using set() function
letters = set("hello")
print(letters)   # {'h', 'e', 'l', 'o'}
