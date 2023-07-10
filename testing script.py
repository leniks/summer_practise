import json
import pprint

with open('data.json') as json_file:
    data = json.load(json_file)

for elem in data:
    print(elem['id'])