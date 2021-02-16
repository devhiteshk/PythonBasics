# THURSDAY : Else statement
name = "John"
if name == "Jacob":
    print("Hello Jacob!")
else:
    print("Hello {}!".format(name))

# Completing Conditional Statement
name = "John"
if name[0] == "A":
    print("name starts with A")
elif name[0] == "B":
    print("Name starts with B")
elif name[0] == "J":
    print("Nmae starts with J")
else :
    print("Name starts with {}".format(name[0]))

# THURSDAY Exercise:
name = "John"
if name == "Jack":
    print("Hello Jack")
else:
    print("Hello John")

tim = int(input("Enter the time:\n"))
if tim < 1200:
    print("Good morning")
elif tim == 1200 or tim<1700:
    print("Good Afternoon")
else:
    print("good evening")
