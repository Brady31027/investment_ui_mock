import datetime
import requests
import json

constituents = {}
constituents['update_time'] = "{:%B %d, %Y}".format(datetime.datetime.now())
constituents['dow_list'] = []

def get_constituents():
	query_cmd = json_data['FMP_API_DOW_ROOT']+json_data['FMP_API_KEY']
	contents = requests.get(query_cmd).json()
	for entry in contents:		
		constituents['dow_list'].append({
            'symbol': entry['symbol'], 
            'title' : entry['name'], 
            'sector' : entry['sector'], 
            'sub_sector': entry['subSector'],
            'hq': entry['headQuarter'] if entry['headQuarter'] else 'N/A'
        })

input_file = open ('../settings.json')
json_data = json.load(input_file)
get_constituents();

with open(json_data['DOW_LIST_DIST'], 'w') as outfile:
    json.dump(constituents, outfile)
