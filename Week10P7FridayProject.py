# FRIDAY PROJECT

# importing libraries

import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from bs4 import Comment


# graph results of top 7 words
def displayResults(words, site):
    count = [item[1] for item in words][::-1]  # reverses order
    word = [item[0] for item in words][::-1]  # reverses order

    plt.figure(figsize=(20, 10))  # define how large the figure appears

    plt.bar(word, count)

    plt.title("Analyzing Top Words from: {}...".format(site[:50]), fontname="Sans Serif", fontsize=24)
    plt.xlabel("Words", fontsize=24)
    plt.ylabel("# of Appearances", fontsize=24)
    plt.xticks(fontname="Sans Serif", fontsize=20)
    plt.yticks(fontname="Sans Serif", fontsize=20)

    plt.savefig('microsoft.png')
    plt.show()


# filter article words and hidden characters
def filterWaste(word):
    bad_words = (
    'the', 'a', 'in', 'of', 'to', 'you', '\xa0', 'and', 'at', 'on', 'for', 'from', 'is', 'that', 'are', 'be', '-', 'as',
    '&', 'they', 'with',
    'how', 'was', 'her', 'him', 'i', 'has', '|', 'his')

    if word.lower() in bad_words:
        return False
    else:
        return True


# filter out all elements that do not contain text that appears on site
def filterTags(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False

    if isinstance(element, Comment):
        return False

    return True


# request site and top 7 most used words
def scrape(site):
    page = requests.get(site)

    soup = BeautifulSoup(page.content, 'html.parser')

    text = soup.find_all(text=True)  # will get all text within the document

    visible_text = filter(filterTags, text)

    word_count = {}

    for text in visible_text:
        words = text.replace('\n', '').replace('\t', '').split(' ')  # replace all hidden chars

        words = list(filter(filterWaste, words))

        for word in words:
            if word != '':
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    word_count = sorted(word_count.items(), key=lambda kv: kv[1], reverse=True)

    return word_count[:7]


# main loop should ask if user wants to scrape, then what site to scrape
while input('Would you like to scrape a website (y/n)? ') == 'y':
    try:

        site = input('Enter a website to analyze: ')

        top_words = scrape(site)

        top_word = top_words[0]  # tuple of (word, count)

        print("The top word is: {}".format(top_word[0]))

        displayResults(top_words, site)
    except:
        print('Something went wrong, please try again.')

print('Thanks for analyzing! Come back again!')