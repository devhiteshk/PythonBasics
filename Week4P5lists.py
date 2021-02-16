# Working with lists

# checking length
nums = [5, 10, 15]
length = len(nums)  # len() returns length
print(length)

# Slicing list

# accessing specific items of a lost with slices
print(nums[1:3])  # will output items in index 1 and 2
print(nums[:2])  # will output items in index 0 and 2
print(nums[::2])  # will print every other index - 0,2,4 etc
print(nums[-2:])  # will output the last two items in the list

# adding items to a list by .append()
nums = [10, 20]
nums.append(5)
print(nums)

# insert a value i the list by .list()
words = ["ball", "base"]
words.insert(0, "glove")  # 1st value is index second is value
print(words)

# Removing items by pop()
# using pop to remove items and saving to a variable to use later

items = [5, "ball", True]
items.pop()  # removes last item
removed_item = items.pop(0)  # removes 5 and stores it into variable
print(removed_item, "\n", items)  # only ball left in list now

# .remove() function removes based on list value
sports = ["baseball", "soccer", "football", "hockey"]
try:
    sports.remove("soccer")
except:
    print("That item does not exist in thr list")
print(sports)

# Now the reason why we use a try and
# except with the removal is because if “soccer” didn't exist in the list, then the program
# would crash
