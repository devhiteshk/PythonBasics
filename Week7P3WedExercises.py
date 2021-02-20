# 1. SETTER AND GETTER TO CHANGE ATTRIBUTE

class animals:
    def __init__(self, species=0):
        self.species = species

        # getter method

    def Getter(self):
        print(self.species)

        # setter method

    def Setter(self, species):
        self.species = species


Lion = animals()
Lion.Setter("Feline")
Lion.Getter()

# User input

class person:
    def __init__(self,name, age= 0):
        self.name = name

    def Setter(self):
        age = input("Please enter your age: ")
        self.age = age

    def Getter(self):
        print("You are {} years old".format(self.age))

p1 = person("hitesh")
p1.Setter()
p1.Getter()

