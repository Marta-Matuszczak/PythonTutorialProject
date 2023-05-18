# Tuples are ordered, immutable (unchangeable) and allow duplicate elements
import sys
import timeit

my_list = [1, 2, 3, "Max", "Jim", 45, True]
my_tuple = (1, 2, 3, "Max", "Jim", 45, True)

print(sys.getsizeof(my_list))
print(sys.getsizeof(my_tuple))

# working with tuples can be more efficient compared to lists
print(timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=10000000))
print(timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=10000000))

"""
# unpacking
my_tuple = "Max", 28, "Boston"

name, age, city = my_tuple
print(age)
print()

my_tuple2 = 0, 1, 2, 3, 4, 5, 6, 7

i1, *i2, i3, i4 = my_tuple2
print(i1)
print(i2)
print(i3)
print(i4)
"""

"""
my_list = ["Max", 28, "Boston"]
my_tuple = tuple(my_list)

print(my_tuple)

for i in my_tuple:
    print(i)

if 28 in my_tuple:
    print("yes")
else:
    print("no")
"""

"""
my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(my_tuple)
my_list = list(my_tuple)
print(my_list)

#slicing
b = my_tuple[2:5]
print(b)
c = tuple(my_list[::-3])
print(c)
"""
