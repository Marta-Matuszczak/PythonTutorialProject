# set is unordered, mutable (changeable), does not allow duplicates
# frozen set is immutable version of a set

a = frozenset([1, 3, 9, 0, 100])
print(a)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}

print(setA.issubset(setB))
print(setB.issubset(setA))
print()
print(setA.issuperset(setB))
print(setB.issuperset(setA))
print()

print(setA.isdisjoint(setB))
setC = {7, 8}
print(setA.isdisjoint(setC))

setD = setA.copy()
setE = set(setA)
setF = setA

setA.add(200)

print(setA)
print(setD)
print(setE)
print(setF)

"""
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)

i2 = odds.intersection(primes)
print(i2)

d = odds.difference(primes)
print(d)

d2 = primes.difference(odds)
print(d2)

d_symmetric = odds.symmetric_difference(primes)
print(d_symmetric)
print()

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3, 7, 8, 9}
print("set A: " + str(setA))
print("set B: " + str(setB))

setC = setA.intersection(setB)
print("Intersection:")
print(setC)

setC = setA.difference(setB)
print("Difference A:")
print(setC)

setC = setB.difference(setA)
print("Difference B:")
print(setC)

setC = setA.symmetric_difference(setB)
print("Symmetric difference:")
print(setC)

setC = setB.union(setA)
print("Union:")
print(setC)

setA.update(setB)
print("Update A:")
print(setA)

setA = {1, 2, 3, 4, 5, 6}
setA.intersection_update(setB)
print("Intersection update A:")
print(setA)

setA = {1, 2, 3, 4, 5, 6}
setA.difference_update(setB)
print("Difference update A:")
print(setA)

setA = {1, 2, 3, 4, 5, 6}
setA.symmetric_difference_update(setB)
print("Symmetric difference update A:")
print(setA)
"""

"""
my_set1 = {6, 4, 1, 5356272, 2}
print(my_set1)
print(type(my_set1))

my_set2 = set([2, 6, 3, 6])
print(type(my_set2))

my_set3 = set("Hello")
print(my_set3)

my_set4 = set()
print(type(my_set4))

my_set4.add(3)
my_set4.add("horse")
print(my_set4)
my_set4.remove(3)
print(my_set4)

print()
print(my_set1)
my_set1.discard(7)
print(my_set1)

print()
if 1 in my_set1:
    print("yes")

print()
for i in my_set1:
    print(i)
"""

# pop() removes arbitrary element
# remove() removes a specified element, returns error if not found
# discard() discards a specified element, does not return error if not found
