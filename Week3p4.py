# Wednesday elif statements
x, y = 5, 10
if x > y:
    print("x is greater")
elif x < y:
    print("x is less")

# Multiple elif conditions
x, y = 5, 10
if x > y:
    print("x is greater")
elif (x+10) < y:
    print("x is less")
elif (x+5) == y:
    print("equal")

# Conditionals within conditionals
x, y, z = 5, 10, 5
if x > y:
    print("greater")
elif x<= y:
    if x == z:
        print("x is equal to z")
    elif x != z:
         print("x is not equal to z")

# testing output of two if statements in a row that are both true
x, y, z = 5, 10, 5
if x < y:
    print("x is less")
if x == z:
    print("x is equal")

# testing output of an if and elif statement that are both true
x, y, z = 5, 10, 5
if x < y:
    print("x is less")
elif x == z:
    print("x is equal to z")

# Wednesday Exercise

num = int(input("Enter a number"))
if num < 100:
    print("{} is lower than 100".format(num))
elif num > 100:
    print("{} is greater than 100".format(num))

x, y = 5, 10
if x > y:
    print("greater")
elif x < y:
    print("lower")