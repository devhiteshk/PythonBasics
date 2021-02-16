# COMMENTS AND BASIC DATA TYPES

# this is a comment

print("hello")   #A print statement

"""

        This is a multiline comment

"""

# Data Types are Integers  Float   Boolean   String
#                   5       5.7     true      "hii"

# following are all integers
print(2)
print(10)

# following are all floats
print(10.935)
print(8.0)

# the following are all boleans
print(True)
print(False)

# following are the strings
print("")       # print a empty line
print("there's a snake in my boot!")
print('True')

# MONDAY EXERCISE
print("Hitesh Kumar")
print(type(int))   # will output <class 'int'>

# TUESDAY : VARIABLES

first_name = "John"    # A str data type is stored in first_name

# integer and float variables

num1 = 5   # storing int type in num1
num2 = 8.4 # storing float type in num2
print(num1, num2)

# Boolean variables

# storing boolean into a variable
switch = True
print(switch)

# STRING variables

# storing string into a variable
name = 'John Smith'
fav_number = '9'
print(name, fav_number)  # will print 9 next to the name

# Using multiple variables to create another variable
result = num1 + num2
print(result)

# USING OPERATORS ON NUMERICALS VARIABLES

#  Adding, deleting, multiplying, dividing, from a variable
result += 1  # same as saying result = result +1
print(result)
result *= num1  # same as  saying result = result * num1
print(result)


# Overwriting previously created variables

# defining a variable and overwriting it's value

name = 'John'
print(name)
name = 'Sam'
print(name)

# WHITESPACE
name = 'John Smith'

# Tuesday Exercise
# 1 calculating product of two numbers and giving out result
x = 3
y = 10
result = x*y
print(x,'+',y,'=',result)

# Area calculation
L = 245.54
B = 13.66
result = L*B
print('Area of Rectangle is =',result)

# WEDNESDAY : Working with strings

# string Concatenation
name = "John" + " " + "Smith"
print(name)

first_name = "john"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)

# Fomatting strings

# .format()
# injecting variables using the format method
name = "John"
print("Hello {}".format(name) )
print("Hello {}, you are {} years old!".format(name,28))

# f Strings
# using the new fstring in python
name = "John"
print(f"Hello{name}")

# In Python 2
# python 2 multiple variable formatting
first_name = "John"
last_name = "Smith"
print( "Hello, %s %s" % (first_name, last_name) )
# surround the variables in parenthesis

# STRING INDEX
# in python index staets with 0

# Using indexes to print each element
word = "Hello"
print( word[0])        # will output 'H'
print( word[1])        # will output 'e'
print( word[-1])       # will output 'o' the last element of string

# String Slicing
print( word[0:2])             # will output He

# variable_name[start : stop : step]
print( word[0:5:2])           # will output 'Hlo'

# Wednesday Exercise
# 1

print("{} years old {} inch. tall man gave {} statement his name is {}".format(23,4.5,False,name))

print("{}'s favourite sports is {}.".format('Hitesh','Cricket'))
print("{}'s is working on {} programming!".format('Deepak','Py4e'))


# THURSDAY String manipulation
# .title()
# using the title method to capitalize a string

name = "john smith"
print( name.title())     # Gives John Smith
print( name.lower())     # All lower case
print( name.upper())     # All upper

# .replace()
# replacing an exclamation point with a period
words = "Hello there!"
print( words.replace( "!", "." ) )  # replace ! with .
words = words.replace('!','.')

# .find()
# finding the starting index of our searched ter
s = "Look over that way"
print(s.find("over"))        # returns starting position of over

# .strip()
# removing white space with strip
name = "  john  "
print(name.strip())          # removes spaces from both sides
print(name.lstrip())         # removes spaces from left side
print(name.rstrip())         # removes spaces from right side


# .split()
# converting a string into a list of words
s = "These words are separated by spaces"
print( s.split(" "))

# Thursday exercises
# 1 Uppercasing
st = "uppercase"
print(st.upper())

# 2 Strip symbols
c = "$$John Smith"
print(c.strip("John Smith"))
print(c.strip("JohnSmit "))
print(c.lstrip("$$"))

# Challenge : Reverse a String by Slice
AN = "Hello"
print(AN[::-1])
# Go to W2 Receipt printing Program




















