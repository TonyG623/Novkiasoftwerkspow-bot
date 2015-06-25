import requests
from BeautifulSoup import *

foodtrucks = requests.get("http://www.chicagofoodtruckfinder.com/weekly-schedule")

soup = BeautifulSoup(foodtrucks.content)

day = 5 # Table column.. hard coded for now

for tr in soup.findAll('tr'):
    if tr.findAll("td"):
        all_tds_in_row = tr.findAll("td")
        location = all_tds_in_row[0].text
        print location
        foodtrucks = all_tds_in_row[day]
        for foodtruck in foodtrucks.findAll("img"):
            print foodtruck["title"]
