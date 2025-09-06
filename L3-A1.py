# Write in file using with() function
with open('Codingal.txt', 'w') as file:
    file.write("Hi, I am Penguin and I am 1 year old.")


# Split file into words
with open('Codingal.txt', 'r') as file:
    data = file.readlines()
    print(data)

    print("Words in the file are...")
    for line in data:
        word = line.split()
        print(word)