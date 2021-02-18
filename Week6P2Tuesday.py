# Tuesday working with dictionary

# adding new key/value pairs to a dictionary

car = {"year": 2018}
car["color"] = "Blue"
print("year:{}\t Color:{}".format(car["year"], car["color"]))

# Changing information

# updating a value for a key/value pair that already exist

car = {"year": 2018, "color": "Blue"}
car["color"] = "Red"

print("Year:{} \t Color:{}".format(car["year"], car["color"]))

# Deleting information

# deleting a key /value pair from a dictionary

car = {"year": 2018}
try:
    del car["year"]
    print(car)

except:
    print("that key does not exist")

# Looping a dictionary

# Dictionaries are iterable like lists. However, they have three different methods for doing
# so. You can iterate over both the keys and values together, only keys, or only values.

# 1 looping over a dictionary via keys

person = {"name": "John", "age": 26}
for key in person.keys():
    print(key, "   ", person[key])      # will output the value at the current key


# 2 looping over a dictionary via the values
person = {"name": "John", "age": 26}
for value in person.values():
    print(value)

# 3 looping over a dictionary via the key/value pair
person = {"name": "John", "age": 26}
for key, value in person.items():
    print("{}: {}".format(key, value))


# Tuesday Exercises
# 1

epty = {}
uname = input("please enter your name: ")
uaddress = input("please enter your address: ")
unumber = input("please enter your number: ")

epty["name"] = uname
epty["address"] = uaddress
epty["number"] = unumber

for key,value in epty.items():
    print("{} : {}".format(key,value))

# challenge complete

# 2
# What is wrong with the following code:
person = {'name', 'John Smith'}       # : sign should be there between key and value
print(person['name'])



