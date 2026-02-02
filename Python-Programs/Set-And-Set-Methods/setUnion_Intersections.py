s1={1,46,23}
s2={23,45,67}
# Set Union
# The union method combines two sets and returns a new set containing all unique elements from both sets
result = s1.union(s2)
print(result)  # it will print {1, 67, 23, 45, 46}

# we can also use '|' operator to perform union operation
A1 ={11,22,33}
A2 ={33,44,55}
response = A1 | A2
print(response)  # it will print {33, 22, 55, 11, 44}

# Set Intersection
# The intersection method returns a new set containing only the elements that are present in both sets.
print(A1.intersection(A2)) # it will print {33}

# we can also use '&' operator to perform intersection operation
result2 = s1 & s2
print(result2)  # it will print {23}
# Summary of Set Union and Intersection
'''
1. Union: Use the union() method or | operator to combine two sets and get all unique elements from both sets.  

2. Intersection: Use the intersection() method or & operator to get common elements between two sets.
'''

'''
Comparison:
B1 - B2 = {1, 2} (elements in B1 but not in B2)
B2 - B1 = {5, 6} (elements in B2 but not in B1)
You can also use the .difference() method instead of the - operator
'''

B1 = {1, 2, 3, 4}
B2 = {3, 4, 5, 6}
result = B1-B2  
print(result)  # it will give {1, 2} which are in B1 but not in B2.

# we can also use difference() method to perform the same operation
result2 = B1.difference(B2)
print(result2)  # it will give {1, 2} which are in B1 but not in B2.

print(B2-B1)  # it will give {5, 6} which are in B2 but not in B1.
result3 = B2.difference(B1)


