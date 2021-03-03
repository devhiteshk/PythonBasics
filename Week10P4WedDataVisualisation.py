# data visualisation

import numpy

# Data visualization is one of the most powerful tools an analyst has for two main reasons.
# Firstly, it is unrivalled in its ability to guide the analyst’s hand in determining “what
# to look at next.” Often, a visual is revealing of patterns in the data that are not easily
# discernable by just looking at DataFrames. Secondly, they are an analyst’s greatest
# communication tool. Professional analysts need to present their results to groups of
# people responsible for acting based on what the data says. Visuals can tell your story
# much better than raw numbers.

# Types of Charts
# Knowing which chart to use is important in presenting your data properly. We’ll go over
# several charts today; however, these are some of the common charts you’ll want to know:
# • Line Chart: Exploring data over time
# • Bar Chart: Comparing categories of data and tracks changes over
# time
# • Pie Chart: Explores parts of a whole, that is, fractions
# • Scatter Plot: Like line charts, tracks correlations between two
# categories
# • Histogram: Unrelated from bar charts, shows distribution of
# variables
# • Candlestick Chart: Used a lot in financial sector, that is, can compare
# a stock over a period
# • Box Chart: Looks identical to candlestick charts, and compares
# minimum, 1st, median, 3rd quartiles, and max values
# Depending on what you need to accomplish in conceptualizing your data, you will
# be able to choose a specific type of chart to portray your data.

from matplotlib import pyplot as plt

# Creating a line plot using x and y coordinates
x, y = [1600, 1700, 1800, 1900, 2000], [0.2, 0.5, 1.1, 2.2, 7.7]

plt.plot(x, y)  # creates the line

plt.title("World Population Over Time")
plt.xlabel("Year")
plt.ylabel("Population (billions)")
plt.show()

# Creating line plot with multiple lines

x1, y1 = [1600, 1700, 1800, 1900, 2000], [0.2, 0.5, 1.1, 2.2, 7.7]
x2, y2 = [1600, 1700, 1800, 1900, 2000], [1, 1, 2, 3, 4]
plt.plot(x1, y1, "rx-", label="Actual")  # create a red solid line with x dots
plt.plot(x2, y2, "bo--", label="Fake")  # create a blue dashed line with circle dots

plt.title("World Population Over Time")
plt.xlabel("Year")
plt.ylabel("Population (billions)")
plt.legend()  # shows labels in best corner
plt.show()


# creating a bar plot using x and y coordinates
num_people, categories = [ 4, 8, 3, 6, 2 ] , [ "Comedy", "Action", "Thriller", "Romance", "Horror" ]
plt.bar(categories, num_people)
plt.title("Favorite Movie Category", fontsize=24)
plt.xlabel("Category", fontsize=16)
plt.ylabel("# of People", fontsize=16)
plt.xticks(fontname="Fantasy")
plt.yticks(fontname="Fantasy")
plt.show()



# Box Plot
# Box plots are useful in situations where you need to compare a single statistic either
# over time or against categories. They are like candlestick charts in their design, where
# you can view the min, max, 25% quartile, 75% quartile, and median, which can be useful
# for displaying data over time. In the case of stocks, currency would be the y axis data
# and time would be the x axis data. For our example, let’s create two separate groups and
# display the heights for each:


# creating a box plot – showing height data for male-female
males, females = [72, 68, 65, 77, 73, 71, 69], [60, 65, 68, 61, 63, 64]
heights = [males, females]
plt.figure(figsize=(15, 8))     # makes chart bigger
plt.boxplot(heights)   # takes in list of data, each box is its own array, heights contains two lists

plt.xticks([1, 2], ["Male", "Female "])  # # sets number of ticks and labels on x-axis
plt.title("Height by Gender", fontsize=22)
plt.ylabel("Height (inches)", fontsize=14)
plt.xlabel("Gender", fontsize=14)
plt.show()





