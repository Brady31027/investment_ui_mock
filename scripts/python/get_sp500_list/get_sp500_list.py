from urllib import request
from bs4 import BeautifulSoup
import json

def get_constituents():
    req = request.Request(json_data['SP500_list_url'])
    opener = request.urlopen(req)
    content = opener.read().decode() # Convert bytes to UTF-8

    soup = BeautifulSoup(content)
    table = soup.find_all('table')[0] # HTML table we actually need is tables[0] 

    constituents = []
    row = table.findAll('tr')
    for r_idx in range(1, len(row)):
        col = row[r_idx].findAll('td')
        symbol = col[0].text.strip()
        title = col[1].text.strip()
        sector = col[3].text.strip()
        sub_sector = col[4].text.strip()
        hq = col[5].text.strip()
        constituents.append([symbol, title, sector, sub_sector, hq])
    
    return constituents


input_file = open ('../settings.json')
json_data = json.load(input_file)

constituents = get_constituents();
print(constituents)