a = "\nRohan is also good"
with open("shraddha.txt", "a") as f:
    f.write(a)

# 'a' is for append mode
# with statement automatically takes care of closing the file
# no need to explicitly call f.close()
# content = f.readlines()
#  # it will read line by line and store it in a list of lines
# print(content)
# f.close() --- IGNORE ---
# file.write(a) or f.write(a)