# Wednesday: RETURN STATEMENT

def returnMultiple():
    a = 5
    b = 10
    return [a, b]


# using return keyword to return the sum of two numbers
def addNums(num1, num2):
    return num1 + num2


num = addNums(5.5, 4.5)  # saves returned value into num
print(num)
print(addNums(10, 10))  # doesn't save returned value


# shorthand syntax using a ternary operator
def searchList(aList, el):
    return True if el in aList else False


result = searchList(["one", 2, "three"], 2)  # result = True
print(result)


# Wednesday exercise
# 1 full name

def FullName(fname, lname):
    return fname + ' ' + lname


name = FullName('hitesh', 'kumar')
print(name)


# 2 user input
def userInput():
    value = input("enter a value: ")
    return int(value)


z = userInput() + 23
print(z)
