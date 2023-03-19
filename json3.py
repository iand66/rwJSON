import json

with open('people.json','r') as f:
    jString = json.loads(f.read())

print(jString, type(jString))

for j in jString['people']:
    print(j['name'])

