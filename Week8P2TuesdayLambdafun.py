# Tuesday: Lambda functions

# Lambda functions, otherwise known as anonymous functions, are one-line functions
# within Python. Like list comprehension, lambda functions allow us to reduce the lines of
# code we need to write within our program. It doesn't work for complicated functions but
# helps to improve readability of smaller functions.

# syntax:
# lambda arguments : expression

# lambda arguments : value_to_return if condition else value_to_return

# using a lambda to square a number
(lambda x: print(x ** 2))(4)

# Passing multiple argument
(lambda x, y: print(x * y))(10, 5)

# saving a lambda function

square = lambda x, y: x * y
print(square)
result = square(10, 5)
print(result)

# using conditional statements with a lambda to the greater number

greater = lambda x, y: x if x > y else y
result = greater(5, 10)
print(result)


# Returning a lambda


def myfunc(n):
    return lambda x: x * n


doubler = myfunc(2)
print(doubler(5))
tripler = myfunc(3)
print(tripler(5))

# Tuesday Exercises

tf = (lambda x: True if x > 50 else False)
print(tf(55))

faren = lambda D: ((9 / 5) * D) + 32
print(faren(12))

# Challenge complete
