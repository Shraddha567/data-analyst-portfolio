d = {} #empty dictionary
print(type(d))

# Dictionary is a collection of key-value pairs. It allows us to associate data with unique keys and values and we can say dictionary is a list of key-value pairs and we stored it in a collection.
# Dictionaries are mutable, unordered, and indexed collections in Python.

marks = {
    "Harry": 85,
    "Rohan": 90,
    "Shubham": 78
}
# Accessing values in a dictionary using keys
print(marks["Math"])  # it will print 90 in Big-O of minutes.
# Adding a new key-value pair to the dictionary
marks["History"] = 92
print(marks)                
# Modifying an existing value in the dictionary
marks["Math"] = 95
print(marks)
'''
01. Dictionaries are mutable : meaning that we can change, add, or remove items after its creation.

02. Dictionaries are unordered :  meaning that the items have no defined order, and cannot be accessed by index.

03. Dictionaries do not allow duplicate keys : meaning that each key must be unique. If you try to insert a duplicate key, the last value will overwrite the previous one.

04. Dictionaries are defined using curly braces {} with key-value pairs separated by commas.
Dictionaries are defined using curly braces {} or the dict() function.

05. It is Indexed : meaning that we can access values using keys.iska matlab ye hai ki hum index ke through access nahi kar sakte hain but key ke through access kar sakte hain.
# Keys must be unique and immutable (string, number, or tuple with immutable elements) whereas values can be of any data type and can be duplicated.

# Each key is separated from its value by a colon (:).  
'''
