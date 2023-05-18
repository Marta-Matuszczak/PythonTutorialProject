import copy


class Person:
    def __init__(self, name, age, kids):
        self.name = name
        self.age = age
        self.kids = kids


print("Reference")
p1 = Person("Alex", 27, ["Anna", "Patrick"])
p2 = p1
p2.kids[0] = "Bob"
print(p1.kids)
print(p2.kids)

print("Shallow copy")
p1 = Person("Alex", 27, ["Anna", "Patrick"])
p2 = copy.copy(p1)
p2.kids[0] = "Bob"
print(p1.kids)
print(p2.kids)

print("Deep copy")
p1 = Person("Alex", 27, ["Anna", "Patrick"])
p2 = copy.deepcopy(p1)
p2.kids[0] = "Bob"
print(p1.kids)
print(p2.kids)