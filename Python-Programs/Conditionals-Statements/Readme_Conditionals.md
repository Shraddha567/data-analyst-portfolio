* Conditional Statements in Python
Conditional statements are used to make decisions in a program.
They allow the program to execute different blocks of code based on conditions.

Python uses if, elif, and else for conditional logic.

The if Statement
The if statement checks a condition.
If the condition is true, the code inside the block runs.

age = 18
 
if age >= 18:
    print("Eligible")

The else Statement
The else block runs when the if condition is false.

age = 16
 
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

The elif Statement
elif stands for else if. It is used to check multiple conditions.

score = 75
 
if score >= 90:
    print("Grade A")
elif score >= 60:
    print("Grade B")
else:
    print("Grade C")

Indentation in Conditionals
Python uses indentation to define code blocks.

if True:
    print("This runs")
    print("This also runs")

Incorrect indentation will cause an error.

Comparison Operators in Conditions
Conditions often use comparison operators.

x = 10
 
if x == 10:
    print("Equal")
 
if x != 5:
    print("Not equal")

Logical Operators in Conditions
Logical operators allow combining multiple conditions.

age = 25
country = "India"
 
if age >= 18 and country == "India":
    print("Allowed")

Nested Conditionals
Conditionals can be placed inside other conditionals.

age = 20
 
if age >= 18:
    if age < 60:
        print("Adult")

Using pass in Conditionals
The pass statement is used when a condition is required syntactically but no action is needed.

age = 15
 
if age >= 18:
    pass
else:
    print("Minor")

Conditional Expressions (Ternary Operator)
Python supports one line conditionals.

age = 20
status = "Adult" if age >= 18 else "Minor"

Common Mistakes
Forgetting indentation
Using = instead of == in conditions
Writing overly complex nested conditions