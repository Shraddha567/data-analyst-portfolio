# Q1
words = {
    "Name": "Shraddha",
    "Age": 30,
    "City": "Indore",
    "Profession": "Data Analyst"
}

word = input("Enter the word you want to search: ")
if word in words:
    print(f"{word} is found in the dictionary with value: {words[word]}")
else:
    print(f"{word} is not found in the dictionary")

s = set()
for i in range(1, 8):
    n = input(f"Enter No.{i}: ")
    s.add(int(n))

print("The unique numbers are: ")
print(s)
print(words[word])
# is found in the dictionary with value: {words.get(word, 'Not Found')})
# print(f"{word} is found in the dictionary with value: {words[word]}")

# Q2
s= set()
n = input("Enter No.1: ")
s.add(int(n))
n= input("Enter No.2: ")
s.add(int(n))
n= input("Enter No.3: ")
s.add(int(n))
n= input("Enter No.4: ")
s.add(int(n))
n= input("Enter No.5: ")
s.add(int(n))
n= input("Enter No.6: ")
s.add(int(n))
n= input("Enter No.7: ")
s.add(int(n))
print("The unique numbers are: ")

# Q3
s= set()
s.add(18)
s.add("18")
s.add(18.0)
s.add(True)
s.add((18,))
print(s)  # it will print {True, 18, '18', (18
# because True is considered as 1 in Python and 18, 18.0 are considered the same in set
print(len(s))  # it will print 4

