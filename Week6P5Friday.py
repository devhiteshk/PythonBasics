# Friday PROJECT

# Creating a database with CSV files

import csv
from IPython.display import clear_output


# Handling user registration and writing it to csv

def registerUser():
    with open("users.csv", mode='a', newline="") as f:
        writer = csv.writer(f, delimiter=",")
        print("To register, please enter your info: ")
        email = input("Enter E-mail: ")
        password = input("Enter Password: ")
        password2 = input("Re-type password: ")
        clear_output()
        if password == password2:
            writer.writerow([email, password])
            print("you are registered!")
        else:
            print("something went wrong! try again.")


# Handling user login

def loginUser():
    print("To login, please enter your info: ")
    email = input("email: ")
    password = input("password")
    clear_output()
    with open("users.csv", mode='r') as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row == [email, password]:
                print("you are logged in!")
                return True
    print("something went wrong! try again.")
    return False



# creating main loop

# main variables
active = True
logged_in = False

# main loop
while active:
    if logged_in:
        print("1. Logout\n2. Quit")
    else:
        print("1. Login\n2. Register\n3. Quit")

    choice = input("What would you like to do?:\t").lower()
    clear_output()
    if choice == "register" and logged_in== False:
        registerUser()
    elif choice == "login" and logged_in == False:
        logged_in == loginUser()
        logged_in = True
    elif choice == "quit":
        active == False
        print("Thanks for using our software!")
        break
    elif choice == "logout" and logged_in == True:
        logged_in = False
        print("You are now logged out.")
    else:
        print("Sorry, please try again!")
