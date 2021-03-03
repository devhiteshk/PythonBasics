# Scatter Plot
# If you’re familiar with clusters, then you’ll know the importance of scatter plots.
# These types of plots help to distinguish groups apart from each other by plotting a
# dot for each set of data. Using two characteristics, like height and width of a flower,
# we can classify which species a flower belongs to. Let’s create some fake data and
# plot the points:

import random

from matplotlib import pyplot as plt

# creating a scatter plot to represent height-weight distribution

random.seed(2)
height = [random.randint(58, 78) for x in range(20)]

weight = [random.randint(90, 250) for x in range(20)]

plt.scatter(weight, height)
plt.title("Height-Weight Distribution")
plt.xlabel("Weight (lbs)")
plt.ylabel("Height (inches)")
plt.show()

# Histogram
# While line plots are great for visualizing trends in time series data, histograms are the
# king of visualizing distributions. Often, the distribution of a variable is what you’re
# interested in, and a visualization provides a lot more information than a group of
# summary statistics. First, let’s see how we can create a histogram:

# creating a histogram to show age data for a fake population

import numpy as np

# import the numpy module to generate data
np.random.seed(5)

ages = [np.random.normal(loc=40, scale=10) for x in range(1000)]  # ages distributed around 40

plt.hist(ages, bins=45)  # bins is the number of bars
plt.title("Ages per Population")
plt.xlabel("Age")
plt.ylabel("# of People")
plt.show()

# Importance of Histogram Distribution
# To see why histograms are so important with understanding central distribution, we’ll
# need to create some more fake data. We’ll then plot both datasets and see how they
# stack up:


# showing the importance of histogram's display central distribution
florida = [np.random.normal(loc=60, scale=15) for x in range(1000)]

# assume numpy is imported
california = [np.random.normal(loc=35, scale=5) for x in range(1000)]
# chart 1
plt.hist(florida, bins=45, color="r", alpha=0.4)

# alpha is opacity, making it see through
plt.show()
# chart 2
plt.hist(california, bins=45, color="b", alpha=0.4)

# alpha is opacity, making it see through plt.show()
# chart 3
plt.hist(florida, bins=45, color="r", alpha=0.4)

plt.hist(california, bins=45, color="b", alpha=0.4)

# alpha is opacity,

plt.show()

# When rendering several charts, matplotlib understands how to separate
# each plot by resetting the chart to empty after the show method is run, until then
# all information being plotted will be included in one chart.

# Saving the Chart
# Being able to render these charts is wonderful; however, at times you need to use them
# within a presentation. Luckily for us, matplotlib comes with a method that can save the
# charts we create to a file. The savefig() method supports many different file extensions;
# the most common “.jpg” is what we’ll use. Let’s render a simple plot line chart to the local
# folder:

# using savefig method to save the chart as a jpg to the local folder
x, y = [1600, 1700, 1800, 1900, 2000], [0.2, 0.5, 1.1, 2.2, 7.7]

plt.plot(x, y, "bo-")
plt.title("World Population Over Time")

plt.xlabel("Year")
plt.ylabel("Population (billions)")
# plt.savefig("population.png")

# Note You can save the chart in other formats like PDF or PNG.


# Flattening Multidimensional Data
# Generally, in data analysis you want to avoid 3D plotting wherever possible. It’s not
# because the information you want to convey isn’t contained within the result, but
# sometimes it is simply easier to express a point by other means. One of the best ways to
# represent a third dimension is to use color instead of depth.
# For instance, imagine that you have three datasets that you need to plot: height,
# weight, and age. You could render a 3D model, but that would be excessive. Instead,
# you can render the height and weight like we have before on a scatter plot and color
# each dot to represent the age. The third dimension of color is now easily readable rather
# than trying to depict the data using the z axis (depth). Let’s create this exact scatter plot
# together in the following:

# creating a scatter plot to represent height-weight distribution

random.seed(2)
height = [random.randint(58, 78) for x in range(20)]
weight = [random.randint(90, 250) for x in range(20)]
age = [random.randint(18, 65) for x in range(20)]
plt.scatter(weight, height, c=age)
plt.title("Height-Weight Distribution")
plt.xlabel("Weight (lbs)")
plt.ylabel("Height (inches)")
plt.colorbar(label="Age")  # adds color bar to right side
plt.show()





















