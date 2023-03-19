import json

people = '''
{
    "people":[
        {"name":"John Smith","phone":"615-555-7164","email":"johnsmith@somwhere.com","license":false},
        {"name":"Jane Doe","phone":"560-555-5153","email":"jane@everywhere.co.uk","license":true}
        ]
}
'''

data = json.loads(people)
print(data)
#print(type(data))
#print(type(data['people']))
print([x for x in data['people']])
#print([x['name'] for x in data['people']])
for x in data['people']:
    del x['phone']
#new = json.dumps(data, indent=2)
new = json.dumps(data, indent=2, sort_keys=True)
print(new)