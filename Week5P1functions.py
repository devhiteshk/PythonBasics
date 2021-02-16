# Creating and calling functions

# Monday

# A function is a block of code which only runs when it is called
# You can pass data, known as parameters, into a function
# A function can return data as a result

# def FunctionName(parameter):

def printInfo():  # defines a function
    print("Name: John Smith")
    print("Age: 45")


printInfo()
printInfo()


# performing a calculation in a function
def calc():
    x, y = 5, 10
    print(x + y)


calc()


def myName():
    print("Hitesh Kumar")


myName()


def pizzaToppings():
    print("Tomato")
    print("mushroom")
    print("onion")
    print("chicken")


pizzaToppings()


# Tuesday

def printName(name):
    print('Hello {}'.format(name))


printName('John')


# passing a single parameter into a function
def printName(full_name):
    print("Your name is: {}".format(full_name))


printName("John Smith")
printName("Amanda")


# passing multiple parameters into a function
def addNums(num1, num2):
    result = num1 + num2
    print("{} + {} = {}".format(num1, num2, result))


addNums(5, 8)  # will output 13
addNums(3.5, 5.5)  # will output 9.0

# using a function to square all information
numbers1 = [2, 4, 5, 10]
numbers2 = [1, 3, 6]


def squares(nums):
    for num in nums:
        print(num ** 2)


squares(numbers1)
squares(numbers2)


# setting default parameter values
def calcArea(r, pi=3.14):
    area = pi * (r ** 2)
    print("Area: {}".format(area))


calcArea(2)  # assuming radius is the value of 2


# setting default parameter values
def printName(first, last, middle=""):
    if middle:
        print("{} {} {}".format(first, middle, last))
    else:
        print("{} {}".format(first, last))


printName("John", "Smith")
printName("John", "Smith", "Paul")  # will output with middle name


# explicitly assigning values to parameters by referencing the name
def addNums(num1, num2):
    print(num2)
    print(num1)


addNums(5, num2=2.5)


# using args parameter to take in a tuple of arbitrary values
def outputData(name, *args):
    print(type(args))
    for arg in args:
        print(arg)


outputData("John Smith", 5, True, "Jess")


# using kwargs parameter to take in a dictionary of arbitrary values
def outputData(**kwargs):
    print(type(kwargs))
    print(kwargs["name"])
    print(kwargs["num"])
    print(kwargs["b"])


outputData(name="John Smith", num=5, b=True)

# Tuesday exercise

w = input("Enter a word: ")
print(w[0])


def CheckUpper(i):
    if i[0] == i[0].upper():
        print("True")
    else:
        print("false")


CheckUpper(w)


# Question 2

def NoName(first_name="",last_name=""):
    if first_name or last_name:
        print(first_name,last_name)
    else:
        print("No name passed in")

NoName("Hitesh","Kumar")
NoName()