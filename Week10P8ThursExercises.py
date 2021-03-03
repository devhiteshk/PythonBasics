# 2 Print all names of national stadiums

import requests
from bs4 import BeautifulSoup


page = requests.get('https://en.wikipedia.org/wiki/List_of_current_National_Football_League_stadiums')
soup = BeautifulSoup(page.content, 'html.parser')
nfl_stadiums_table = soup.findAll('table')[1]
tbody = list(nfl_stadiums_table.children)[1]

stadiums = []

for i in range(1, len(list(tbody.children))):
    row = list(tbody.children)[i]
    th = row.find('th')
    try:
        stadium_name = th.get_text()
        stadiums.append(stadium_name)
    except:
        pass
for stadium in stadiums:
    print(stadium)

print(len(stadiums))  # should be 31, two teams share a field
