# USING MAP, FILTER, and Reduce

# The map function is used to iterate over a data collection and modify it. The filter
# function is used to iterate over a data collection, and you guessed it… filter out data
# that doesn’t meet a condition. Lastly, the reduce function takes a data collection and
# condenses it down to a single result, like the sum function for lists.

# Map without lambdas

def convertDeg(C):
    return (9 / 5) * C + 32


temps = [12.5, 13.6, 15, 9.2]
converted_Temps = map(convertDeg, temps)
print(converted_Temps)
converted_Temps = list(converted_Temps)
print(converted_Temps)

# maps with lambdas

temps = [12.5, 13.6, 15, 9.2]
converted_Temps = list(map(lambda C: (9 / 5) * C + 32, temps))
print(converted_Temps)


# filter without lambda

def filtertemps(C):
    converted = (9 / 5) * C + 32
    return True if converted > 55 else False


temps = [12.5, 13.6, 15, 9.2]
filtered_temps = filter(filtertemps, temps)
print(filtered_temps)
filtered_temps = list(filtered_temps)
print(filtered_temps)

# filter with lambdas
temps = [12.5, 13.6, 15, 9.2]
filtered_temps = list(filter(lambda C: True if (9 / 5) * C + 32 > 55 else False, temps))
# type convert the filter
print(filtered_temps)

# The problem with reduce
# So now reduce(). This is actually the one I've always hated most, because,
# apart from a few examples involving + or ∗, almost every time I see a
# reduce() call with a non-trivial function argument, I need to grab pen and
# paper to diagram what's actually being fed into that function before I
# understand what the reduce() is supposed to do. So in my mind, the applicability of
# reduce() is pretty much limited to associative operators, and in
# all other cases it's better to write out the accumulation loop explicitly.


# Using reduce

# The reduce function accepts two arguments, the function to perform the execution and
# the data collection to iterate over. Unlike filter and map, however, reduce iterates two
# items at a time instead of one. The result of reduce is to always return a single result.

from functools import reduce

nums = [1, 2, 3, 4]
result = reduce(lambda a, b: a * b, nums)
print(result)


# Wednesday Exercises
# 1

names = ['Ryan', 'Paul', 'Kevin Connors']
result = list(map(lambda x: (x.lower()), names))
print(result)

#2
result = []
names = ["Amanda", "Frank", "abby", "Ripal", "Adam"]
for i in range(len(names)):
    if names[i][0] in ['A', 'a']:
        continue
    else:
        result.append(names[i])

print(result)

# challenge

LamFil = list(filter(lambda x: x[i] if x[i in range(len(x))][0] not in ['A', 'a'] else False, names))
print(LamFil)