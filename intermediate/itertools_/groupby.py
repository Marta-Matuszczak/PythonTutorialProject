import math
from itertools import groupby

"""
def smaller_than_3(x):
    return x < 3
"""

a = [1, 2, 3, 4]

# group_obj = groupby(a, key=smaller_than_3)
group_obj = groupby(a, key=lambda x: x < 3)

for key, value in group_obj:
    print(key, list(value))

names = ["Anna", "Max", "Ernie"]

group_names = groupby(names, key=lambda name: "A" in name or "a" in name)
for key, value in group_names:
    if key:
        desc = "Names with an 'a': "
    else:
        desc = "Names with no 'a': "
    print(desc, list(value))

print("Yes") if "Anna" in names else print("No")
print("Brian" in names)


def rem(x):
    return x % 2 == 0


b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nNot sorted:")
gr = groupby(b, key=lambda x: rem(x))
for key, value in gr:
    print(key, list(value))
print("\nSorted:")
gr = groupby(sorted(b, key=lambda x: rem(x)), key=lambda x: rem(x))
for key, value in gr:
    print(key, list(value))

persons = [
    {"name": "Max", "age": 28}, {"name": "Dan", "age": 25},
    {"name": "Lisa", "age": 27}, {"name": "Anna", "age": 28}
]

age_group = groupby(sorted(persons, key=lambda x: x["age"]), key=lambda x: x["age"])

for key, value in age_group:
    print(key, list(value))
