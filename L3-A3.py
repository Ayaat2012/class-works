# A program to eliminate repeated lines from a file

# Creating output file
op_file = open('Updated.txt', 'w')

# Reading the input file
ip_file = open('Repeated.txt', 'r')

# holds lines already seen
lines_seen_so_far = set()
print("Eliminating duplicate lines...")
#literating each line in the file
for line in ip_file:

    #checking if line is unique
    if line not in lines_seen_so_far:

        #write unique lines in output file
        op_file.write(line)

        #adds unique lines to lines_seen_so_far
        lines_seen_so_far.add(line)

# Closing the file
ip_file.close()
op_file.close()