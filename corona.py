import pandas as pd
import json
import requests
import time
import texttable as tt
from bs4 import BeautifulSoup


def countrywise():
    url = 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
 
    data = []
 

    data_iterator = iter(soup.find_all('td'))
 

    while True:
        try:
            country = next(data_iterator).text
            confirmed = next(data_iterator).text
            deaths = next(data_iterator).text
            continent = next(data_iterator).text

            data.append((
                country,
                int(confirmed.replace(',', '')),
                int(deaths.replace(',', '')),
                continent
            ))
    

        except StopIteration:
            break
 

    data.sort(key = lambda row: row[1], reverse = True)


    data.sort(key = lambda row: row[1], reverse = True)

    table = tt.Texttable()
    table.add_rows([(None, None, None, None)] + data)
    table.set_cols_align(('c', 'c', 'c', 'c')) 
    table.header((' Country ', ' Number of cases ', ' Deaths ', ' Continent '))
    
    print(table.draw())

def casesActive():
    url = "http://127.0.0.1:5000/"
    res = requests.get(url)
    # HtmlData = res.text
    final_dict = res.json()
    # print(final_dict)
    data = json.dumps(final_dict)
    # print(data)
    df = pd.read_json(data, typ='series', orient='index')
    print("-----------------------------------")
    df = pd.DataFrame(df)
    print(df)
    print("-----------------------------------")
    print("-----------------------------------")


while True:
    casesActive()
    countrywise()
    time.sleep(100)





