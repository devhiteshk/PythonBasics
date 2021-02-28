# introduction to data analysis

# We’ll learn about the Pandas library and how to work with tabular data structures,
# web scraping with BeautifulSoup and understanding how to parse data, as well as data
# visualization libraries like matplotlib. At the end of the week, we’ll use all these libraries
# together to create a small project that scrapes and analyzes web sites.
# Overview
# • Working with Anaconda environments and sending requests
# • Learning how to analyze tabular data structures with Pandas
# • Understanding how to present data using matplotlib
# • Using the BeautifulSoup library to scrape the Web for data
# • Creating a web site analysis tool


# Monday: Virtual Environments and Requests Module

# Today we’ll be learning all about virtual environments, why we need them and how to
# use them. They’re necessary for what we need to do this week, which is downloading
# and importing a few libraries to work with. We’ll also get into the requests module and
# cover APIs briefly.

# What Are Virtual Environments?

# Python virtual environments are essentially a tool that allows you to keep project
# dependencies in a separate space from other projects. Most projects in Python need
# to use modules that are not included by default with Python. Now, you could simply
# download the modules (or libraries) into your Python folder to use; however, that could
# cause some issues down the road. Let’s say you’re working on two separate projects,
# where the first one uses Python version 2.7 and the second project uses Python version
# 3.5. If you try and use the same syntax for both, you’ll run into several issues. Instead,
# you would create two separate virtual environments, one for each project. This way both
# projects can run properly using the correct dependencies because of the personalized
# virtual environment.


# When creating a virtual environment, a folder called “venv ” will appear.
# This is where all the libraries that you download are saved. Simply put, a virtual
# environment is not much more than a folder that stores other files.

# As an analogy to understand virtual environments, first picture our own planet.
# Now think of it as an environment filled with grass, sun, clouds, air, etc. In the case
# of programming, Python would be like the planet, and the grass, sun, clouds, and air
# would be like libraries that you need to include in the environment. As Python does
# not come included with them, we would create a virtual environment to store these
# libraries so that we may import them into our project when needed. If you think of
# Mars, that would be another project, with a separate virtual environment specifically
# made for that program.
# Virtual environments can often be a tough concept to grasp for anyone seeing it
# for the first time, so here’s another analogy. Imagine you’ve planned two vacations,
# one to the beach and the other to go skiing. Rather than using the same suitcase
# filled with mixed clothes, you’ve decided to pack two separate suitcases. The one for
# the beach will include a bathing suit, sunglasses, and flip-flops. The other suitcase
# will include a jacket, skis, and boots. In the following, you can find the relationships
# within this analogy:
# • Vacations                   ➤ Projects
# • Suitcases                   ➤ Virtual Environments
# • Clothes and Accessories     ➤ Project Dependencies/Files


# Remember from the first chapter, when working in terminal, you’ll see the
# $ next to the commands that we enter. For the next few sections, we’ll be working
# inside of terminal.

# What Is Pip?

# Pip is the standard package manager for Python. Anytime you need to download,
# uninstall, or manage a library or module to use within your project, you use pip. It has
# been included in all installations of Python since v3.4. To check your version of pip, write
# the following in terminal:

# $ pip --version

# Creating a Virtual Environment

# $ conda create --name data_analysis python=3.7

# You can create a conda environment from anywhere; you do not need to be
# cd’ed into a specific folder.


# An application programming interface (API) is a set of functions and procedures
# that allow applications to access the features or data of an operating system, application,
# or other service. In a simpler description, APIs allow us to interact with web pages
# and software designed by other developers. Imagine you need some data on housing
# prices. Rather than collecting all that information yourself, you could use the resources
# that major companies like Zillow and Trulia have put together. In order to access
# that information, you need to call their API, which will return the data that you need.
# APIs make a developer’s life easier because we can use data or tools created by other
# companies within our projects.

# Sending a Request
import requests
r = requests.get("https://api.github.com/users/Connor-SM")
print(r)
print(type(r))

# Accessing the response Content
data = r.content
print(data)

# converting the Response from JSON into a python Dictionary
data = r.json()
for k, v in data.items():
    print("Key: {} \t Value: {}".format(k, v))
