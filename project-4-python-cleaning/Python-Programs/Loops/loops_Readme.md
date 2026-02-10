Loops are used to execute a block of code multiple times.
They help reduce repetition and make programs more efficient.

Python mainly provides two types of loops:

for loop
while loop
The for Loop
The for loop is used to iterate over a sequence.

items = ["apple", "banana", "orange"]
 
for item in items:
    print(item)

The loop runs once for each element in the sequence.

Using range() with for Loop
The range() function generates a sequence of numbers.

for i in range(5):
    print(i)

This will print numbers from 0 to 4.

range() with Start and Step
for i in range(1, 10, 2):
    print(i)

This prints numbers from 1 to 9 with a step of 2.

Looping Through a String
Strings can also be iterated character by character.

text = "Python"
 
for char in text:
    print(char)

The while Loop
The while loop runs as long as a condition remains true.

count = 1
 
while count <= 5:
    print(count)
    count += 1

Infinite Loop
If the condition never becomes false, the loop runs forever.

while True:
    print("Running")

Use infinite loops carefully.

Loop Control Statements
Python provides special statements to control loop execution.

break
Stops the loop completely.

for i in range(10):
    if i == 5:
        break
    print(i)

continue
Skips the current iteration and moves to the next one.

for i in range(5):
    if i == 2:
        continue
    print(i)

pass
Acts as a placeholder where a statement is required.

for i in range(5):
    pass

Nested Loops
A loop inside another loop is called a nested loop.

for i in range(3):
    for j in range(2):
        print(i, j)

Looping with else
The else block runs when the loop finishes normally.

for i in range(3):
    print(i)
else:
    print("Loop finished")

The else block does not run if the loop is terminated using break.