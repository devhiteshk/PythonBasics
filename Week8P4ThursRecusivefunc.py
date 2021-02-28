# Thursday : Recursive Functions and Memoization

# Recursion is a concept in programming where a function calls itself one or more times
# within its block. These types of functions can often run into issues with speed, however,
# due to the function constantly calling itself. Memoization helps this process by storing
# values that were already calculated to be used later. Let’s first understand more about
# recursive functions.

# All recursive functions have what is known as a “base case,” or a stopping point.

# Writing a factorial function
def factorial(n):
    # set your base case!
    if n <= 1:
        return 1
    else:
        return factorial(n - 1) * n


print(factorial(10))  # the result of 5*4*3*2*1


# The fibonacci Series

# Each number in the
# sequence is the sum of the previous two numbers, such that fib(5) = fib(4) + fib(3).
# The base case for the Fibonacci sequence is 0 and 1 because the result of fib(2) is
# “fib(2) = fib(1) + fib(0)”

# writing the recursive fibonacci sequence
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(5))

# Understanding Memoization

# When you go to a web page for the first time, your browser takes a little while to load the
# images and files required by the page. The second time you go to the exact same page, it
# usually loads much faster. This is because your browser is using a technique known as
# “caching.” When you loaded the page the first time, it saved the images and files locally.
# The second time you accessed the web page, instead of re-downloading all the images and
# files, it simply loaded them from the cache. This improves our experiences on the Web.
# In computing, memoization is an optimization technique used primarily to speed
# up computer programs by storing the results of previously called functions and returning
# the saved result when trying to calculate the same sequence. This is simply known as
# “caching,”

# Using Memoization

cache = {}  # # used to cache values to be used later


def fib(n):
    if n in cache:
        return cache[n]  # return value stored in dictionary
    result = 0

    # base case
    if n <= 1:
        result = n

    else:
        result = fib(n - 1) + fib(n - 2)

    cache[n] = result
    return result


print(fib(50))  # else it will take weeks to solve fib 50

# Memoization is not perfect; there is a limit to how much you can store in a
# single cache.


# Using @lru_Cache

from functools import lru_cache


@lru_cache()  # python’s built-in memoization/caching system
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(50))

# Thursday exercise

from functools import lru_cache


@lru_cache()
def factorial(n):
    # set your base case!
    if n <= 1:
        return 1
    else:
        return factorial(n - 1) * n


print(factorial(11))

# 2
# SEARCHING DATA

# Look again

lists = [2, 3, [18, 22], 6]
element = 22
V = False
j = 0
for i in range(len(lists)):
    try:
        if element in lists[i]:
            j = j + 1
            V = True

    except:
        if element in lists:
            V = True

print(V)


# by recursion of function


def SearchList(a, b):
    if b in a:
        return True
    for i in range(len(a)):
        if type(a[i]) == list:
            return SearchList(a[i], b)
        elif b in a:
            return True
    else:
        return False


print(SearchList([2, 3, [18, 22], 6], 22))

# Challenge complete
