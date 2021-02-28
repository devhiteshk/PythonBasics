# Writing a binary search

import random

# nums = [1,5,55,7,12,23,45,99,100]
nums = [random.randint(0, 20) for i in range(10)]


def binarySearch(aList, num):
    aList.sort()
    while aList:
        mid = len(aList) // 2
        if mid == num:
            return True
        elif mid > num:
            aList = aList[:mid]
        elif mid < num:
            aList = aList[mid + 1:]
    return False

print(sorted(nums))
print(binarySearch(nums, 23))

# Week 8 complete

