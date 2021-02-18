# Reading and writing files

# Python comes with an open() function that allows us to create or modify
# files. This function accepts two parameters, the file name, and the mode. If the file name
# exists, then it will simply open the file for modification; otherwise, it will create the file
# for you. The mode is in reference to how Python opens and works with the file.

# opening/creating and writing to a text file

f = open("test.txt", 'w+')  # open file in writing and reading mode
f.write('Hii this is how we write in a file')
f.close()

# reading from a text file

f = open("test.txt", "r")
data = f.read()
f.close()
print(data)

# CSV files work with data by separating a comma between each cell. This is known as a
# tabular data structure. To get started working with them, Python has a default library
# called “csv.”

import csv

with open("test.csv", mode='w', newline="") as f:
    # the second method of opening files using the “with” keyword. This
    # concept works like a while loop, so that while the file is open, we can work with it, and
    # once the block of code is done running, it closes the file automatically for us.

    writer = csv.writer(f, delimiter=",")
    writer.writerow(["Name", "City"])
    writer.writerow(["Craig Lou", "Taiwan"])

# reading from csv files


with open("test.csv", mode="r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        print(row)

# File modes in python

# ‘r’ This is the default mode. It opens the file for reading only.
# ‘w’ Opens file for writing. If file doesn't exist, it creates one.
# ‘x’ Creates a new file. If file exists, the operation fails.
# ‘a’ Open in append mode. If file doesn't exist, it creates one.
# ‘b’ Open in binary mode.
# ‘+’ Will open a file for reading and writing. Good for updating.

# Thursday Exercise

favNo = input("Enter your favourite number: ")
fi = open("fav.txt", 'w+')
fi.write(favNo)
fi.close()

fi = open("fav.txt", 'r')
data = fi.read()
fi.close()
print(data)

# 2  Dumping data

dict_data = {
    'name': ['Dave', 'Dennis', 'Peter', 'Jess'],
    'language': ['Python', 'C', 'Java', 'Python']
}

R = len(dict_data['name'])
print(R)

import csv

with open('data.csv', mode='w+', newline="") as file:
    fieldnames = ['name', 'language']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(0, R):
        writer.writerow({'name': dict_data['name'][i], 'language': dict_data['language'][i]})

file = open("data.csv", 'r')
data = file.read()
file.close()
print(data)

# Challenge completed
