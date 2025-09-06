'''
The 'x' mode in Pythons open() function stands for exclusive creation.
Here's what it does:
1. It creates a new file.
2. If the file already exists, then it will rais a FileExistsError.
3. This mode is used when you want to ensure you're not over writing an existing file.
'''

# Creating a new file
new_file = open('my_file.txt', 'x')
new_file.close()

# Checking if the file exists
import os
print("Checking if my_file exists or not...")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
    print(" 'my_file.txt' is removed.")
else:
    print("The file does not exist.")

# Creating a new file if it does'nt exist
my_file = open('my_file.txt', 'w')
my_file.write("Hi, I'm Ayaat and I'm currently 12 y/o.")
my_file.close()

# Delete file named codingal
os.remove('my_file.txt')

#deleting any folder named folder
# os.rmdir('Folder') :- *If it is empty, it will get deleted.  *If it has files in it, there will be an error.  *If it does'nt exist, there eill be an error.