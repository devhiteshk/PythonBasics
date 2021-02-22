# ADVANCED TOPICS : Efficiency

# MONDAY: LIST COMPREHENSION

# List comprehension allows us to create a list filled with data in a single line. Rather
# than creating an empty list, iterating over some data, and appending it to the list all on
# separate lines, we can use comprehension to perform all these steps at once.


# SYNTAX = *result* = [*transform*  *iteration*  *filter*]

# For example, when you want to populate a list, the syntax would have the following
# structure:

# name_of_list = [ item_to_append for item in list ]

# However, when you want to include an if statement, the comprehension would look
# like the following:

# name_of_list = [ item_to_append for item in list if condition ]

# Lastly, if you would like to include an else condition, it would look like
# the following:

# name_of_list = [ item_to_append if condition else item_to_append for item in list ]

# Generating a list of numbers

nums = [x for x in range(100)]
print(nums)


# using list statements within list comprehension

nums = [x for x in range(10) if x % 2 == 0]
print(nums)


# Using if/else statement within list comprehension

nums = ["Even" if x % 2 == 0 else "odd" for x in range(10)]
print(nums)


# list comprehension with variables

# creating a list of squared numbers from another list of numbers using list comprehension

nums = [2, 4, 6, 8]
sq_nums = [num**2 for num in nums]
print(sq_nums)


# DICTIONARY comprehension

# Not only can you use comprehension on lists but also Python dictionaries as well. The
# syntax structure is the exact same, except you need to include a key-value pair instead of
# a single number to insert into the dictionary.

# creating a dictionary of even numbers and square values using comprehension

numbers = [x for x in range(10)]
squares = {num: num**2 for num in numbers if num % 2 == 0}
print(squares)

# Monday exercises

# 1 deg to farenheit
degrees = [12, 21, 15, 32]
faren = [((9/5)*i) + 32 for i in degrees]
print(faren)

# user input
num = 0
while num <= 100:
    num = int(input("enter a number between 1 and 100: "))
    out = [x for x in range(1,101) if x%num == 0]
    print(out)









