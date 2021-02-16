# TUESDAY EXERCISE
# 1: divisible by 3
print("Numbers divisible by 3 till 100\n")
for num in range(1, 101, 1):
    if num % 3 == 0:
        print("{}".format(num))

print("\nFinding vowels in user input\n")
inp = input("Enter a Sentence:\n")
Sto = (len(inp))
for i in range(0, Sto, 1):
    if inp[i] == 'a' or inp[i] == 'A':
        print(inp[i])
    if inp[i] == 'e' or inp[i] == 'E':
        print(inp[i])
    if inp[i] == 'i' or inp[i] == 'I':
        print(inp[i])
    if inp[i] == 'o' or inp[i] == 'O':
        print(inp[i])
    if inp[i] == 'u' or inp[i] == 'U':
        print(inp[i])

# Challenge complete
