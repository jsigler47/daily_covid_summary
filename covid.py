import requests
import datetime
from bs4 import BeautifulSoup

print('Gathering data...')
# Get the update page from the cdc
url = 'https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Find the summary data
summary = []
section = soup.find('div', class_='2019coronavirus-summary')
ul = section.find('ul')

# Put the data into a dictionary
s = ul.text
data_list = s.split()
data = {
    'Total Cases': data_list[2],
    'Total Deaths': data_list[5],
    'Jurisdictions reporting cases': data_list[9]
}
now = datetime.datetime.now()
f_date = now.strftime('%F  %T\n')

print(f_date + "\n".join("{}: {}".format(k, v) for k, v in data.items()))

# Store the data in a file
f = open('history.txt', 'a')
f.write("\n" + f_date + "\n".join("{},{}".format(k, v) for k, v in data.items()))
f.close()
