# Tuples sets and frozen sets

# A tuple is identical to a list, except it is immutable. When something is immutable, it
# means that it cannot be altered once declared. Tuples are useful for storing information
# that you don’t want to change. They’re ordered like lists, so you can iterate through them
# using an index.

# declaring a tuple

t1 = ("hello", 2, "hello")  # with parens
t2 = True, 1  # without parens
print(type(t1), type(t2))  # both are tuples
# t1[0] = 1            # will crash, tuples are immutable once declared

# The only way to overwrite the data within a tuple is to re-declare the
# entire tuple.


# Sets share the same characteristics of lists and dictionaries. A set is a collection of
# information like a list; however, like a key in a dictionary, sets can only contain unique
# values. They are also an unordered collection. This means that they cannot be accessed
# by index but rather by the value itself like dictionary keys


# Declaring a set

s1 = set([1, 2, 3, 1])              # uses the set keyword and square brackets
s2 = {4, 4, 5}                  # uses curly brackets, like dictionary
print(type(s1), type(s2))


s1.add(5)            # using the add method to add new items to a set
s1.remove(1)         # using the remove method to get rid of the value 1
print(s1)            # notice when printed it removed the second "1" at the end
print(s2)


# Frozenset are essentially the combination of a set and a tuple. They are immutable,
# unordered, and unique. These are perfect for sensitive information like bank account
# numbers, as you wouldn't want to alter those.

# declaring a frozenset

fset = frozenset([1, 2, 3, 4])
print(type(fset))

# Wednesday exercise
# 1

accountNo = []
steps = 0
acNo = 0
while acNo != "Done":
    acNo = input("Enter Account Number/Done: ").title()
    if acNo == "Done":
        break
    else:
        accountNo.append(acNo)

FrzAccounts = frozenset(accountNo)
print(FrzAccounts)


# 2

nums = [3, 4, 3, 7, 10]
z = frozenset(nums)
print(z)


nums = [3, 4, 3, 7, 10]
step = 0
for i in range(0, len(nums)-1):
    if nums[step] == nums[i]:
        nums.pop(i)
    else:
        step = 0
print(nums)

# challenge complete

