a = "\nRohan is also good" # text to be appended in the file robot.txt
file = open("robot.txt", "a") # 'a' is for append mode
file.write(a)
file.close()