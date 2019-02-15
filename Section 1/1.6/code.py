import urllib.request
wiki = "https://en.wikipedia.org/wiki/List_of_countries_by_the_number_of_billionaires"
page = urllib.request.urlopen(wiki) 

from bs4 import BeautifulSoup
soup = BeautifulSoup(page)
print (soup.prettify())

soup.title.text

soup.a 
soup.find_all("a")

right_table = soup.find('table',class_ = 'wikitable')
table_body = right_table.find('tbody')
rows = table_body.find_all('tr')

count = 0
data = []

for row in rows:
    if count == 0:
        cols = row.find_all('th')
        cols = [elem.text.strip() for elem in cols]
        data.append([elem for elem in cols if elem])
        count = count + 1
    else:
        cols = row.find_all('td')
        cols = [elem.text.strip() for elem in cols]
        data.append([elem for elem in cols if elem])
        
import pandas as pd
dataframe = pd.DataFrame(columns = data[0])      

for i in range(1,len(data)):
    dataframe = dataframe.append(pd.Series(data[i],index = data[0]),ignore_index = True)






















    