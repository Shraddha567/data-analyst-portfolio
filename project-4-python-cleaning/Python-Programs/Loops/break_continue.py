# ‘break’ is used to come out of the loop when encountered. It instructs the program to – exit the loop now.
for i in range(10):
    if (i == 5):
        break
    print(i)
print("Loop ended using break statement")
# ‘continue’ is used to stop the current iteration of the loop and continue with the next one. It instructs the Program to “skip this iteration”.
for i in range(10):
    if(i == 6):
        continue
    print(i)
print("Loop ended using continue statement")
# In the first loop, when the value of i reaches 5, the break statement is executed,
# which causes the loop to terminate immediately. Therefore, the numbers 0, 1, 2, 3, 4 are printed, and then "Loop ended using break statement" is printed.

# In the second loop, the continue statement is used to skip the current iteration when i equals 6.
# As a result, only the numbers 0 to 9 except 6 are printed,
# followed by "Loop ended using continue statement".    

# The break statement is used to exit a loop prematurely when a certain condition is met.Let say we have a condition where we have i==5, we want to stop the loop at that point. and Break statement says stop the loop when i == 5 is met.So the loop will print numbers from 0 to 4 and then exit the loop.
 
# The continue statement is used to skip the current iteration of a loop and move to the next iteration.
# Let say we have a condition where we have i == 6, we want to skip the particular iteration when i == 6 is met. So the loop will print numbers 0 to 9 and except 6 which means continue not let to print 6, when i == 6 is met it will skip that iteration and continue with the next iteration.
# PASS STATEMENT : pass is a null statement in python. It instructs to “do nothing”.
l = [1,7,8]
for item in l:
    pass 
print("Loop ended using pass statement")
# without pass, the program will throw an error because the loop is empty
# In this example, the pass statement is used as a placeholder inside the for loop.
# Since there is no other code inside the loop, the pass statement allows the loop to run without any errors.
# After the loop, "Loop ended using pass statement" is printed.
# The pass statement is useful when you want to create a loop or a function that you plan to implement later, but you want to avoid syntax errors in the meantime.