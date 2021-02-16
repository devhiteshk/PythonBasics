# Wednesday: While loops

# writing while loops

health = 10
while health > 0:
    print(health)
    health -= 1  # forgetting this line result in infinite loop

# While Vs For
# general rule of thumb is counting with for loops, conditions with while loops.


# game_over = False
# while not game_over:
# print(game_over)      # A infinite loop

# Nested Loops
# using two or more loops is called a nested loop

for i in range(2):  # outside loop
    for j in range(3):  # inside loop
        print(i, j)

# Wednesday exercise

# userIP = 1
# while userIP != 'quit':
#    userIP = input("Please enter the input:\n")

game_over = 0
while not game_over:
    for k in range(0, 5, 1):
        if k == 3:
            game_over = True
            break
        else:
            print(k)

# Exercise completed
