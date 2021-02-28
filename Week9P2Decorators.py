# Tuesday Decorators

# Decorators, also known as wrappers, are functions that give other functions extra
# capabilities without explicitly modifying them. They are denoted by the “@” symbol
# in front of the function name, which is written above a function declaration like the
# following:
# @decorator
# def normalfunc():


# Higher-Order Functions

# A higher-order function is a function that operates on other functions, either by taking
# a function as its argument or by returning a function.


# Creating and Applying a Decorator

def decorator(func):
    def wrap():
        print("=======")
        func()
        print("=======")

    return wrap


@decorator
def printName():
    print("John!")


printName()


# creating a decorator that takes in parameters


def run_times(num):
    def wrap(func):
        for i in range(num):
            func()

    return wrap


@run_times(4)
def sayHello():
    print("Hello!")


# When passing an argument into a decorator, the function is automatically
# run, so we do not need to call sayHello in this instance

# Functions with decorators and parameters

def birthday(func):
    def wrap(name, age):
        func(name, age + 1)

    return wrap


@birthday
def celebrate(name, age):
    print("Happy birthday {}, you are now {}".format(name, age))


celebrate("paul", 43)


# Restricting function access

# real world sim, restricting function access

def login_required(func):
    def wrap(user):
        password = input("What is the password?")
        if password == user["password"]:
            func(user)
        else:
            print("Access Denied")

    return wrap


@login_required
def restrictedFunc(user):
    print("Access granted, welcome {}".format(user["name"]))


user = {"name": "Jess", "password": "ilywpf"}
restrictedFunc(user)


# Tuesday Exercises

def number(func):
    def wrap(num):
        if num < 100:
            func(num)
        else:
            None
    return wrap

@number
def numbers(num):
    print("Less than 100")


num = 99
numbers(num)


# 2

def route(stringIn):
    def wrap(func):
        print(stringIn)
        func()
    return wrap


@route("/index")
def index():
    print("This is how web pages are made in Flask")














