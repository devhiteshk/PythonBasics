# Challenge question with 2 story lines
print(" What you would like to choose!\n1. AGE GROUP\n2. CALCULATOR")
print("Choose 1 or 2")
choose = input()
if choose == "1":

    Age = float(input("Enter the age to know your age group:\t"))
    print("Your age is {}".format(Age))
    if 0 < Age <= 12:
        print("Kid")
    elif 13 <= Age <= 19:
        print("Teenager")
    elif 20 <= Age <= 30:
        print("Young Adult")
    elif 31 <= Age <= 64:
        print("Adult")
    elif Age >= 65:
        print("Senior")
    else:
        print("Error: Please enter a valid age")

# FRIDAY: CREATING A CALCULATOR

# step 1: ask user for calculation to be performed
elif choose == "2":

    operation = input("Would you like to add/subtract/multiply/divide?:\n").lower()
    print("You have chosen to {}".format(operation))

    # Step 2 : ask for number inputs
    if operation == "subtract" or operation == "divide":
        print("you chose {}".format(operation))
        print("Please keep in mind that order matters.")
    num1 = input("Enter the first number: \t")
    num2 = input("Enter the second number: \t")
    print("First Number : {}".format(num1))
    print("Second Number : {}".format(num2))

    # Ask to reverse the order of number

    order = input("Do you want to reverse the order of number: Y/N\t")
    if order == "Y":
        num3 = num1
        num1 = num2
        num2 = num3
        print("corrected order is\nNumber 1: {} \nNumber 2: {}".format(num1, num2))
    elif order == "N":
        num1 = num1
        num2 = num2

    # step 3: Set up try/ except for mathematical operation

    try:
        # convert to float
        num1, num2 = float(num1), float(num2)
        if operation == "add":
            result = num1 + num2
            print("{} + {} = {}".format(num1, num2, result))
        elif operation == "subtract":
            result = num1 - num2
            print("{} - {} = {}".format(num1, num2, result))
        elif operation == "multiply":
            result = num1*num2
            print("{} * {} = {}".format(num1, num2, result))
        elif operation == "divide":
            result = num1/num2
            print("{}/{} = {}".format(num1, num2, result))
        else:
            print("Sorry but {} is not an option.".format(operation))

    except:
        print("Error: Improper numbers used. Please try again.")

else:
    print("ERROR: Please choose between 1 and 2 only")