print(data["name"])         # accessing data directly

# Passing Parameters
# outputting specific key-value pairs from data
r = requests.get("https://api.github.com/search/repositories?q=language:python")
data = r.json()
print(data["total_count"])       # output the total number of repositories that use python

# Monday Exercises
r = requests.get("https://api.github.com/search/repositories?q=language:javaScript")
data = r.json()
print(data["total_count"])


# Output
# <Response [200]>
# <class 'requests.models.Response'>
# b'{"login":"Connor-SM","id":20958711,"node_id":"MDQ6VXNlcjIwOTU4NzEx","avatar_url":"https://avatars.githubusercontent.com/u/20958711?v=4","gravatar_id":"","url":"https://api.github.com/users/Connor-SM","html_url":"https://github.com/Connor-SM","followers_url":"https://api.github.com/users/Connor-SM/followers","following_url":"https://api.github.com/users/Connor-SM/following{/other_user}","gists_url":"https://api.github.com/users/Connor-SM/gists{/gist_id}","starred_url":"https://api.github.com/users/Connor-SM/starred{/owner}{/repo}","subscriptions_url":"https://api.github.com/users/Connor-SM/subscriptions","organizations_url":"https://api.github.com/users/Connor-SM/orgs","repos_url":"https://api.github.com/users/Connor-SM/repos","events_url":"https://api.github.com/users/Connor-SM/events{/privacy}","received_events_url":"https://api.github.com/users/Connor-SM/received_events","type":"User","site_admin":false,"name":"Connor Milliken","company":"HubSpot, Inc.","blog":"www.connormilliken.com","location":"Boston, MA","email":null,"hireable":null,"bio":"- Author of Python Projects for Beginners\\r\\n\\r\\n- Python Instructor\\r\\n\\r\\n- Adventurer/Traveler","twitter_username":null,"public_repos":51,"public_gists":0,"followers":66,"following":36,"created_at":"2016-08-10T22:39:46Z","updated_at":"2021-02-10T15:50:32Z"}'
# Key: login 	 Value: Connor-SM
# Key: id 	 Value: 20958711
# Key: node_id 	 Value: MDQ6VXNlcjIwOTU4NzEx
# Key: avatar_url 	 Value: https://avatars.githubusercontent.com/u/20958711?v=4
# Key: gravatar_id 	 Value:
# Key: url 	 Value: https://api.github.com/users/Connor-SM
# Key: html_url 	 Value: https://github.com/Connor-SM
# Key: followers_url 	 Value: https://api.github.com/users/Connor-SM/followers
# Key: following_url 	 Value: https://api.github.com/users/Connor-SM/following{/other_user}
# Key: gists_url 	 Value: https://api.github.com/users/Connor-SM/gists{/gist_id}
# Key: starred_url 	 Value: https://api.github.com/users/Connor-SM/starred{/owner}{/repo}
# Key: subscriptions_url 	 Value: https://api.github.com/users/Connor-SM/subscriptions
# Key: organizations_url 	 Value: https://api.github.com/users/Connor-SM/orgs
# Key: repos_url 	 Value: https://api.github.com/users/Connor-SM/repos
# Key: events_url 	 Value: https://api.github.com/users/Connor-SM/events{/privacy}
# Key: received_events_url 	 Value: https://api.github.com/users/Connor-SM/received_events
# Key: type 	 Value: User
# Key: site_admin 	 Value: False
# Key: name 	 Value: Connor Milliken
# Key: company 	 Value: HubSpot, Inc.
# Key: blog 	 Value: www.connormilliken.com
# Key: location 	 Value: Boston, MA
# Key: email 	 Value: None
# Key: hireable 	 Value: None
# Key: bio 	 Value: - Author of Python Projects for Beginners
#
# - Python Instructor
#
# - Adventurer/Traveler
# Key: twitter_username 	 Value: None
# Key: public_repos 	 Value: 51
# Key: public_gists 	 Value: 0
# Key: followers 	 Value: 66
# Key: following 	 Value: 36
# Key: created_at 	 Value: 2016-08-10T22:39:46Z
# Key: updated_at 	 Value: 2021-02-10T15:50:32Z
# Connor Milliken
# 6780940
# 13260301









