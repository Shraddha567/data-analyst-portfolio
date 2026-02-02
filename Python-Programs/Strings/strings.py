'''
String is a data type in Python used to represent text.
String is a sequence of characters enclosed in quotes and it is manipulated so existing string can not changed

We can primarily Write strings using:
1. Single quotes: 'Hello'
2. Double quotes: "Hello"
3. Triple quotes: 
triple_quotes_hello
or triple_quotes_hello2 
A String is a collection of characters
'''
name = "Shraddha"
print(name.replace("S", "Sh"))  # it will replace S with Sh
# and return a new string
greeting = 'Hello, World!'
print(name[0])
print(name[1])
print (greeting[0:5]) # it will print Hello
print (greeting[-6:]) # it will print World!
poem = '''Roses are red,
Violets are blue,
Sugar is sweet,
And so are you.'''
print(poem)
print(len(name)) # it will print length of string which is 8
print(name.lower()) # it will convert all characters to lowercase
print(name.upper()) # it will convert all characters to uppercase
print(len(name.strip())) # Strip remove starting and ending extra spaces, it will remove any start or end whitespace
print(name.split("a")) # it will split the string at each occurrence of 'a' 
print(name.find("r")) # it will return the index of first occurrence of r
print("Shraddha" in greeting) # it will return True if Shraddha is present in greeting else False
print("Python" not in greeting) # it will return True if Python is not present in greeting else False
print(name.isalpha()) # it will return True if all characters in name are alphabetic else False
print(name.isnumeric()) # it will return True if all characters in name are numeric else False
print(name.startswith("S")) # it will return True if name starts with S else False
print(name.endswith("i")) # it will return True if name ends with i else False

# in : is a memebership operator that is used to check elements presence in a string

'''
String concatenation: Joining two or more strings together using + operator
String formatting: Inserting values into a string using placeholders
Strings are immutable: Once a string is created, it cannot be changed
It can only be reassigned to a new string or modified using string methods

# You can destroy a string using del keyword and it will remove the string from memory
then you can create a new string with the same name
# it will give error because strings are immutable
# del name.
Example:   
#name[0] = "s" 

# we can reassign name to a new string and it will not give error
Example:
name = "NewName" 
NewName 
'''
first_name = "Shraddha"
last_name = "Maheshwari"
full_name = first_name + " " + last_name
print(full_name) # it will print Shraddha Maheshwari
age = 25
intro = "My name is {} and I am {} years old.".format(full_name, age)
print(intro) # it will print My name is Shraddha Maheshwari and I
# am 25 years old.
intro_f = f"My name is {full_name} and I am {age} years old."
print(intro_f) # it will print My name is Shraddha Maheshwari and
# I am 25 years old.
'''
String methods:
len(): Returns the length of the string
lower(): Converts the string to lowercase
upper(): Converts the string to uppercase
replace(): Replaces a specified substring with another substring
split(): Splits the string into a list of substrings based on a specified delimiter
find(): Returns the index of the first occurrence of a specified substring
in: Checks if a substring is present in the string
not in: Checks if a substring is not present in the string
'''
