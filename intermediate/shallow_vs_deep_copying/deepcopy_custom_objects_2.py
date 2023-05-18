import copy


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


print("Shallow copy")
p1 = Person("Alex", 27)
p2 = Person("Bob", 51)
company = Company(p2, p1)
company_clone = copy.copy(company)
company_clone.boss.age = 52
company.employee.age = 30

print(company.boss.age)
print(company_clone.boss.age)
print(p2.age)

print(company.employee.age)
print(company_clone.employee.age)
print(p1.age)

print("Deep copy")
p1 = Person("Alex", 27)
p2 = Person("Bob", 51)
company = Company(p2, p1)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 52
company.employee.age = 30

print(company.boss.age)
print(company_clone.boss.age)
print(p2.age)

print(company.employee.age)
print(company_clone.employee.age)
print(p1.age)
