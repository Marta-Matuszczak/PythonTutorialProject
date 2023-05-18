import copy

# shallow copy
print("\nShallow copy, change first level, works fine")
org = [[0, 1], [2, 3, 4]]
cpy = copy.copy(org)
cpy[0] = -12
print(org)
print(cpy)

print("\nShallow copy, change second level")
org = [[0, 1], [2, 3, 4]]
cpy = copy.copy(org)
cpy[0][0] = -12
print(org)
print(cpy)

# different ways of shallow copying
cpy1 = copy.copy(org)
cpy2 = org.copy()
cpy3 = list(org)  # using list function
cpy4 = org[:]  # using slicing operator
