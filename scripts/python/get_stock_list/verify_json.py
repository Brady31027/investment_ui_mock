import json

def verify_sp500():
	with open(json_data['SP500_LIST_DIST']) as json_file:
		data = json.load(json_file)
		print('update at: ' + data['update_time'])
		for entry in data['sp500_list']:
			print(entry['symbol']+ ', ' + entry['title'] + ', ' + entry['hq']+  ', ' + entry['sector'] + ', ' + entry['sub_sector'])

def verify_dow():
	with open(json_data['DOW_LIST_DIST']) as json_file:
		data = json.load(json_file)
		print('update at: ' + data['update_time'])
		for entry in data['dow_list']:
			print(entry['symbol']+ ', ' + entry['title'] + ', ' + entry['hq']+  ', ' + entry['sector'] + ', ' + entry['sub_sector'])

def verify_nasdaq():
	with open(json_data['NASDAQ_LIST_DIST']) as json_file:
		data = json.load(json_file)
		print('update at: ' + data['update_time'])
		for entry in data['nasdaq_list']:
			print(entry['symbol']+ ', ' + entry['title'] + ', ' + entry['hq'] +  ', ' + entry['sector'] + ', ' + entry['sub_sector'])

input_file = open ('../settings.json')
json_data = json.load(input_file)

#verify_sp500()
#verify_dow()
verify_nasdaq()