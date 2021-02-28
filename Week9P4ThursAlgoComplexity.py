# Understanding time Complexity

# Today’s focus is primarily on the theory of programming and
# algorithms. If there is a theory in programming that you should understand, it should be
# Big O Notation.

# As a software engineer, you’ll often need to estimate the amount of time a program may
# take to execute. In order to give a proper estimate, you must know the time complexity of
# the program. This is where algorithmic complexity comes in to play, otherwise known as
# Big O Notation. It is the concept to describe how long an algorithm or program takes to
# execute. Take a list, for example. As the number of items within the list grows, so does the
# amount of time it takes to iterate over the list. This is known as O(n), where n represents
# the number of operations. It’s called Big O Notation because you put a “Big O” in front of
# the number of operations.
# Big O establishes a worst-case scenario runtime. Even if you search through a list of
# 100 items and find what you’re looking for on the first try, this would still be considered
# O(100) because it could possibly take up to 100 operations.
# The most efficient Big O Notation is O(1), also known as constant time. It means that
# no matter how many items or steps are required, it will always take the same amount of
# time and generally occurs instantly. If we took the same list of 100 items and accessed
# an index directly, this would be known as O(1). We would retrieve the value in that index
# immediately without needing to iterate over the list.
# One of the least efficient time complexities is O(n∗∗2). This is a representation of
# a double loop. Our Bubble Sort algorithm that we wrote uses a double for loop and is
# known as one of the less efficient sorting algorithms in programming; however, it is
# simple to understand, so it makes for a good introduction into algorithms. We’ll see
# later today how Bubble Sort compares to another algorithm that is designed to be
# much more efficient.


# When you compare a simple search that iterates through each element of a list to
# an efficient algorithm like Binary Search, you begin to see that they don’t grow at the
# same rate over time. Take Table-1 that illustrates the amount of time to search for a
# given item.


# Table 9-1. Big O Notation growth rate comparison1
#  Number of Elements Simple Search Binary Search


# The runtime in Big O Notation         O(n)        O(log n)
#  10                                   10 ms           3 ms
#  100                                  100 ms          7 ms
#  10,000                               10 sec          14 ms
#  1,000,000,000                        11 days         32 ms


# We can clearly see that efficient algorithms can help to improve our programs speed.
# Therefore, it’s important to keep efficiency and time complexity in mind when writing
# your code.

# You should learn more about BigO.


# Hash Tables

# When we originally covered dictionaries, we went over hashing very briefly. Now that
# we’ve covered Big O Notation, understanding hash tables and why they’re important is
# much easier. Dictionaries can be accessed in O(1) complexity because of how they are
# stored in memory. They use hash tables to store the key-value pairs. Before we cover
# hash tables though, let’s have a quick refresher on the hash function and how to use it:

a, c = "bo", 'bob'
b = a
print(hash(a), hash(b), hash(c))

# When dictionaries store key-value pairs into memory, they use this concept. A hash
# table is used to store a hash, a key, and a value. The hash stored is used for when you
# need to retrieve a given value by the key. Take Table 9-2, for instance. There are three
# key-value pairs in place, all with different hash values. When you want to acces the value
# for name, you would write:

# person["name"]

# What happens is Python hashes the string “name” and looks for the hash value
# rather than the key itself. You can think of this like retrieving an item within a list by its
# index. This is much more efficient as you can retrieve values based on hashes almost
# instantly at O(1) time.

# Table 9-2. Logical representation of
# Python hash table
#  Hash                     Key             Value
#  2839702572               Name            John Smith
#  8267348712               Age             32
#  -2398350273              Language        Python

# Dictionaries are helpful data collections for not only keeping information connected
# but also improving efficiency. Keep this in mind when you’re trying to answer
# programming questions or making a program faster. Like the information on Big O
# Notation, this is simply an introduction into hash tables. If you’d like to learn more, be
# sure to look it up using Google, Quora, etc.


# Dictionaries vs. List

# To understand the true power of a hash table and Python dictionaries, let’s compare it
# against a list. We’ll write a conditional statement to have Python check for a given item
# within a dictionary and list, and we’ll time how long each one takes. We’re going to
# separate the code into two cells. The first cell will generate the dictionary and list with 10
# million items:

# creating data collections to test for time complexity

import time

d = {}  # generate fake dictionary
for i in range(10000000):
    d[i] = "value"
big_list = [x for x in range(10000000)]  # generate fake list

# Go ahead and run the cell. Nothing will happen yet. We’ve simply made the variables
# within this cell so that we don’t have to re-create them, as it takes a couple seconds
# depending on your computer. In the following cell, we’re going to keep a timer on how
# long each data collection takes to find the last element. We’ll use the time module in
# order to track the start and end time:

# retrieving information and tracking time to see which is faster
start_time = time.time()        # Tracking time for dictionary
if 9999999 in d:
    print("Found in dictionary")
end_time = time.time() - start_time
print("Elapsed time for dictionary: {}".format(end_time))

start_time = time.time()        # Tracking time for list
if 9999999 in big_list:
    print("Found in list")
end_time = time.time()-start_time
print("Elapsed time for list: {}".format(end_time))

# You’ll notice there’s a large difference between the two times. The list
# will usually take between 1 and 1.5 seconds, whereas the dictionary is almost instant
# every time. Now this doesn't seem like that big of a difference, but what if you needed
# to search for 1000 items. Using a list now becomes a problem, as a dictionary would
# continue to do it instantly, but the list would take much longer.

# Battle of algorithms

# testing bubble sort vs. insertion sort

def bubbleSort(aList):
    for i in range(len(aList)):
        switched = False
        for j in range(len(aList)-1):
            if aList[j] > aList[j+1]:
                aList[j], aList[j+1] = aList[j+1], aList[j]
                switched = True
        if switched == False:
            break
    return aList

def insertionSort(aList):
    for i in range(1,len(aList)):
        if aList[i] < aList[i-1]:
            for j in range(i, 0, -1):
                if aList[j] < aList[j - 1]:
                    aList[j], aList[j+1] = aList[j+1], aList[j]

        else:
            break
    return aList

# Calling bubble sort and insertion sort to test time complexity


from random import randint
nums = [randint(0, 100) for x in range(5000)]
start_time = time.time()        # tracking time bubble sort
bubbleSort(nums)
end_time = time.time() - start_time
print("Elapsed time for Bubble Sort: {}".format(end_time))

start_time = time.time()        # tracking time insertion sort
insertionSort(nums)
end_time = time.time( ) - start_time
print("Elapsed time for Insertion Sort: {}".format(end_time))

# Thursday exercise
# 1
# n(log(n)) for merge sort algorithm
# 9999999 guesses










