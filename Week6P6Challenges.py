# Palindrome Challenge

word = "nitin"
if word == word[::-1]:
    print("string is palindrome")
else:
    print("not a palindrome")

# Food challenge


import csv

i = 0
while i != 2:
    Choice = int(input("1. Enter food and vote\n2. Done \nChoose between 1 and 2. "))
    if Choice == 1:
        with open("food.csv", mode='w+', newline="") as f:
            writer = csv.DictWriter(f, fieldnames=['Favourite Food?', '# of votes'])
            writer.writeheader()
            writer = csv.writer(f, delimiter=",")
            Fav_Food = input("Enter the name of food: ")
            Vote = input("Vote {} out of 5: ".format(Fav_Food))
            writer.writerow([Fav_Food, Vote])

        f = open("food.csv", 'r')
        data = f.read()
        f.close()
        print(data)


    elif Choice == 2:
        print("Thanks for using our Software")
        break

    else:
        print("That is not an option!!!")
