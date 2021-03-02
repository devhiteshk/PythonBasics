import pandas as pd

# Creating a DataFrame
import csv

# f = open("top250.csv", "r")
# data = f.read()
# f.close()
# print(data)

with open("top250.csv", mode="r") as f:
    reader = csv.reader(f)
    df = pd.DataFrame.from_dict(reader)

print(df)

# 1: print top 5 data
top5 = df.head(5)
print("\n\n\n", top5)

# how many records are there
print(df.shape)

# data types of each column
print(df.dtypes)

# are there duplicates
duplicateRows = df.duplicated()
print(duplicateRows)

# find null data
print(df.isnull)

# Is there a correlation between two or more columns?
print(df.corr())


