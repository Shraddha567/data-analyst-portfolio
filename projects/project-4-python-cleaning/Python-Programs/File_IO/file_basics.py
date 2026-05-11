a = "Shraddha is a Data Analyst"

file = open("sample.txt", "w")
file.write(a)
file.close()

# file = open("robot.txt", "r")
# content = file.read()
content = file.readlines()
 # it will read line by line and store it in a list of lines
print(content)

file.close()