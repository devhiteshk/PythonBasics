# Lists and Loops

# declaring a list of numbers
nums = [5, 10, 15.2, 20]
print(nums)

# accessing elements within a list
print(nums[1])
num = nums[2]
print(num)

# declaring a list of mixed data types
num = 4.3
data = [num, "word", True]
print(data)

# list within lists
data = [5, "book", [34, "hello"], True]
print(data)
print(data[2])

# Accessing lists within lists
print(data[2][0])
print(data[2][1])
print(data[2][1][0])

# changing values in a list
data = [5, 10, 15, 20]
print(data)
data[0] = 100
print(data)

# Variable storage in ID
a = [5, 10]
print(id(a))

# Understanding how lists are sorted
a = [5, 10]
b = a
print("a: {}\t b: {}".format(a, b))
print("location a[0]: {}\t location b[0]: {}". format(id(a[0]), id(b[0])))
a[0] = 20          # # re-declaring the value of a[0] also changes b[0]
print("a: {}\t b: {}".format(a, b))

# COPYING A LIST
# using [:] to copy a list
data = [5, 10, 15, 20]
data_copy = data[:]         # a single colon copies the list
data[0] = 50
print("data: {}\t data_copy: {}".format(data, data_copy))
data_c_method = data_copy.copy()
print("data_c_copy: {}".format(data_c_method))


# MONDAY EXERCISE

# 1
sports = ["cricket", "basketball", "football", "chess"]
print("i like to play {}".format(sports[0]))
print("i like to play {}".format(sports[1]))
print("i like to play {}".format(sports[2]))
print("i like to play {}".format(sports[3]))

# 2
names = ['John', 'Abraham', 'Sam', 'Kelly']
print(names[0][0], names[1][0], names[2][0], names[3][0])

# lists complete imp part is copying a list and manipulating items
