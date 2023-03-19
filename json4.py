import json

class Person:
    def __init__(self, name, age, weight) -> None:
        self.name = name
        self.age = age
        self.weight = weight

    def print_info(self):
        print(self.name, self.age, self.weight)

    def get_older(self, years):
        self.age += years
    
    def saveJSON(self, filename):
        person_dict = {'name':self.name, 'age':self.age, 'weight':self.weight}
        with open(filename, 'w') as f:
            f.write(json.dumps(person_dict, indent=2))

    def loadJSON(self, filename):
        with open(filename,'r') as f:
            data = json.loads(f.read())

        self.name = data['name']
        self.age = data['age']
        self.weight = data['weight']

if __name__ == "__main__":

    p1 = Person("Mike", 27, 90)
    p1.print_info()
    p1.get_older(3)
    p1.saveJSON('mike.json')

    p2 = Person(None, 0, 0)
    p2.loadJSON('mike.json')
    p2.print_info()
