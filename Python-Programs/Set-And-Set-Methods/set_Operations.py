s={1,2,8,2,45,23}
print(len(s))  # it will print 5 because there are 5 unique elements in the set
print(type(s))  # it will print <class 'set'>
print(s)  # it will print the set with unique elements {1, 2, 8, 45, 23}

# Set Operations
# 1. Addition : We can add elements to a set using the add() method.
s.add(99)
print(s)  # it will print the set with the added element {1, 2, 8, 45, 23, 99}

# 2. Removal : We can remove elements from a set using the remove() or discard() method.
s.remove(8)  # it will remove the element 8 from the set
print(s)  # it will print the set after removing the element {1, 2, 45, 23, 99}

# 3. Discarding an element
s.discard(100)  # it will not raise an error even if the element 100 is not present in the set
print(s)  # it will print the set as is {1, 2, 45, 23, 99}  

# 4. Clearing a set : We can remove all elements from a set using the clear() method.
s.clear()
print(s)  # it will print an empty set set()
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# 5.Difference : The difference method returns a new set containing elements that are in the first set but not in the second set.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1.difference(set2)

# 6. Union (combine) : The union method combines two sets and returns a new set containing all unique elements from both sets.
a = {1,2,3,4}
b = {4,5,6,7}
# a | b    
result = a.union(b)
print(result) # it will print {1, 2, 3, 4, 5, 6, 7}

# 7. Intersection : (gives us common elements)
A = {1, 2, 3}
B = {3, 4, 5}
result = A.intersection(B)
print(result)  # it will print {3}
# The intersection method returns a new set containing only the elements that are present in both sets.

# 8. Symmetric Difference : The symmetric_difference method returns a new set containing elements that are in either of the sets but not in both.
setA = {1, 2, 3}
setB = {3, 4, 5}
result = setA.symmetric_difference(setB)
print(result)  # it will print {1, 2, 4, 5}

# 9. pop() method removes and returns a random element from the set
my_set = {10, 20, 30, 40}
removed_element = my_set.pop()
print(removed_element)  # it will print a random element from the set
print(my_set)  # it will print the set after removing the random element
print(s)  # it will print the set after removing the random element

# 10. difference_update() method removes the elements of another set from the current set
setX = {1, 2, 3, 4, 5}
setY = {4, 5, 6, 7}
setX.difference_update(setY)
print(setX)  # it will print {1, 2, 3} which are in setX but not in setY        

# 11. Using issubset() method to check if one set is a subset of another
setA = {11,22,33}
setB = {44,55,66}
print(setA.issubset(setB)) 
 # it will print False as setA is not a subset of setB

# Using isSuperset() method to check if one set is a superset of another
setC = {1,2,3,4,5}
setD = {2,3}
print(setC.issuperset(setD)) 
# it will print True as setC is a superset of setD


# Summary of Set Operations
'''
1. Addition: Use the add() method to add elements to a set.
2. Removal: Use the remove() or discard() method to remove elements from a set.
3. Clearing: Use the clear() method to remove all elements from a set.
4. Difference: Use the difference() method to get elements in one set that are not in another.
5. Union: Use the union() method or | operator to combine two sets.
6. Intersection: Use the intersection() method or & operator to get common elements between two sets.
7. Symmetric Difference: Use the symmetric_difference() method or ^ operator to get elements in either set but not in both.
'''



