import random
from itertools import product

a = [1, 2, 3]
b = [4, 5, 6]
prod = product(a, b, repeat=2)
print(prod)
print(list(prod))

print()
x = ["good", "bad", "colorful"]
y = ["cat", "dog", "monkey"]
prod = product(x, y)
prod_list = list(prod)
prod_rand = prod_list[random.randrange(len(prod_list))]

print(prod_rand[0] + " " + prod_rand[1])


my_list = [t[0] + " " + t[1] for t in prod_list]
print(my_list)
