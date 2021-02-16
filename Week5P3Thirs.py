# where global variables can be accessed
number = 5


# def scopeTest():
#  number += 1  # not accessible due to function level scope


# scopeTest()

# accessing variables defined in a function
def scopeTest():
    word = "function"
    return word


value = scopeTest()
print(value)

# changing list item values by index
sports = ["baseball", "football", "hockey", "basketball"]


def change(aList):
    aList[0] = "soccer"


print("Before Altering: {}".format(sports))
change(sports)
print("After Altering: {}".format(sports))


# Thursday Exercise

names = ['Bob', 'Rich', 'Amanda']
def changeValue(aList, name, index):
    aList[index] = name
    return aList

print(changeValue(names,'Bill', 1))
print(changeValue(names,'Hitesh', 2))