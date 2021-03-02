# Pandas
#
# When you need to work with data, Pandas is the ultimate tool. It’s essentially Excel on
# steroids. If you’re familiar with the SQL language, this will come easier to you, as Pandas
# is a mix of Python and SQL. By the end of the day, you’ll be able to analyze and work with
# tabular data in a more efficient way than other traditional methods.


# What Is Pandas?
# Pandas is a flexible data analysis library built within the C language, which is excellent
# for working with tabular data. It is currently the de facto standard for Python-based data
# analysis, and fluency in Pandas will do wonders for your productivity and frankly your
# resume. It is one of the fastest ways of getting from zero to answer. Having been written
# in C, it has increased speed when performing calculations. The Pandas module is a high
# performance, highly efficient, and high-level data analysis library. It allows us to work
# with large sets of data called DataFrames.


# Note NumPy is a fundamental package for scientific computing in Python. Built
# from the C language, it uses multidimensional arrays and can perform calculations
# at high-rate speeds.

# The Pandas library is useful in so many ways that you can do any of the following
# and more:
# • Calculate statistics and answer questions about the data like average,
# median, max, and min of each column
# • Finding correlations between columns
# • Tracking the distribution of one or more columns
# • Visualizing the data with the help of matplotlib, using plot bars,
# histograms, etc.
# • Cleaning and filtering data, whether it’s missing or incomplete, just
# by applying a user-defined function (UDF) or built-in function
# • Transforming tabular data into Python to work with
# • Exporting the data into a CSV, other file, or database
# • Feature engineer new columns that can be applied to your analysis
# No matter what you need to do with data, Pandas is your end-all-be-all
# analysis library.


# The following are key terms we’ll be using throughout this section. Be sure to look over
# them and reference them when necessary:
# • Series ➤ One-dimensional labeled array capable of holding data of
# any type
# • DataFrame ➤ Spreadsheet
# • Axis ➤ Column or row, axis = 0 by row; axis = 1 by column
# • Record ➤ A single row
# • dtype ➤ Data type for DataFrame or series object
# • Time Series ➤ Series object that uses time intervals, like tracking weather by the hour


# Import pandas

import pandas as pd

# Creating a DataFrame

# using the from_dict method to convert a dictionary into a Pandas DataFrame

import random

random.seed(3)  # generate same random numbers every time, number used doesn't matter

names = ["Jess", "Jordan", "Sandy", "Ted", "Barney", "Tyler", "Rebecca"]

ages = [random.randint(18, 35) for x in range(len(names))]

people = {"names": names, "ages": ages}
df = pd.DataFrame.from_dict(people)
print(df)

# Accessing data

# directly selecting a column in Pandas

print(df["ages"])
print(df["ages"][3])
# print( df[4] )         # doesn't work, 4 is not a column name


# Indexing by Record

# When you need to access an entire record, you must use loc. This allows us to specify the
# record location via the index. Let’s access the entire first record, then the name within
# that record:

# directly selecting a record in Pandas using .loc
print(df.loc[0])
print(df.loc[0]["names"])

# selecting the value at record 0 in the "names" column

# Slicing a dataframe

# When you want to access a specific number of records, you must slice the DataFrame.
# Slicing in Pandas works the exact same way as a Python list does, using start, stop, and
# step within a set of brackets.

# slicing a DataFrame to grab specific records
print(df[2:5])

# head( )
# When you work with large sets of data, you’ll often want to view a couple records to get
# an idea of what you’re looking at. To see the top records in the DataFrame, along with the
# column names, you use the head() method:


# accessing the top 5 records using .head( )
print(df.head(5))

# tail( )

# To view a given number of records from the bottom, you would use the tail() method:
# # accessing the bottom 3 records using .tail( )
print(df.tail(3))

# keys( )
# Sometimes you’ll need the column names. Whether you’re making a modular script or
# analyzing the data you’re working with, using the keys( ) method will help:
# # accessing the column headers (keys) using the .keys( ) method
headers = df.keys()
print(headers)

# .shape
# The shape of a DataFrame describes the number of records by the number of columns.
# It’s always important to check the shape to ensure you’re working with the proper
# amount of data:
# checking the shape, which is the number of records and columns
print(df.shape)

