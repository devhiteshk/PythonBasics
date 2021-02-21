# Thursday :  INHERITANCE

# Sometimes you’ll create classes that will have similar attributes or methods. Take a Dog
# and Cat class, for example. Both will have nearly the same code, attributes, and methods.
# Rather than writing the same code twice, we use a concept called inheritance.

# Inheritance is one of the concepts that allow classes to have code re-usability within
# programming. When you have two or more classes that use similar code, you generally
# want to set up what is called a “superclass.” The two classes that will inherit all the code
# within the superclass are known as “subclasses.”

# inheriting a class and accessing the inherited method

class Animal:
    def makeSound(self):
        print("roar")


class Dog(Animal):  # Inheriting class animal
    species = "Canine"


sam = Dog()
sam.makeSound()
lion = Animal()


# lion.species not accessible, because inheritance does not work backwards


# Using the super() method to declare inherited attributes

# The super method is used to create forward compatibility when using inheritance. When
# declaring attributes that are required within the superclass, super is used to initialize its
# values.


class Animals:
    def __init__(self, species):
        self.species = species


class Dog(Animals):
    def __init__(self, species, name):
        self.name = name
        super().__init__(species)  # using super to declare the species attribute defined in Animal


sam = Dog("Canine", "Sammi")
print(sam.species)


# Method Overriding

# Sometimes when using inheritance, you want the subclass to be able to perform a
# different action when the same method is called. Take our makeSound method from the
# previously created Animal class. It prints out “roar”, but that’s not the sound you want
# dogs making when you create your Dog class. Instead, we use the concept of method
# overriding to change what the method does.

# overriding methods defined in the superclass

class Animal:
    def makeSound(self):
        print("Roar")


class Dog(Animal):
    def makeSound(self):
        print("bark")


sam, lion = Dog(), Animal()  # declaring multiple variables on a single line

sam.makeSound()  # overriding will call the makeSound method in Dog
lion.makeSound()  # no overriding occurs as Animal does not inherit anything


# Inheriting multiple classes


# The main difference is how you super the attributes.
# Rather than using the super method, you call the class name directly and pass in the self
# parameter with the attributes. Let’s see how:

class Physics:
    gravity = 9.81


class Automobile:
    def __init__(self, make, model, year):
        self.make, self.model, self.year = make, model, year
        # declaring all attributes on one line


class Ford(Physics, Automobile):
    def __init__(self, model, year):
        Automobile.__init__(self, "Ford", model, year)  # super does not work with multiple


truck = Ford("F-150", 2018)
print(truck.gravity, truck.make)


# Thursday Exercises

class Characters(object):
    def __init__(self, name, team, height=0, weight=0):
        self.name, self.team, self.height, self.weight = name, team, height, weight

    def sayhello(self):
        return "Hello, my name is {} and I'm on the {} guys".format(self.name, self.team)


class goodPlayers(Characters):
    def __init__(self, name, team):
        self.name, self.team = name, team
        super().__init__(name, team, height=0, weight=0)


class badPlayers(Characters):
    def __init__(self, name, team):
        self.name, self.team = name, team
        super().__init__(name, team, height=0, weight=0)


G1 = goodPlayers("Max", "good")
B1 = badPlayers("Tony", "bad")

print(G1.sayhello())
print(B1.sayhello())


# Done
