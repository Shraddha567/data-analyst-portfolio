try:
    x = int(input("Enter a number: \n"))
    y = 10/x
    print(f"10 divided by {x} is {y}")

except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("Division by zero is not allowed!")
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    print("Operation completed successfully without any errors.")
finally:
    print("I will always execute and run")
    

