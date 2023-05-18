import json

person = {"name": "John", "age": 31, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# serialize - dumps() into string; dump() into file
personJSON = json.dumps(person, indent=4, sort_keys=False)
print(personJSON)

with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

# deserialize
person2 = json.loads(personJSON)
print(person2)

with open("example.json", "r") as file:
    person_from_file = json.load(file)
    print("Hahaha")
    print(person_from_file)
