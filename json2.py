import json

persons = {
    "people":[
        {"name":"Bob","age":28,"weight":80},
        {"name":"Anna","age":34,"weight":67},
        {"name":"Charles","age":45,"weight":78},
        {"name":"Daniel","age":21,"weight":110}
        ]
    }

# Read STR - Write JSON
jString = json.dumps(persons, indent=2)
with open ('people.json','w') as f:
     f.write(jString)