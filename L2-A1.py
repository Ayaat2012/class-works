#open file and read its contents
file = open('Codingal.txt', 'r')
print(file.read())
file.close()

#open file and read its first 8 characters
file = open('Codingal.txt', 'r')
print("\nRead in parts\n")
print(file.read(8))
file.close()

#append your name and age in the file
file = open('Codingal.txt', 'a')
file.write("Hi! I'm Penguin. And I am 1 y/o")
file.close()