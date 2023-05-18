# Dictionaries are ordered (from python 3.7) and mutable Key-Value pairs
# list cannot be used as key, tuple can (tuple is immutable type)

my_dict = {
    "name": "Max",
    "age": 26,
    "city": "New York"
}

my_dict4 = {
    "name": "Anna",
    "age": 24,
    "email": "anna@gmail.com"
}

print(my_dict)
my_dict["email"] = "r@g.com"
print(my_dict)


for key, value in my_dict.items():
    print(key)
    print(value)

my_dict1 = dict(my_dict)
my_dict2 = my_dict.copy()
my_dict2.popitem()

print(my_dict)
print(my_dict2)
print()
print()

my_dict.update(my_dict4)
print(my_dict)
