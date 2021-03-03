# Print all text from a website

from bs4 import BeautifulSoup
import requests

page = requests.get("http://www.york.ac.uk/teaching/cws/wws/webpage1.html")
print(page)
# print(page.content)

soup = BeautifulSoup(page.content, "html.parser")
# print(soup.prettify())

# title = soup.find("p")
# print(title.get_text())   # extracts all text within element

texts = soup.findAll(text=True)

count = 0

for text in texts:
    words = text.replace('\n', '').replace('\t', '').split(' ')

    for word in words:
        if word not in ['', '.', '-']:
            count += 1

print(count)
# Challenge complete




