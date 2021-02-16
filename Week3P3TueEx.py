# Week 3 Tuesday exercise
word = input("Enter a sentence:\n ")
if "es" in word:
    print("{} contains 'es' in it".format(word))

wo2 = input("Enter a sentence:\n ")
print(wo2[-3::1])
if "ing" in wo2[-3::1]:
    print("{} contains ing in the end".format(wo2))

two_words = input("Enter 2 words:\n")
words = two_words.split(" ")
if words[0].lower() == words[1].lower():
    print("both are same words")

num = input("Enter a number:\n")
num = int(num)
if num<10:
    print("square of number is: ",num*num)

# Tuesday completed for week 3
