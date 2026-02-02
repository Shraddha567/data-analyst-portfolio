score = 75
if score >= 80: # condition false
    print("Grade: A")
elif score >= 70: # condition true 
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
else:
    print("Grade: F")

if score % 2 ==0:
    print("Score is even")
else:
    print("Score is odd")

'''
All conditions are checked in order until one is found to be true. In this case, since score is 75, the second condition is true, so "Grade: B" is printed and the rest of the conditions are skipped.
Because if, elif and else are used in combination, only one block of code will be executed based on the first true condition.
Which means agar ek bhi elif condition true ho jata hai to uske baad ke sare elif or else conditions ko skip kar diya jata hai.
so Ye ek saath multiple conditions ko check karne ke liye use hota hai.
block of code sirf tabhi execute hota hai jab uski condition true ho.

'''