# describe( )
# The describe method will give you a base analysis for all numerical data. You’ll be able
# to view min, max, 25%, 50%, mean, etc., on all columns just by calling this method on the
# DataFrame. This information is helpful to start your analysis but generally won’t answer
# those questions you’re looking for. Instead, we can use this method as a guideline of
# where to start:

# # checking the general statistics of the DataFrame using .describe( ),
# only works on numerical columns
print(df.describe())

# sort_values( )
# When you need to sort a DataFrame based on column information, you use this method.
# You can pass in one or multiple columns to be sorted by. When passing multiple, you must
# pass them in as a list of column names, in which the first name will take precedence:
# # sort based on a given column, but keep the DataFrame in tact using  sort_values( )
df = df.sort_values("ages")
print(df.head(5))

# Filtration
# Let’s look at how to filter DataFrames for information that meets a specific condition.

# Conditionals
# Rather than filtering out information, we can create a boolean data type column that
# represents the condition we’re checking. Let’s take our current DataFrame and write a
# condition that shows those who are 21 or older and can drink:
# # using a conditional to create a true/false column to work with
can_drink = df["ages"] > 21
print(can_drink)

# Sub-setting
# When you need to filter out records but retain the information within the DataFrame
# you need to use a concept called sub-setting. We’ll use the same condition as earlier,
# except this time we’ll use it to filter out records rather than create a true-false
# representation:

# using sub-setting to filter out records and keep DataFrame intact
print(df[df["ages"] > 21])

# Column Transformations
# Rarely, if ever, will the columns in the original raw DataFrame imported from CSV or a
# database be the ones you need for your analysis. You will spend lots of time constantly
# transforming columns or groups of columns using general computational operations to
# produce new ones that are functions of the old ones. Pandas has full support for this and
# does it efficiently.


# Generating a New Column with Data
# To create a new column within a DataFrame, you use the same syntax as if you were
# adding a new key-value pair into a dictionary. Let’s create a column of fake data that
# represents how long the people within our DataFrame have been customers with our
# company:
# generating a new column of fake data for each record in the DataFrame to represent customer tenure
random.seed(321)
tenure = [random.randint(0, 10) for x in range(len(df))]
df["tenure"] = tenure  # same as adding a new key-value pair in a dictionary
print(df.head())


# apply( )

# Adding new columns based on current data is known as “feature engineering.” It
# makes up a good portion of a data analysts’ job. Often, you won’t be able to answer the
# questions you have from the data you collect. Instead, you need to create your own data
# that is useful to answering questions. For this example, let’s try to answer the following
# question: “What age group does each customer belong to?”. You could look at the persons’
# age and assume their age group; however, we want to make it easier than that. In order to
# answer this question easily, we’ll need to feature engineer a new column that represents
# each customer’s age group. We can do this by using the apply method on the DataFrame.
# The apply method takes in each record, applies the function passed, and sets the value
# returned as the new column data. Let’s check it out:

# feature engineering a new column from known data using a UDF
def ageGroup(age):
    return "Teenager" if age < 21 else "Adult"


df["age_group"] = df["ages"].apply(ageGroup)
print(df.head(10))

# Aggregations
# The raw data plus transformations is generally only half the story. Your objective is
# to extract actual insights and actionable conclusions from the data, and that means
# reducing it from potentially billions of rows to a summary of statistics via aggregation
# functions. This section assumes some knowledge of SQL and the group-by function.
# If you’re not familiar with how group-by works in SQL, visit w3schools3 for reference material.


# groupby()
# In order to condense the information down to a summary of statistics, we’ll need to use
# the groupby method that Pandas has. Whenever you group information together, you
# need to use an aggregate function to let the program know how to group the information
# together. For now, let’s count how many records of each age group there are within our
# DataFrame:

# grouping the records together to count how many records in each group
print(df.groupby("age_group", as_index=False).count().head())

# mean( )
# Instead of counting how many records there are in each category, let’s go ahead and find
# the averages of each column by using the mean method. We’ll group based on the same
# column:

