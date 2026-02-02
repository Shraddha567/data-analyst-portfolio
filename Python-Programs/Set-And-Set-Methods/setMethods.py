s = set() # Creating an empty set no repetition allowed
print(type(s))  # Output: <class 'set'>

items = {"apple", "banana", "orange"}
# 01. Add Method: The add() method is used to add a single element to a set.
items.add("grapes")  # Adds an element to the set
print(items)
items.update(["kiwi", "mango"])  # Adds multiple elements to the set 
# update is a method which takes lists, tuples, or other sets as arguments
# set doesnot promise any order so we can expect from set that our items will be Unique and items will not repeated and We cant expext that set will not maintain any specific order of elements.
print(items)
items.remove("banana")  # Removes an element from the set If item is not present it will raise a KeyError
'''items.remove("bananae")  #Raises KeyError as the element is not present in the set iska matlab hai agar wo element set me nahi hota hai to error dega 
print(items)
'''

items.discard("bananae") #No error even if the element is not present in the set
print(items)
# Removes an element from the set if it exists agar wo element set me nahi hai to error nahi dega ar agar hota hai to remove kardeta hai
print(len(items))
# pop method removes and returns an random element or item from the set
a = items.pop()
print(a)
print(items)

# clear() method removes all elements from the set
items.clear()
print(items)  # Output: set()
print(len(items))  # Output: 0

# Properties of SETS
'''
1)Sets are unordered - meaning that the items have no defined order, and cannot be accessed by index.
2) sets are unIndexed - So We can not access items or elements by index like in a list.
3)Sets do not allow duplicate values - meaning that each value must be unique. If you try to insert a duplicate value, it will be ignored.
4)Sets are mutable - meaning that we can change, add, or remove items after its
creation.
5) There is no way to change items in a set, but we can add or remove items.
6) Sets are defined using curly braces {} or the set() function.
7) Sets are used to store multiple values in a single variable.
'''



