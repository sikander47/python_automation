import csv
import json
import requests
from testrail import *
from pprint import pprint



client = APIClient('https://aarmaj.testrail.io')
client.user = 'Aarmaj.us@gmail.com'
client.password = 'Testrail1234!'


csvfile = open('complex_data.csv', 'r')
csvfile1 = open('valid_test_id.csv', 'r')


fieldnames = ("email","password")
reader = csv.DictReader( csvfile, fieldnames)

for row,col in zip(csvfile,csvfile1) :
	id = col.split('\n')[0]
	r = requests.post('https://jsonplaceholder.typicode.com/posts', data= row)
	data= r.json()	
	if data['id'] == 101:
		print('Test Passed!')
	# 	client.send_post(
	# 'add_result_for_case/2/'+ id,
	# { 'status_id': 1, 'comment': 'This test worked fine!' }
# )
		
	else :
		print('Test Failed')
# 		client.send_post(
# 	'add_result_for_case/2/'+ id,
# 	{ 'status_id': 5, 'comment': 'This test worked not fine!' }
# )


