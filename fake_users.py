import csv
import json
import requests
from testrail import *
from pprint import pprint


client = APIClient('https://aarmaj.testrail.io')
client.user = 'Aarmaj.us@gmail.com'
client.password = 'Testrail1234!'


csvfile = open('wrong_email.csv', 'r')
csvfile1 = open('invalid_email_id.csv', 'r')

fieldnames = ("email","password")
reader = csv.DictReader( csvfile, fieldnames)
i=12
for row,col in zip(reader,csvfile1):
	id = col.split('\n')[0]
	# print (row)
	r = requests.post('https://reqres.in/api/login',data = row)
	
	if r.status_code == 200:
		print('Test Passed! '+id)
		client.send_post(
	'add_result_for_case/1/' +id,
	{ 'status_id': 5, 'comment': 'This test worked fine!' }
)
		print(id)
		
	else :
		print('Test Failed '+id)
		client.send_post(
	'add_result_for_case/1/'+id,
	{ 'status_id': 1, 'comment': 'This test worked not fine!' }
)


