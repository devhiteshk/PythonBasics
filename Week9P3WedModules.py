# MODULES

# Most programs tend to include so many lines of code that you wouldn’t store it all within
# a single file. Instead you separate the code into several files, which helps to keep the
# project organized. Each one of these files is known as modules. Within these modules
# are variables, functions, classes, etc., that you can import into a project.


# import the entire math module
import math

print(math.floor(2.5))  # rounds down

print(math.ceil(2.5))  # round up

print(math.pi)

# importing only variables and functions rather than an entire module, better efficiency
from math import floor, pi

print(floor(2.5))
# print( ceil(2.5) ) # will cause error as not imported

print(pi)

# Often, the name of what you’d like to import can be lengthy. Rather than having to write
# out an entire name each time you’d like to use it, you can give an “alias” or nickname
# when importing:


from math import floor as f

print(f(2.5))

# Creating your own module in text editor file test.py

# Using our module

from test import length, width, printInfo
print(length, width)
printInfo("John Smith", 37)

# Wednesday Exercises

import time as t
t.sleep(5)
print("Time module imported")


from calculation import calArea
calArea(15, 30)


