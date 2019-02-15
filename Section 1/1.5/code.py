import urllib.request
wiki = "https://en.wikipedia.org/wiki/List_of_countries_by_the_number_of_billionaires"
page = urllib.request.urlopen(wiki)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page)
print(soup.prettify())

soup.title.text

soup.find('a')

soup.find_all('a')

