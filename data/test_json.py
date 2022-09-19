import json

with open('cad.json', 'r') as json_file:
    contents = json.load(json_file)

data5 = contents['data'][1:5]

print(data5)