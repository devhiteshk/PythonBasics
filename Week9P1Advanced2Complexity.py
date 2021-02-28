# Monday: Generators and Iterators

# you may have seen the words generators or iterators
# mentioned. Without knowing, you’ve been using them the entire time. Today, we’ll dive
# into what each of these concepts are and how to use them.

# An iterator is an object that contains items which can be iterated upon, meaning
# you can traverse through all values. An iterable is a collection like lists, dictionaries,
# tuples, and sets. The major difference is that iterables are not iterators; rather they are
# containers for data.

# Creating a basic Iterator

sports = ["baseball", "soccer", "football", "hockey", "basketball"]
my_iter = iter(sports)
print(next(my_iter))
print(next(my_iter))
for item in my_iter:
    print(item)


# print(next(my_iter))           # Will produce error


# Creating our own iterator

class Alphabet():
    def __iter__(self):
        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.index = 0
        return self

    def __next__(self):
        if self.index <= 25:
            char = self.letters[self.index]
            self.index += 1
            return char
        else:
            raise StopIteration


for char in Alphabet():
    print(char)


# GENERATORS

# Generators are functions that yield back information to produce a sequence of results
# rather than a single value. They’re a way to simplify the creation of an iterator. Normally,
# when a function has completed its task and returned information, the variables declared
# inside of the function will be deleted. With generators, however, they use the “yield”
# keyword to send information back to the location it was called without terminating the
# function. Generators don’t always have to yield back integers though you can yield any
# information you’d like.


# creating a range generator


def myRange(stop, start=0, step=1):
    while start < stop:
        print("Generator Start value: {}".format(start))
        yield start
        start += step


for x in range(5):
    print("For loop X value: {}".format(x))


# Monday Exercise

# 1 Reverse iterator












