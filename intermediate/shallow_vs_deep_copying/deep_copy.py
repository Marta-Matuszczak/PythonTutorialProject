import copy

# deep copy
print("\nDeep copy, change first level")
org = [[0, 1], [2, 3, 4]]
cpy = copy.deepcopy(org)
cpy[0] = -12
print(org)
print(cpy)

print("\nDeep copy, change second level")
org = [[0, 1], [2, 3, 4]]
cpy = copy.deepcopy(org)
cpy[0][0] = 7
print(org)
print(cpy)

print("\nDeep copy, change third level")
org = [[[0, 1], [2, 3]], [[4, 5], [6, 7]]]
cpy = copy.deepcopy(org)
cpy[0][0][0] = 7
print(org)
print(cpy)
