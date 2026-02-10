# key values which we get are in the form of tuples
marks = {
    "Harry": 100,
    "Alice": 56,
    "Bob": (75, 80, 70)     
}
print (marks.items()) #Returns a list of (key, value)tuples.
print(marks.keys()) #Returns a list of all the keys in the dictionary.
print(marks.values()) #Returns a list of all the values in the dictionary.
marks.update({"Harry": 99, "Renuka":88}) # it will update the value of Harry to 99 and add a new key Renuka with value 88
print(marks)
# We can use the get() method to access values in a dictionary
print(marks.get("Shivika")) # Prints None
print(marks.get("Harry"))  # it will print 99
print(marks.get("Harry2")) # Prints None
# print(marks["Harry2"]) # Returns an error if the key is not exist in the dictionary (key error)

# We can use the pop() method to remove a key-value pair from the dictionary
removed_value = marks.pop("Bob")  # it will remove the key Bob and return its value
print(removed_value)  # it will print (75, 80, 70)

fruits = {
    "apple": 2,
    "banana": 3,
    "orange": 1
}
dict.clear(fruits) # it will remove all the fruits from the dictionary
print(fruits)  # it will print {}

new_dict = marks.copy() # it will create a shallow copy of the dictionary
print(new_dict)  # it will print the copied dictionary

# The fromkeys() method creates a new dictionary with keys from an iterable and values set to a specified value.
# syntax - dict.fromkeys(seq[, value]) 
# it will create a new dictionary with keys from `seq` and values set to value
dict.fromkeys(["a", "b", "c"], 0)
print(new_dict)  # it will print the new dictionary created

# The setdefault() method returns the value of a key if it is in the dictionary. If not, it inserts the key with a specified value.
marks.setdefault("Rohan", 95)  # it will return the value of Rohan
print(marks)  # it will print the dictionary with Rohan's value
marks.setdefault("NewStudent", 88)  # it will add NewStudent with value 88
print(marks)  # it will print the dictionary with NewStudent added
# The popitem() method removes and returns an arbitrary (key, value) pair from the dictionary.
item = marks.popitem()  # it will remove and return an arbitrary (key, value
print(item)  # it will print the removed (key, value) pair
print(marks)  # it will print the dictionary after removing the item
# The items() method returns a view object that displays a list of a dictionary's (key, value) tuple pairs.
print(marks.items())  # it will print the (key, value) pairs of the dictionary
# The keys() method returns a view object that displays a list of all the keys in the dictionary.
print(marks.keys())  # it will print all the keys of the dictionary
# The values() method returns a view object that displays a list of all the values in the dictionary.
print(marks.values())  # it will print all the values of the dictionary         
# Dictionary Methods Summary
'''
1. clear() - Removes all items from the dictionary.
2. copy() - Returns a shallow copy of the dictionary.
3. fromkeys(seq[, value]) - Creates a new dictionary with keys from seq and values set to value.
4. get(key[, default]) - Returns the value of key if it exists, otherwise returns default (None if not provided).
5. items() - Returns a view object of (key, value) pairs in the dictionary.
6. keys() - Returns a view object of all keys in the dictionary.
7. pop(key[, default]) - Removes the specified key and returns its value. If key is not found, returns default if provided, otherwise raises KeyError.
8. popitem() - Removes and returns an arbitrary (key, value) pair from the dictionary.      
9. setdefault(key[, default]) - Returns the value of key if it exists; otherwise, inserts key with a value of default and returns default.
10. update([other]) - Updates the dictionary with key-value pairs from other, overwriting existing keys.
11. values() - Returns a view object of all values in the dictionary.
'''
# we can also calculate length of dictionary
s={1:"one",2:"two",3:"three"}
print(len(s))  # it will print the number of key-value pairs in the dictionary.
# it will print 3










