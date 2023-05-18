org = 5
cpy = org  # new variable with the same reference, both variables point to the same number

# this is not a problem for immutable types, like integer
print("Original: ", org)
print("New reference: ", cpy)

org = 7

print("Original: ", org)
print("New reference: ", cpy)

cpy = 9

print("Original: ", org)
print("New reference: ", cpy)

print()
# this IS a problem for mutable types, like list
org = [1, 2, 3]
cpy = org

print("Original: ", org)
print("New reference: ", cpy)

org.append(7)

print("Original: ", org)
print("New reference: ", cpy)

cpy.append(8)

print("Original: ", org)
print("New reference: ", cpy)