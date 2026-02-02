print("Initializing...")
a = int(input("Enter a number: \n"))
b = int(input("Enter another number: \n"))
try :
    print("The value of a/b is:", a/b)
except Exception as e:
    print("Some error occurred!", e)

print("Execution Completed!")
