# Tuesday : IF STATEMENTS

# using an if statement to only run code if the condition is met
x, y = 5, 10
if x < y:
    print("x is less than y")

# Checking user input
ans = int(input("what is 5 + 5? "))
if ans == 10:
    print("you got it right!")


# LOGICAL OPERATORS
# AND

x,y,z = 5, 10, 5
if x<y and x == z:
    print("both statements were true")

# OR operator
x, y, z = 5, 10, 5
if x<y or x!=z:
    print("One or Both statements were true")

# NOT operator
flag = False
if not flag:       # same as if flag==False
    print("Flag is False")

# MEMBERSHIP operators
# IN

word = "Baseball"
if "b" in word:
    print("{} contains the character b".format(word))

# NOT IN
if "x" not in word:
    print("{} does not contain the character x".format(word))




