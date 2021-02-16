# help()  to get help from online documentation
# this is 2nd line of the program
# this is third line of the program

# week 1 "FIRST PROGRAM"

# Guessing Game
from random import randint
from IPython.display import clear_output
guessed = False
number = randint(0,100)
guesses = 0
while not guessed:
    ans = input("Try to guess the number i am thinking of")
        # use tab to indent
    guesses += 1
    clear_output()
    if int(ans) == number:
        print("congrats! you guessed it correctly")
        print('if you took { } guesses1'.format(guesses) )
        break
    elif int(ans) > number:
        print("The number is lower than what you guessed.")
    elif int(ans) < number:
        print("The number is greater than what you guessed.")

# Chapter 1 is over Basics of Python in Chapter 2.