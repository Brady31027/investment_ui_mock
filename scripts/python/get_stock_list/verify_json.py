import json

def verify_sp500():
	with open(json_data['SP500_list_dist']) as json_file:
		data = json.load(json_file)
		for entry in data['sp500_list']:
			print(entry['symbol']+ ', ' + entry['title'] + ', ' + entry['hq']+  ', ' + entry['sector'] + ', ' + entry['sub_sector'])

def verify_dows():
	pass

def verify_nasdaq():
	pass

input_file = open ('../settings.json')
json_data = json.load(input_file)

verify_sp500() 