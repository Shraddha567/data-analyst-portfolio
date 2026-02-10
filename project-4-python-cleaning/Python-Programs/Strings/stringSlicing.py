'''String Slicing in Python can be sliced for getting a part of strings using indexing.
In Python, strings are indexed starting from 0 for the first character, 1 for the second character, and so on.
Negative indexing is also supported, where -1 refers to the last character, -2 to the
second last character, and so on.
consider the following example:
Shraddha'''
name = "Shraddha" # length = 8
print (len(name)) # it will print length of string which is 8 and we can Count negative index of string and 
'''Negative indexing starts from -1 and goes to -8 for Shraddha
0 1  2  3  4  5  6  7
S  h  r  a  d  d  h  a
-8 -7 -6 -5 -4 -3 -2 -1
So, name[-1] will give 'a' and name[-8] will give 'S'
Example:
print(name[-1]) # it will print 'a'
print(name[-8]) # it will print 'S'
'''

nameShort = name[0:3] # it will print 'Shr'
print (nameShort) # returns 'Shr' from index 0 to 2 and It starts form index 0 and ends till 3 (excluding 3)
# So as We know total string length is 8 and last index is 7 and If we have to print 3 characters and we have print[-8: -5] which means -8+8 =0 to -5+8=3 and it will print string of index 0 to 2 which is Shr.

print (name[-8:-5]) # it is same as name[0:3]
print (name[-7:-1]) # it is same as name[1:7]
print (name[1:3])
print (name[1:-1]) #is same as name[1: (-1 + len(name))] or name[1:4]
print (name[1:4])
# to not to use this negative string slicing we can add string length using len() function
print (name[:3]) # it is same as name[0:3]  Blank in left side which means 0 index
print (name[2:]) # it will print from index 2 to end of string Blank in right side means total len of string which is 8
print (name[:]) # it will print the complete string
'''Slicing with Skip Value: You can also specify a step value to skip characters while slicing.
We can Provide third parameter in slicing which is step value.
Syntax: string[start:end:step]
Example: name = "Shraddha"
print(name[0:8:2]) # it will print 'Sradha' (skipping every 2nd character) 
print(name[::3]) # it will print 'S
'''
