# Thursday: Web Scraping
# You may have heard the term “web scraping” previously. In most languages like Python,
# web scraping is comprised of two parts: sending out a request and parsing the data. We’ll
# need to use the requests module for the first part and a library called Beautiful Soup for
# the second part. In a nutshell, the script you write to request data and parse it is called a
# “scraper.”


# importing the beautiful soup and requests library
from bs4 import BeautifulSoup
import requests

# Requesting Page Content
# To begin scraping data, let’s send a request to a simple web page that contains only
# a poem:
# performing a request and outputting the status code

page = requests.get("http://www.arthurleej.com/e-love.html")
print(page)

# outputting the request response content
print(page.content)

# Parsing the Response with Beautiful Soup

# The Beautiful Soup library comes with many attributes and methods that make
# parsing the code easier for ourselves. Using this library, we can make the code easy
# to view, scrape, and traverse through. We’ll need to create a BeautifulSoup object to
# work with by passing the page content into it, along with the type of parser we want
# to use. In our case, we’re working with HTML code, so we’ll need to use the HTML
# parser:


# turning the response into a BeautifulSoup object to extract data
soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())

# Scraping Data
# There are many methods to extract data using Beautiful Soup. The following sections will
# cover a few of the main methods in doing so. Basic HTML knowledge is assumed for this
# section.

# .find( )
# To find a specific element within the code, we can use the find() method. The argument
# we pass is the tag that we want to search for, but it will only find the first instance and
# return it. Meaning that if there are four bold element tags within our code, and we use
# this method to find a bold tag, it will respond back with only the first bold element tag
# found. Let’s try it out:

# using the find method to scrape the text within the first bold tag
title = soup.find("b")
print(title)
print(title.get_text)  # extracts all text within element

# .find_all( )
# To find all instances of a given element, we use the find_all() method. This will give us
# back a list of all tags found within the code. Let’s find all bold tags within the code and
# extract the text:
# get all text within the bold element tag then output each
poem_text = soup.find_all("b")
for text in poem_text:
    print(text.get_text())


# Finding Elements by Attributes
# All HTML elements have attributes associated with them, whether it’s a style, id, class,
# etc., you can use Beautiful Soup to find elements with a specific attribute value. Let’s
# request a response from my personal Github page and find the element that shows my
# username:

# finding an element by specific attribute key-values
page = requests.get("https://github.com/Connor-SM")
soup = BeautifulSoup(page.content, "html.parser")
username = soup.find("span", attrs={"class": "vcard-username"})    # find first span with this class
print(username)         # will show that element has class of vcard-username
print(username.get_text)

# Finding elements by attributes also works with the find_all method. You can
# also include multiple key-value pairs to look for within the attrs argument.


# DOM Traversal
# This section will cover how to extract information by traversing through the DOM
# hierarchy. The DOM, short for Document Object Model, is a concept in web design that
# describes the relationships and structure between elements on a browser. All elements
# on a web page belong to one of three relationships:
# 1. Parent-Child
# 2. Sibling
# 3. Grandparent-Grandchild

# This concept is important to understand when you are web scraping because you
# may need to access the children of a specific element. The children are in reference to all
# elements within another element. Take the following HTML code, for instance:
# <body>
#
# <div>
#
# <h1>Title</h1>
#
# <h3>Sub-title</h3>
#
# <p>Text</p>
#
# </div>
# </body>
# In this example, the <div> element is the parent of the h1, h3, and p elements. Those
# three elements are known as the children. If we wanted to extract all the text from within
# this <div> element, we could access the children elements

# In the preceding example, the h1, h3, and p elements are all siblings. The
# body would be the parent of the div element and the grandparent of the h1, h3,
# and p elements.


# Accessing the Children Attribute
# Lucky for us, when Beautiful Soup converts the page content into an object, it keeps
# track of the children for all elements. This allows us to traverse through the DOM and
# parse data as we see fit. Let’s grab the poem from earlier and convert the response into a
# BeautifulSoup object:

# traversing through the DOM using Beautiful Soup – using the children attribute
page = requests.get("http://www.arthurleej.com/e-love.html")
soup = BeautifulSoup(page.content, "html.parser")
print(soup.children)        # outputs an iterator object

# Understanding the Types of Children
# Before we begin, we first need to understand the types of children within the
# BeautifulSoup object. Let’s convert the iterator into a list of elements that we can
# loop over:

# understanding the children within the soup object
for child in list(soup.children):
    print(type(child))

# Go ahead and run the cell. As a result, we’ll get four children but only three
# different types:
# • <class ‘bs4.element.Doctype’>
# – A Doctype object is in reference to the Docstring that defines the
# HTML version used.
# • <class ‘bs4.element.NavigableString’>
# – A string corresponds to a bit of text within a tag. Beautiful Soup
# uses the NavigableString class to contain these bits of text. So far,
# we’ve used the get_text() method to extract text; however, you can
# use the following to extract data as well:
# >>> tag.string
# Which results in NavigableString type.

# • <class ‘bs4.element.Tag’>
# – A Tag object corresponds to an XML or HTML tag in the original
# document. When we access the elements and their text, we’ll be
# accessing the original tags to do so.


# Accessing the Tag Object
# If we want to access the text within the title tag, we need to traverse into its parent first, which
# happens to be the head tag. Now that we know the elements that we’re looking for reside in
# the Tag object, we need to save that object to a variable and output the sections within it:


# # accessing the .Tag object which holds the html – trying to access the title tag

html = list(soup.children)[2]
for section in html:
    print("\n\n Start of new section")
    print(section)


# Accessing the Head Element Tag
# Now that we know the head element is at index 1 of the HTML children,
# we can perform the same execution to access each child within the head

# accessing the head element using the children attribute
head = list(html.children)[1]
for item in head:
    print("\n\n New Tag")
    print(item)

# Remember that each object stored in these variables is an iterator and can
# be type converted into lists.


# Scraping the Title Text
# The final step is to extract the text from the title tag:

# scraping the title text
title = list(head)[1]
print(title.string)         # .string is used to extract text as well
print(type(title.string))   # results in NavigableString
print(title.get_text())

# The ability to access an object’s children elements allows us to create
# modular or automated web scrapers that can perform a various number of tasks.
# As most sites follow a similar style on their web pages, creating a script that
# would extract information on a single page would allow us to do so on many
# other pages if we knew the proper pattern. For instance, the online statistical
# database for baseball called baseball-reference holds data for all baseball players
# throughout the history of the MLB.Each player has a unique identifier on the web
# site’s URL. If you wrote a parsing script that would extract information for one
# player, you would be able to write a loop to extract information from all players in
# the database.
















































