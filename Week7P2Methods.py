# Wednesday Methods
# Methods are essentially functions that are within classes. If you hear someone talking
# about methods, you’ll instantly know that they are talking about OOP

# defining and calling

class Dog:
    def makeSound(self):
        print("bark")


sam = Dog()
sam.makeSound()


# accessing class attributes within the class

class Dog:
    sound = "Bark"

    def makeSound(self):
        print(self.sound)  # # self required to access attributes  defined in the class


sam = Dog()
sam.makeSound()


# Method SCOPE

# Like global attributes, you may have methods that are accessible through the class itself
# rather than an instance of the class. These may also be known as static methods. They
# are not accessible by instances of the class.

# # understanding which methods are accessible via the class itself and
# class instances

class Dog():
    sound = "Bark"

    def makeSound(self):
        print(self.sound)

    def printInfo():
        print("I am dog")


Dog.printInfo()  # # able to run printInfo method because it does not include self parameter

# Dog.makeSound()   # Produce an error, self is in reference to instances only

sam = Dog()

sam.makeSound()  # able to access, self can reference the instance of sam


# sam.printInfo()     # will produce error, instances require the self parameter to access methods


# Passing arguments into methods

# writing methods that accept parameters

class Dog:
    def showAge(self, age):
        print(age)  # # does not need self, age is referencing the parameter not an attribute


sam = Dog()
sam.showAge(6)  # passing the integer 6 as an argument to the showAge method


# Using setters and getters

# They are methods that you
# create to re-declare attribute values and return attribute values.

# using methods to set or return attribute values, proper programming practice

class Dog:
    name = " "  # would normally use init method to declare, this is for testing purposes

    def setName(self, new_name):
        self.name = new_name  # declares the new value for the name attribute

    def getName(self):
        return self.name  # returns the value of the name attribute


sam = Dog()
sam.setName("Sammi")
print(sam.getName())  # prints the returned value of self.name


# Incrementing Attributes with Methods

# Like setters, when you want to alter an attributes value by incrementing or decrementing
# it rather than just changing it completely, the best way is to create a method to complete
# the task:

class Dog():
    age = 5

    def happyBirthday(self):
        self.age += 1


sam = Dog()
sam.happyBirthday()  # calls method to increment value by one
print(sam.age)  # better practice use getters, this is for testing


# Methods calling methods
# When calling a method from another method, you need to use the self parameter

# calling a class method from another method
class Dog:
    age = 6

    def getAge(self):
        return self.age

    def printInfo(self):
        if self.getAge() < 10:  # need self to call other method for an instance
            print("Puppy!")


sam = Dog()
sam.printInfo()


# Magic Methods

# All magic methods
# have two underscores before and after their name. When you print out anything,
# you’re accessing a magic method called __str__. When you use operators (+, -, /, ∗, ==,
# etc.), you’re accessing magic methods. They are essentially functions that decide what
# operators and other tasks in Python perform.

class Dog:
    def __str__(self):
        return "This is a dog class"

    
sam = Dog()
print(sam)      # will print the return of the string magic method
