# Program to count number of files in "Codingal.txt" file
# Opening a file
file = open('Codingal.txt', 'r')
counter = 0

#Reading from file
Content = file.read()

# Spliting contents into lines and storing them into a list
CoList = Content.split("\n")
print(CoList)
for i in CoList:
    if i:
        counter += 1
print("This is the number of lines in the file")
print(counter)