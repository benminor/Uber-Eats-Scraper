from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json
import ssl
import urllib

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'} # set the headers
ssl._create_default_https_context = ssl._create_unverified_context

data = {}
city = input("Please enter the name of a city: ")
state = input("Enter the abbreviation of your state: ")
url = "https://www.ubereats.com/us/city/" + city.lower() + "-" + state.lower()
req = Request(url, headers={'User-Agent' : 'Mozilla/5.0'})
page = urlopen(req).read()
soup = BeautifulSoup(page, 'html.parser')

for x in soup.findAll('h3'): # find the name of the restaurant
    a = x.findNext('div', attrs = {'class' : 'ag bk'})
    if a is not None:
        time = a.findNext('span').text
        time = time.replace("–"," to ")
        pre_rating = x.findNext('div', attrs = {'class' : 'spacer _16'})
        rating = pre_rating.findNext('div')
        key = x.text
       
        data[key] = []
        data[key].append({
            'Delivery Time' : time,
            'Delivery Cost' : a.text,
            'Rating' : rating.text
        })

with open('final_result.json', 'w+', encoding='utf-8') as out: # writing the ginal file
    json.dump(data, out, indent=4, ensure_ascii=False)
