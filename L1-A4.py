# Program to append contents of one file to another file

#Entering the file names
first_file = input("Enter the name of the first file")
second_file = input("Enter the name of the second file")

#Opening bothe files in read only mode to read intial contents
f1 = open(first_file, 'r')
f2 = open(second_file, 'r')

#Printing the contents of the files before appending
print('content of first file before appending -\n', f1.read())
print('content of second file before appending -\n', f2.read())

#Closing the files
f1.close()
f2.close()

#Opening first file in append mode and second file on read mode
f1 = open(first_file, 'a+')
f2 = open(second_file, 'r')

#Appending the contents of the first file to the second file
f1.write(f2.read())

#Relocating the cursor of the files at the beginning
f1.seek(0)
f2.seek(0)

#Printing the contents of the files after appending
print('content of first file after appending -\n', f1.read())
print('content of second file after appending -\n', f2.read())

#Closing the files
f1.close()
f2.close()