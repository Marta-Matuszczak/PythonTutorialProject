# lambda arguments: expression
from functools import reduce

add10 = lambda x: x + 10

print(add10(5))


def add10_func(x):
    return x + 10


print(add10_func(5))

mult = lambda x, y: x * y

print(mult(2, 4))

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
print(points2D)
points2D_sorted = sorted(points2D)
print(points2D_sorted)
points2D_sorted2 = sorted(points2D, key=lambda x: x[1])
print(points2D_sorted2)


def sort_by_y(x):
    return x[1]


points2D_sorted2_func = sorted(points2D, key=sort_by_y)
print(points2D_sorted2_func)

print()

points_s = sorted(points2D, key=lambda x: -x[1])
print(points_s)

sumP = sorted(points2D, key=lambda x: x[0] + x[1])
print(sumP)
print()

a = [1, 2, 3, 4, 5, 6]
# list comprehension
b = [x * 2 for x in a]
print(a)
print(b)

# map function
c = map(lambda x: x * 2, a)
print(list(c))
print()

# filter function
b = filter(lambda x: x % 2 == 0, a)
print(list(b))

c = [x for x in a if x % 2 == 0]
print(c)


a = [1, 2, 3, 4, 5]
# reduce function
product_a = reduce(lambda x, y: x * y, a)
print(product_a)

