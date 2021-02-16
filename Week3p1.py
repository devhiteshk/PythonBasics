# User Input and Conditionals

# accepting and outputting user input
print( input("What is your name? ") )

# saving what the user inputs
ans = input("What is your name? ")
print("Hello {}!".format(ans) )

# checking data type
num = 5
print(type(num))

# converting data types
num = "9"
num = int(num)
print(type(num))

# working with user input to perform calculations
ans = input("Type a number to add: ")
print( type(ans) ) # default type is string, must convert
result = 100 + int(ans)
print( "100 + {} = {}".format(ans, result))


# using the try and except blocks, use tab to indent where necessary
try:
    ans = float( input("Type a number to add: ") )
    print( "100 + {} = {}".format(ans, 100 + ans) )
except:
    print("You did not put in a valid number!")
# without try/except print statement would not get hit if error occurs
print("The program did not break!")










