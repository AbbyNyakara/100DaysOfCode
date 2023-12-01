import os


# Dealing with text files

# #1. Opening text files: 
# with open("my_file.txt") as file:
#     #Read the contents:
#     contents  = file.read()
#     print(contents)
#     #file.close()

# The with keyword closes the file once it is open.

# Writing to a file: 

with open("new_file.txt", mode="w") as file:
    file.write("This is a new file")




