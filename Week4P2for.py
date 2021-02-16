# writing your first for loop using range
for num in range(5):
    print("Value: {}".format(num))

# providing the start, stop, and step for the range function
for num in range(2, 10, 2):             # 10 not included : its up to 10
    print("Value: {}".format(num))        # will print all evens between 2 and 10

# printing all characters in a name using the 'in' keyword
name = "John Smith"
for letter in name:
    print("Value: {}".format(letter))

# Continue statement
for num in range(5):
    if num == 3:
        continue     # using the continue statement within a for loop
    print(num)


# Break statement: only break from loop which has break
for num in range(5):
    if num == 3:
        break         # breaking out of a loop using the 'break' keyword
    print(num)


# Pass Statement

# setting a placeholder using the 'pass' keyword
for i in range(5):
    # TODO: add a code to print number
    pass

'''

          If you take the pass statement out completely,the program will
          break because there needs to be some sort of code within the block.

'''