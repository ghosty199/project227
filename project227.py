import json
import csv


data_from_txt=[]
with open('data_set.txt', 'r') as f:
	data_from_txt = json.loads(f.read())

csvfilestore = open('data_set.csv', 'w', newline='')
writer=csv.DictWriter(csvfilestore, fieldnames=field_names)


with open('data_set.csv', 'r') as file:
	reader = csv.reader(file)

