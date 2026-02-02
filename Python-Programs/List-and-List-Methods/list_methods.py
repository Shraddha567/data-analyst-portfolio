items=["apple", "banana", "orange"]
# List Length: len() function is used to get the number of elements in a list
count = len(items)
print(count)
print(items[-1])
print(items[-2])

# Modifying List Elements
items[1] = "grapes"

# Adding Elements to a List. append(): Adds an element to the end of the list.
items.append("Chiku")

# insert(): Inserts an element at a specific index.
items.insert(2, "mango")

# extend(): Adds multiple elements from another list.
items.extend(["more Bananas", "kiwi", "pineapples"])
print (items)

# Removing Elements from a List: remove() function removes the first occurrence of a value and If you have multiple apples so remove() will remove only first one.
items.remove("apple")
print(items)

# pop(): pop() function removes the last element and if we want to pop the given index then we can pass the index in the pop() function.
items.pop()
items.pop(2)
items.pop(0)
print(items)

# clear(): It removes all the elements from the list.
juices = ["apple", "banana"]
juices.clear()
print(juices)

# index(): It returns the index of the first occurrence of a value.
fruits = ["apple", "banana", "orange", "banana", "kiwi"]
index_of_banana = fruits.index("banana")
print(index_of_banana)

# count(): It returns the number of occurrences of a value in the list.
count_of_banana = fruits.count("banana")
print(count_of_banana)

# Reverse() : 
numbers = [5, 3, 7, 9, 0, 2]
numbers.sort()
print(numbers)
numbers.sort(reverse=True) # descending orders
print(numbers)
print (11 in numbers) # False
print (3 in numbers)  # True

'''
We can append any item in list using append()
It changes the Existing list and adds the new item in last of our List.
'''

