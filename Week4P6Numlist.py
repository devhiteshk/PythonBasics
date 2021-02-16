# using min, max, and sum

nums = [5, 3, 9]
print(min(nums))         # will find the lowest number in the list
print(max(nums))         # will find the highest number in the list
print(sum(nums))         # will add all numbers in the list and return the sum

# sorting a list
# using .sorted()

nums = [5, 8, 0, 2]
sorted_nums = sorted(nums)
print(nums, sorted_nums)     # original list are left intact

# .sort() changer the original string
nums.sort()
print(nums)


# Conditionals and lists
# using "in" and "not in" words
names = ["Jack", "Robert", "Mary"]
if "Mary" in names:
    print("found")
if "Jimmy" not in names:
    print("not found")

# checking an empty list
nums = []
if not nums:      # same as 'if nums == []'
    print("empty")

# To check for a list with items, you would write the following:
# if nums:

# using for loops
sports = ["Baseball", "Hockey", "Football", "Basketball"]
for sport in sports:
    print(sport)

# Using while loops to remove a certain value
names = ["Bob", "Jack", "Rob", "Bob", "Robert"]
while "Bob" in names:
    names.remove("Bob")    # remove all instances of bob
print(names)

# THURSDAY EXERCISE
# 1 REMOVING DUPLICATES
dup = ["Bob", "Kenny", "Amanda", "Bob", "Kenny"]
j = len(dup) - 1
for i in range(0, j, 1):
    x = dup.count(dup[i])
    if x > 1:
        dup.remove(dup[i])
print(dup)

# 2 user input
i = 0
msg = 0
li1 = []
while msg!="quit":
    inp = input("Enter a word: ")
    if inp != "quit":
        li1.append(inp)
    else:
        msg = inp
j = len(li1)
print("The list is:")
for i in range(0,j,1):
    print(li1[i])

# Challenge Completed
