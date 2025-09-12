#Program to copy odd lines of one file to another

# Opening the file in read mode
fn = open('Codingal.txt', 'r')

# Opening other file in write mode
fn1 = open('CodingalUpdated.txt', 'w')

#read the contents of the file
cont = fn.readlines()
type(cont)
for i in range(1, len(cont)+1):
    if(i % 2 != 0):
        fn1.write(cont[i-1])
        
    else:
        pass

#Close the file
fn1.close()

#open file in read mode
fn1 = open('CodingalUpdated.txt', 'r')

#read the contents of the file
cont1 = fn1.read()

#print the contents of the file
print(cont1)

#close all files
fn.close()
fn1.close()