# grouping the data to see averages of all columns
print(df.groupby("age_group", as_index=False).mean().head())

# groupby( ) with Multiple Columns
# When you need to group by multiple columns, the arguments must be passed in as a list.
# The first item in the list will be the main column that the DataFrame is grouped by. In
# our case, let’s check how many adults have a tenure of five years:

# grouping information by their age group, then by their tenure
print(df.groupby(["age_group", "tenure"], as_index=False).count().head(10))

# Adding a record
# To add a record into the DataFrame, you’ll need to access the next index and assign a value as
# a list structure. In our case, the next index would be 7. Let’s add an identical row that already
# exists in our DataFrame, so we can see how to remove duplicate information in the next cell:

# adding a record to the bottom of the DataFrame
df.loc[7] = [25, "Jess", 2, "Adult"]

# add a record
print(df.head(10))

# drop_duplicates( )
# Way too often will you see data with duplicate information, or just duplicate IDs. It’s
# imperative that you remove all duplicate records as it will skew your data, resulting
# in incorrect answers. You can remove duplicate records based on a single column or
# an entire record being identical. In our case, let’s remove duplicates based on similar
# names, which will remove the record we just added into our DataFrame:


# removing duplicates based on same names
df = df.drop_duplicates(subset="names")
print(df.head(10))

# Omitting the subset argument will remove only duplicate records that have
# identical values in all columns.


# Pandas Joins
# Often, you will have to combine data from several different sources to obtain the actual
# dataset you need for your exploration or modeling. Pandas draws heavily on SQL in its
# design for joins.

# Creating a Second DataFrame
# Let’s create a secondary DataFrame to represent our customers posting ratings about
# our company. We’ll create ratings for three users so we can see both inner joins and
# outer joins:
# # creating another fake DataFrame to work with, having same names and a
# new ratings column
ratings = {
    "names": ["Jess", "Tyler", "Ted"],
    "ratings": [10, 9, 6]
}
ratings = df.from_dict(ratings)
ratings.head()


# Inner Join
# Anytime you perform a join, you need a unique column to join the data with. In our
# case, we can use the names column to join the ratings DataFrame with our original
# DataFrame.

# performing an inner join with our df and ratings DataFrames based on names, get data that matches
matched_ratings = df.merge(ratings, on="names", how="inner")
print(matched_ratings.head())


# Outer Join
# If we want to return all the records, but connect the ratings for people who gave one,
# we would need to perform an outer join. This would allow us to keep all records from
# our original DataFrame while adding the ratings column. We need to specify the how
# parameter to “outer”:

# performing an outer join with our df and ratings DataFrames based on names, get all data
all_ratings = df.merge(ratings, on="names", how="outer")
print(all_ratings.head())


# Dataset Pipeline
# A dataset pipeline is a specific process in which we take our data and clean it for our
# model, which will be able to make predictions. This can be a lengthy process if the
# dataset that you use is unclean. A dataset that is not clean will have duplicates records,
# null values everywhere, or unfiltered information that leads to incorrect predictions.
# Here is the general process:


# 1. Performing Exploratory Analysis
# • In this step you want to get to know your data very well. Take
# notes for what you see at a glance or what you may want to clean
# or add. You essentially want to get a feel for what your data has
# to offer. Make note of the number of columns, the data types,
# outliers, null values, and columns that aren’t necessary. This is
# generally when you want to plot out each column of data and
# speculate correlations, non-informational features, etc.


# 2. Data Cleaning
# • Improper cleaning can lead to poor predictions and bad
# datasets. Here, you’ll want to remove unwanted observations
# like duplicates, fix structural errors like columns that have the
# same name but are typos, handle missing data, and filter outlier
# information. This is key for the next step.


# 3. Feature Engineering
# • Creating new information that isn’t depicted by the dataset is
# important. You can use your own expertise if you have knowledge
# of the subject, and you can isolate data which allows your
# algorithms to focus more on the important observations. Here
# you can feature engineer columns into a group, add dummy
# variables, remove unused features, etc. This is where you want to
# expand on the dataset with your own knowledge if you believe
# data is either missing or could be created from the information
# within the dataset.








