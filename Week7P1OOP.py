# WEEK 7 Object oriented Programming

values = {4: 4, 8: 8, "Q": 10, "ACE": 11}
card = ("Q", "Hearts")
print("{}".format(values[card[0]]))


# Monday: Creating and instantiating a class

# All objects in Python are created from classes. The point of OOP is to reuse the same
# code while giving flexibility to create each object with their own features.

# OOP Stages

# There are two stages when using classes. The first stage is the class definition. Like
# function definitions, this stage is where you write the blueprint to be used when called.
# The second stage is called instantiation. It is the process of creating an object from the
# class definition. After an object is instantiated, it is known as an instance.

# The first step in using classes is creating the class definition or “blueprint.” To create
# a new class, the syntax is like functions, but you use the class keyword instead of def.


# DEFINING FIRST CLASS
class Car:
    pass  # simply using as a placeholder until we add more code tomorrow


ford = Car()  # Creating first instance
print(ford)

subaru = Car()  # Creating multiple instances
print(hash(ford))
print(hash(subaru))  # # hash outputs a numerical representation of the location in memory for the variable


# Monday exercises

class animals:
    pass


lion = animals()
tiger = animals()


class Bus:
    pass


school_bus = Bus()


# Tuesday : ATTRIBUTES

# Today, we’ll begin to understand
# how to give personalized features, known as attributes, to classes and their instances.
# Attributes are just variables defined within a class, nothing more than that

# how to define attributes

class Car:
    sound = "beep"
    color = "red"


ford = Car()
print(ford.color)  # known as 'dot syntax'


# Changing the value of an attribute
class Car():
    sound = "beep"
    color = "red"


ford = Car()
print(ford.sound)
ford.sound = "honk"

print(ford.sound)


# USING the __init__() method

# When you want to instantiate
# an object with specific properties, you need to use the initialization (init) method.
# Whenever an instance is created, the init method is called immediately.


# using the init method to give instances personalized attributes upon creation

class Car:
    def __init__(self, color):
        self.color = color  # sets the attribute color to the value passed in


ford = Car("blue")  # instantiating a Car class with the color blue
print(ford.color)


# The self keyword

# The self keyword is a reference to the current instance of the class and is used to access
# variables and methods associated with that instance.

# Instantiating Multiple Objects with __init__()

# defining different values for multiple instances

class Car:
    def __init__(self, color, year):
        self.color = color
        self.year = year


ford = Car("Blue", 2016)
subaru = Car("red", 2018)

print(ford.color, ford.year)
print(subaru.color, subaru.year)


# Global attributes vs. Instance attributes

# Global attributes can be referenced by the class directly and all
# its instances, whereas instance attributes (which are defined within the init method)
# can only be accessed by the class instances. If an attribute is declared inside of a class,
# but not within the init method, then it is known as a global attribute. Any attributes
# declared within the init method using the self keyword are instance attributes


# using and accessing global class attributes

class Car:
    sound = "Beep"  # global attribute, accessible through the class itself

    def __init__(self, color):
        self.color = "blue"  # # instance specific attribute, not accessible through the class itself


print(Car.sound)
# print(Car.color)     won't work, as color is only available to
#                      instances of the Car class, not the class itself

ford = Car("Blue")
print(ford.sound, ford.color)  # color will work as this is an instance


# Tuesday Exercise

class Dog:
    species = "Canine"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


dog1 = Dog("Sammi", "Husky")
dog2 = Dog("Casey", "Chocolate_Lab")

print(dog1.name, dog1.breed)
print(dog2.name, dog2.breed)


class Person:
    def __init__(self, name):
        self.name = name


N = input("Enter your name: ")
P1 = Person(N)
print(P1.name)