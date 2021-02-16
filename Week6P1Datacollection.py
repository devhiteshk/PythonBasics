# monday dictionaries

# A dictionary is a collection of unordered data, which is stored in key-value pairs.

# declaring a dictionary variable
empty = {}   # empty dictionary
person = {"name": "John Smith"}   # dictionary with one key/value pairs

customer = {
    "name": "Morty",
    "age": "26"
}                 # dictionary with two key/value pairs
print(customer)

# You could also use dict( ) to declare an empty dictionary.

# accessing dictionary information through keys
person = {"name": "John"}
print(person["name"])           # # access information through the key

# using get method to access dictionary information
person = {"name": "John"}
print(person.get("name"))
print(person.get("age", "Age is not available"))  # get is secure way to receive information


# storing a list within a dictionary and accessing it
data = {"sports": ["baseball", "football", "hockey", "soccer"]}
print(data["sports"][0])      # first access the key, then the index

# Keep in mind that we cannot create a dictionary that stores a list without first
# attaching a key:

# improperly storing a list within a dictionary
sports = ["baseball", "football", "hockey", "soccer"]
sports_dict = dict({"sports": sports})      # will produce error, no key
print(sports_dict)


# storing a dictionary within a list and accessing it
data = ["John", "Dennis", {"name": "Kirsten"}]
print(data[2])     # the dictionary is in index 2
print(data[2]["name"])     # first access the index, then access the key

# storing a dictionary within a dictionary and accessing it
data = {
    "team": "Boston Red Sox",
    "wins": {"2018": 108, "2017": 93}
}
print(data["wins"])         # will output the dictionary within the wins key
print(data["wins"]["2018"])      # first access the wins key, then the next key


# Monday Exercises
# 1
name = input("Enter your name: ")
age = input("Enter your age: ")

data = {"name": name, "age": age}
print(data)

# 2
pizza = {
    'ingredients': ['cheese', 'sausage', 'peppers']
}

for key, value in pizza.items():
    x = value

for i in range(0, len(x)):
    print(x[i])
